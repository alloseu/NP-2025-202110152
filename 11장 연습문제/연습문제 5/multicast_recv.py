from socket import *
import struct
import sys, traceback

print("[DEBUG] multicast_recv starting", flush=True)
try:
    BUFFER = 1024
    group_addr = "224.0.0.255"

    r_sock = socket(AF_INET, SOCK_DGRAM)
    r_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    r_sock.bind(("", 5005))

    # 그룹 가입
    mreq = struct.pack("4sl", inet_aton(group_addr), INADDR_ANY)
    r_sock.setsockopt(IPPROTO_IP, IP_ADD_MEMBERSHIP, mreq)

    print("Ready to receive multicast message...", flush=True)
    while True:
        rmsg, addr = r_sock.recvfrom(BUFFER)
        print(f"Received '{rmsg.decode()}' from {addr}", flush=True)
        r_sock.sendto('ACK'.encode(), addr)
except Exception as e:
    print("[ERROR] multicast_recv exception:", e, file=sys.stderr, flush=True)
    traceback.print_exc()
    # re-raise so caller sees it if running interactively
    raise
