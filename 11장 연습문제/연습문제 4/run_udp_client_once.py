import socket
import time

server = ('127.0.0.1', 5005)
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.settimeout(3)
    msg = 'hello'
    print(f"[클라이언트] 서버 {server} 로 메시지 전송: {msg}")
    s.sendto(msg.encode(), server)
    try:
        data, addr = s.recvfrom(1024)
        print(f"[클라이언트] 서버 응답: {data.decode()}")
    except Exception as e:
        print(f"[클라이언트] 응답 수신 실패: {e}")
