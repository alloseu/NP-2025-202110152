import socket

HOST = ''
PORT = 8001

print("=== Echo 서버 시작 ===")
print(f"포트 {PORT}에서 대기 중...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"\n클라이언트 접속: {addr}")
            print("-" * 50)
            
            while True:
                data = conn.recv(1024)
                if not data:
                    print(f"\n클라이언트 {addr} 연결 종료")
                    print("-" * 50)
                    break
                    
                msg = data.decode()
                print(f"▶ 받은 메시지: {msg}")
                conn.sendall(data)
                print(f"◀ 메시지 반환: {msg}")
