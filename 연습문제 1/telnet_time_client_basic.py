import socket

# 로컬 테스트 서버 사용 (time_server.py 실행 필요)
HOST = '127.0.0.1'  # 로컬호스트
PORT = 13013  # Daytime protocol port (로컬 테스트용)

print(f"연결 중: {HOST}:{PORT}")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)

try:
    sock.connect((HOST, PORT))
    response = sock.recv(1024).decode('ascii')
    print("서버 원본 응답:", response.strip())
except Exception as e:
    print(f"연결 실패: {e}")
    print("\n💡 먼저 로컬 서버를 실행하세요: python3 time_server.py")
finally:
    sock.close()