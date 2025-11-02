import threading
import socket
import datetime
import time
HOST = '127.0.0.1'
PORT = 8000

def server_func():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"[SERVER] Time server started on {HOST}:{PORT}...")
        conn, addr = s.accept()
        with conn:
            print(f"[CONNECTED] {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                conn.sendall(current_time.encode())

def client_func():
    time.sleep(0.2)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"TIME")
        data = s.recv(1024)
    print("서버 시간:", data.decode())

if __name__ == '__main__':
    srv = threading.Thread(target=server_func, daemon=True)
    srv.start()
    client_func()
    time.sleep(0.1)
