from socket import *
import sys

sock = socket(AF_INET, SOCK_DGRAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind(('', 10000))  # 모든 인터페이스 수신

def main():
    print("[서버] 브로드캐스트 수신 대기 중...", flush=True)
    try:
        while True:
            try:
                msg, addr = sock.recvfrom(1024)
                print(f"[수신] {addr} -> {msg.decode()}", flush=True)
            except KeyboardInterrupt:
                print("[서버] KeyboardInterrupt: 종료합니다", flush=True)
                break
            except Exception as e:
                # 개별 수신 예외는 로그로 남기고 루프 계속
                print(f"[서버] recv 예외: {e}", flush=True)
    finally:
        try:
            sock.close()
        except Exception:
            pass

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"[서버] 예외로 종료: {e}", file=sys.stderr, flush=True)
        raise