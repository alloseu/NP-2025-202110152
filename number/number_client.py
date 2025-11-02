import socket

HOST = '서버_IP주소'
PORT = 8002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = input("숫자 입력 (exit 종료): ")
        if msg.lower() == 'exit':
            break
        s.sendall(msg.encode())
        data = s.recv(1024)
        print("결과:", data.decode())
