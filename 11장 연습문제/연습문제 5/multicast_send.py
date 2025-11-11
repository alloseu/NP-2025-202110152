from socket import *
import struct

group_addr = ("224.0.0.255", 5005)
s_sock = socket(AF_INET, SOCK_DGRAM)
TTL = struct.pack('@i', 2)

# TTL 및 루프백 설정
s_sock.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, TTL)
# 로컬 수신(루프백) 허용: 같은 호스트의 수신기가 패킷을 받도록 1로 설정
s_sock.setsockopt(IPPROTO_IP, IP_MULTICAST_LOOP, 1)
# 타임아웃을 약간 늘려 ACK 수신 여유를 줌
s_sock.settimeout(1.0)

print("멀티캐스트 송신기 시작 (224.0.0.255:5005)", flush=True)
while True:
    rmsg = input("보낼 메시지 입력: ")
    s_sock.sendto(rmsg.encode(), group_addr)
    try:
        response, addr = s_sock.recvfrom(1024)
        print(f"응답 수신: {response.decode()} from {addr}", flush=True)
    except timeout:
        pass
