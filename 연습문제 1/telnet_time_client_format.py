import socket
from datetime import datetime

HOST = '127.0.0.1'
PORT = 13013

print(f"연결 중: {HOST}:{PORT}")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)

try:
    sock.connect((HOST, PORT))
    response = sock.recv(1024).decode('ascii').strip()
    print("서버 원본 응답:", response)
    
    # 응답 예시: "60988 25-11-09 10:42:37 50 0 0 123.4 UTC(NIST) *"
    parts = response.split()
    
    if len(parts) >= 3:
        date_str = parts[1] + " " + parts[2]  # "25-11-09 10:42:37"
        dt = datetime.strptime(date_str, "%y-%m-%d %H:%M:%S")
    
        # 형식 변환
        formatted = dt.strftime("%Y %b %d (%a) %H:%M:%S")
        print("변환된 시각:", formatted)
    else:
        print("⚠️ 서버 응답 형식이 예상과 다릅니다.")
        
except Exception as e:
    print(f"연결 실패: {e}")
    print("\n💡 먼저 로컬 서버를 실행하세요: python3 time_server.py")
finally:
    sock.close()