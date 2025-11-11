import socket
import sys

def get_port_from_args():
    if '-p' in sys.argv:
        index = sys.argv.index('-p') + 1
        if index < len(sys.argv):
            return int(sys.argv[index])
    return 2500  # 기본 포트

PORT = get_port_from_args()
SERVER = 'localhost'  # 서버가 로컬에서 실행 중인 경우

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((SERVER, PORT))
    message = input("서버로 보낼 메시지 입력: ")
    sock.send(message.encode())

    data = sock.recv(1024)
    print(f"[서버 응답] {data.decode()}")