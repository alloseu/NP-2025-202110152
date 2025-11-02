import socket

HOST = ''
PORT = 8002

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[SERVER] Number server running on port {PORT}...")

    conn, addr = s.accept()
    with conn:
        print(f"[CONNECTED] {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            try:
                n = int(data.decode())
                result = sum(range(1, n + 1))
                conn.sendall(str(result).encode())
            except ValueError:
                conn.sendall(b"Error: invalid number")