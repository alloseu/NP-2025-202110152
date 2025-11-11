#!/usr/bin/env python3
from socket import *
import struct
import sys

# usage: multicast_send_once.py [message]
msg = 'one-shot-default'
if len(sys.argv) > 1:
    msg = ' '.join(sys.argv[1:])

group_addr = ("224.0.0.255", 5005)

s_sock = socket(AF_INET, SOCK_DGRAM)
TTL = struct.pack('@i', 2)
# TTL 및 루프백 설정 (로컬 테스트 허용)
s_sock.setsockopt(IPPROTO_IP, IP_MULTICAST_TTL, TTL)
s_sock.setsockopt(IPPROTO_IP, IP_MULTICAST_LOOP, 1)
s_sock.settimeout(2.0)

print(f"[송신기-one-shot] 전송: {msg} -> {group_addr}")
try:
    s_sock.sendto(msg.encode(), group_addr)
    try:
        response, addr = s_sock.recvfrom(1024)
        print(f"[송신기-one-shot] 응답 수신: {response.decode()} from {addr}")
    except Exception as e:
        print(f"[송신기-one-shot] 응답 없음: {e}")
finally:
    s_sock.close()
