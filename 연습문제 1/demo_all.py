#!/usr/bin/env python3
"""
연습문제 1 - 모든 시간 클라이언트 실행 데모
네트워크 접근이 제한된 환경에서도 동작을 확인할 수 있도록 수정
"""

import socket
from datetime import datetime

print("=" * 60)
print("연습문제 1 - 시간 프로토콜 클라이언트 실행 결과")
print("=" * 60)

# 1. Telnet 기본 클라이언트 (port 13) 시뮬레이션
print("\n[1] Telnet Time Client (Basic) - Port 13")
print("-" * 60)

# 여러 시간 서버 시도
time_servers = [
    'time.nist.gov',
    'utcnist.colorado.edu',
    'time-a.nist.gov',
    'time-b.nist.gov'
]

connected = False
for HOST in time_servers:
    try:
        import telnetlib
        PORT = 13
        print(f"서버 연결 시도: {HOST}:{PORT}")
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((HOST, PORT))
        response = sock.recv(1024).decode('ascii')
        sock.close()
        
        print(f"✓ 서버 원본 응답: {response}")
        connected = True
        break
        
    except Exception as e:
        print(f"  → 실패: {e}")
        continue

if not connected:
    print("\n모든 서버 연결 실패 - [시뮬레이션 모드]")
    sample_response = "60311 25-11-09 12:34:56 50 0 0 123.4 UTC(NIST) *"
    print(f"서버 원본 응답: {sample_response}")

# 2. Telnet 포맷 클라이언트 (날짜/시간 파싱)
print("\n[2] Telnet Time Client (Format) - Port 13 with Parsing")
print("-" * 60)

connected = False
for HOST in time_servers:
    try:
        import telnetlib
        PORT = 13
        print(f"서버 연결 시도: {HOST}:{PORT}")
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        sock.connect((HOST, PORT))
        response = sock.recv(1024).decode('ascii').strip()
        sock.close()
        
        print(f"✓ 서버 원본 응답: {response}")
        
        parts = response.split()
        if len(parts) >= 3:
            date_str = parts[1] + " " + parts[2]
            dt = datetime.strptime(date_str, "%y-%m-%d %H:%M:%S")
            formatted = dt.strftime("%Y %b %d (%a) %H:%M:%S")
            print(f"✓ 변환된 시각: {formatted}")
        
        connected = True
        break
        
    except Exception as e:
        print(f"  → 실패: {e}")
        continue

if not connected:
    print("\n모든 서버 연결 실패 - [시뮬레이션 모드]")
    sample_response = "60311 25-11-09 12:34:56 50 0 0 123.4 UTC(NIST) *"
    print(f"서버 원본 응답: {sample_response}")
    
    parts = sample_response.split()
    date_str = parts[1] + " " + parts[2]
    dt = datetime.strptime(date_str, "%y-%m-%d %H:%M:%S")
    formatted = dt.strftime("%Y %b %d (%a) %H:%M:%S")
    print(f"변환된 시각: {formatted}")

# 3. UDP Time Client (port 37)
print("\n[3] UDP Time Client - Port 37")
print("-" * 60)

udp_servers = [
    "time.nist.gov",
    "utcnist.colorado.edu",
    "time-a.nist.gov"
]

connected = False
for SERVER in udp_servers:
    try:
        PORT = 37
        print(f"[UDP 요청 전송 중...] {SERVER}:{PORT}")
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(3)
        sock.sendto(b'', (SERVER, PORT))
        data, _ = sock.recvfrom(4)
        sock.close()
        
        print(f"✓ [수신됨] 원시 데이터: {data}")
        
        if len(data) == 4:
            seconds_since_1900 = int.from_bytes(data, byteorder='big')
            seconds_since_1970 = seconds_since_1900 - 2208988800
            dt = datetime.utcfromtimestamp(seconds_since_1970)
            print(f"✓ UDP 방식 현재 시각: {dt.strftime('%Y %b %d (%a) %H:%M:%S')}")
        
        connected = True
        break
        
    except Exception as e:
        print(f"  → 실패: {e}")
        continue

if not connected:
    print("\n모든 서버 연결 실패 - [시뮬레이션 모드]")
    # 현재 시각을 시뮬레이션
    dt = datetime.utcnow()
    seconds_since_1970 = int(dt.timestamp())
    seconds_since_1900 = seconds_since_1970 + 2208988800
    data = seconds_since_1900.to_bytes(4, byteorder='big')
    print(f"[수신됨] 원시 데이터: {data}")
    print(f"UDP 방식 현재 시각: {dt.strftime('%Y %b %d (%a) %H:%M:%S')}")

print("\n" + "=" * 60)
print("실행 완료")
print("=" * 60)
print("\n참고:")
print("- Port 13: Daytime Protocol (텍스트 기반)")
print("- Port 37: Time Protocol (바이너리, 32비트 타임스탬프)")
print("- 네트워크 제한으로 실제 서버 연결 실패 시 시뮬레이션 출력 표시")
print("=" * 60)
