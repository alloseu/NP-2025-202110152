#!/usr/bin/env python3
"""
로컬 시간 서버 (테스트용)
- Port 13: Daytime Protocol (TCP)
- Port 37: Time Protocol (UDP)
"""

import socket
import threading
from datetime import datetime
import time

def daytime_server(port=13013):  # 권한 문제로 높은 포트 사용
    """Port 13 스타일 Daytime 서버"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', port))
    server.listen(5)
    print(f"✓ Daytime 서버 시작: 127.0.0.1:{port}")
    
    while True:
        try:
            client, addr = server.accept()
            now = datetime.utcnow()
            
            # NIST 형식 응답 생성
            mjd = int((now - datetime(1858, 11, 17)).total_seconds() / 86400)
            response = f"{mjd} {now.strftime('%y-%m-%d %H:%M:%S')} 50 0 0 123.4 UTC(NIST) *\n"
            
            client.sendall(response.encode('ascii'))
            client.close()
            print(f"  → 클라이언트 응답: {addr}")
        except Exception as e:
            print(f"  → 에러: {e}")
            break

def time_server_udp(port=13037):  # 권한 문제로 높은 포트 사용
    """Port 37 스타일 Time 서버 (UDP)"""
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(('127.0.0.1', port))
    print(f"✓ Time 서버(UDP) 시작: 127.0.0.1:{port}")
    
    while True:
        try:
            data, addr = server.recvfrom(1024)
            # 1900년 1월 1일부터의 초 계산
            now = datetime.utcnow()
            seconds_since_1970 = int(now.timestamp())
            seconds_since_1900 = seconds_since_1970 + 2208988800
            
            response = seconds_since_1900.to_bytes(4, byteorder='big')
            server.sendto(response, addr)
            print(f"  → UDP 클라이언트 응답: {addr}")
        except Exception as e:
            print(f"  → 에러: {e}")
            break

if __name__ == '__main__':
    print("=" * 60)
    print("로컬 시간 서버 시작")
    print("=" * 60)
    
    # TCP Daytime 서버 스레드
    tcp_thread = threading.Thread(target=daytime_server, daemon=True)
    tcp_thread.start()
    
    # UDP Time 서버 스레드
    udp_thread = threading.Thread(target=time_server_udp, daemon=True)
    udp_thread.start()
    
    print("\n서버가 실행 중입니다. Ctrl+C로 종료하세요.")
    print("=" * 60)
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n서버를 종료합니다.")
