import socket

HOST = '127.0.0.1'  
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"TIME")
    data = s.recv(1024)

print("서버 시간:", data.decode())

