from socket import *

# 1회용 브로드캐스트 클라이언트: 255.255.255.255로 메시지 전송 후 종료
addr = ('255.255.255.255', 10000)

sock = socket(AF_INET, SOCK_DGRAM)
# 브로드캐스트를 허용
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

msg = 'test-broadcast-255'
print(f"[클라이언트 테스트] 주소 {addr} 로 메시지 전송: {msg}")
sock.sendto(msg.encode(), addr)
sock.close()
print("[클라이언트 테스트] 전송 완료")
