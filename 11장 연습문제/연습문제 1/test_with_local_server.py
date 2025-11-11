#!/usr/bin/env python3
"""
연습문제 1 - 로컬 서버를 사용한 실제 동작 테스트
"""

import socket
from datetime import datetime
import time

print("=" * 60)
print("연습문제 1 - 시간 프로토콜 클라이언트 실행 결과")
print("=" * 60)

# 로컬 서버 사용
LOCAL_HOST = '127.0.0.1'
TCP_PORT = 13013  # Daytime
UDP_PORT = 13037  # Time

# 1. Telnet 기본 클라이언트 (port 13) 
print("\n[1] Telnet Time Client (Basic) - Port 13")
print("-" * 60)
try:
    print(f"서버 연결 시도: {LOCAL_HOST}:{TCP_PORT}")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    sock.connect((LOCAL_HOST, TCP_PORT))
    response = sock.recv(1024).decode('ascii')
    sock.close()
    
    print(f"✓ 서버 원본 응답: {response.strip()}")
    
except Exception as e:
    print(f"✗ 연결 실패: {e}")
    print("\n💡 로컬 서버를 먼저 실행해주세요:")
    print("   python3 time_server.py")

# 2. Telnet 포맷 클라이언트 (날짜/시간 파싱)
print("\n[2] Telnet Time Client (Format) - Port 13 with Parsing")
print("-" * 60)
try:
    print(f"서버 연결 시도: {LOCAL_HOST}:{TCP_PORT}")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    sock.connect((LOCAL_HOST, TCP_PORT))
    response = sock.recv(1024).decode('ascii').strip()
    sock.close()
    
    print(f"✓ 서버 원본 응답: {response}")
    
    parts = response.split()
    if len(parts) >= 3:
        date_str = parts[1] + " " + parts[2]
        dt = datetime.strptime(date_str, "%y-%m-%d %H:%M:%S")
        formatted = dt.strftime("%Y %b %d (%a) %H:%M:%S")
        print(f"✓ 변환된 시각: {formatted}")
    
except Exception as e:
    print(f"✗ 연결 실패: {e}")
    print("\n💡 로컬 서버를 먼저 실행해주세요:")
    print("   python3 time_server.py")

# 3. UDP Time Client (port 37)
print("\n[3] UDP Time Client - Port 37")
print("-" * 60)
try:
    print(f"[UDP 요청 전송 중...] {LOCAL_HOST}:{UDP_PORT}")
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(3)
    sock.sendto(b'', (LOCAL_HOST, UDP_PORT))
    data, _ = sock.recvfrom(4)
    sock.close()
    
    print(f"✓ [수신됨] 원시 데이터: {data} (hex: {data.hex()})")
    
    if len(data) == 4:
        seconds_since_1900 = int.from_bytes(data, byteorder='big')
        seconds_since_1970 = seconds_since_1900 - 2208988800
        dt = datetime.utcfromtimestamp(seconds_since_1970)
        print(f"✓ UDP 방식 현재 시각: {dt.strftime('%Y %b %d (%a) %H:%M:%S')}")
        print(f"   (타임스탬프: {seconds_since_1900} since 1900, {seconds_since_1970} since 1970)")
    
except Exception as e:
    print(f"✗ [UDP 오류 발생] {e}")
    print("\n💡 로컬 서버를 먼저 실행해주세요:")
    print("   python3 time_server.py")

print("\n" + "=" * 60)
print("실행 완료")
print("=" * 60)
print("\n📝 참고:")
print("- Port 13: Daytime Protocol (텍스트 기반)")
print("- Port 37: Time Protocol (바이너리, 32비트 타임스탬프)")
print("- 로컬 테스트: 127.0.0.1 사용 (포트 13013, 13037)")
print("=" * 60)
