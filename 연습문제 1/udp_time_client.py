import socket
from datetime import datetime

# 로컬 테스트 서버 사용
SERVER = "127.0.0.1"
PORT = 13037

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(5)

try:
    print(f"[UDP 요청 전송 중...] {SERVER}:{PORT}")
    sock.sendto(b'', (SERVER, PORT))
    data, _ = sock.recvfrom(4)
    print(f"[수신됨] 원시 데이터: {data} (hex: {data.hex()})")

    if len(data) == 4:
        seconds_since_1900 = int.from_bytes(data, byteorder='big')
        seconds_since_1970 = seconds_since_1900 - 2208988800  # UNIX 시간 보정
        dt = datetime.utcfromtimestamp(seconds_since_1970)
        print("UDP 방식 현재 시각:", dt.strftime("%Y %b %d (%a) %H:%M:%S"))
        print(f"  (타임스탬프: {seconds_since_1900} since 1900)")
    else:
        print("⚠️ 데이터 길이 이상")
except Exception as e:
    print(f"[UDP 오류 발생] {e}")
    print("\n💡 먼저 로컬 서버를 실행하세요: python3 time_server.py")
finally:
    sock.close()