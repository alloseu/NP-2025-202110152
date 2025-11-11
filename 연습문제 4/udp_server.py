import socket

class UDPServer:
    def __init__(self, host='0.0.0.0', port=5005):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        print(f"[서버] UDP 서버 실행 중... 포트: {self.port}")

    def run(self):
        while True:
            data, addr = self.sock.recvfrom(1024)
            message = data.decode()
            print(f"[수신] {addr} → {message}")

            # 클라이언트에게 응답 전송
            response = f"서버 응답: {message}"
            self.sock.sendto(response.encode(), addr)

if __name__ == "__main__":
    server = UDPServer(port=5005)
    server.run()