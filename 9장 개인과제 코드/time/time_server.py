import socket
import datetime

HOST = ''         
PORT = 8000       

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[SERVER] Time server started on port {PORT}...")

    conn, addr = s.accept()
    with conn:
        print(f"[CONNECTED] {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conn.sendall(current_time.encode())

