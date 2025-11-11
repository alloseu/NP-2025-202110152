import socket
import threading

HOST = ''      # 모든 인터페이스에서 접속 허용
PORT = 2500    # 기본 포트


def handle_client(client_socket: socket.socket, addr):
    """클라이언트 연결을 처리하는 함수(스레드별 실행)."""
    with client_socket:
        print(f"[접속됨] 클라이언트: {addr}")
        while True:
            try:
                data = client_socket.recv(1024)
            except ConnectionResetError:
                break
            if not data:
                break
            try:
                msg = data.decode()
            except Exception:
                msg = repr(data)
            print(f"[수신] {msg}")
            # 그대로 다시 전송 (Echo)
            try:
                client_socket.sendall(data)
            except BrokenPipeError:
                break
    print(f"[종료] 연결 종료: {addr}")


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 주소 재사용 플래그 설정 (빠른 재시작 허용)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"[서버 실행 중] 포트 {PORT}에서 연결 대기 중...")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            # 각 연결을 새 데몬 스레드로 처리
            t = threading.Thread(target=handle_client, args=(client_socket, addr), daemon=True)
            t.start()
    except KeyboardInterrupt:
        print("[서버] 종료 신호(KeyboardInterrupt) 수신 - 종료 중...")
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()