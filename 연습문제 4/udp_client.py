import socket

class UDPClient:
    def __init__(self, server_ip, server_port=5005):
        self.server_ip = server_ip
        self.server_port = server_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print(f"[클라이언트] {self.server_ip}:{self.server_port} 에 연결 준비 완료")

    def run(self):
        try:
            while True:
                message = input("서버로 보낼 메시지를 입력하세요 (종료: exit): ")
                if message.lower() == 'exit':
                    break

                self.sock.sendto(message.encode(), (self.server_ip, self.server_port))
                data, _ = self.sock.recvfrom(1024)
                print(f"[서버 응답] {data.decode()}")
        finally:
            self.sock.close()

if __name__ == "__main__":
    # 기본 서버 IP를 로컬호스트로 설정했습니다. 필요하면 명령행이나 파일을 수정하세요.
    client = UDPClient(server_ip="127.0.0.1", server_port=5005)
    client.run()
