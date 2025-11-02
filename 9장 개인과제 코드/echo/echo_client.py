import socket

HOST = 'localhost'  # 로컬 테스트용
PORT = 8001

print("=== Echo 클라이언트 시작 ===")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"서버 {HOST}:{PORT}에 연결 중...")
    s.connect((HOST, PORT))
    print("서버에 연결되었습니다!")
    print("\n메시지를 입력하세요. 'exit'를 입력하면 종료됩니다.")
    print("-" * 50)
    
    while True:
        msg = input("\n▶ 보낼 메시지: ")
        if msg.lower() == 'exit':
            print("\n클라이언트를 종료합니다.")
            break
        s.sendall(msg.encode())
        data = s.recv(1024)
        print("◀ 서버 응답:", data.decode())
