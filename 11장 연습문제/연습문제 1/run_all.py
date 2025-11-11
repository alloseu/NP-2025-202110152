#!/usr/bin/env python3
"""
연습문제 1 - 전체 실행 스크립트
모든 시간 클라이언트를 순차적으로 실행합니다.
"""

import subprocess
import sys

print("=" * 70)
print(" " * 20 + "연습문제 1 - 전체 실행 결과")
print("=" * 70)

scripts = [
    ("telnet_time_client_basic.py", "Telnet 기본 클라이언트 (Port 13)"),
    ("telnet_time_client_format.py", "Telnet 포맷 클라이언트 (날짜/시간 파싱)"),
    ("udp_time_client.py", "UDP 시간 클라이언트 (Port 37)")
]

for i, (script, description) in enumerate(scripts, 1):
    print(f"\n[{i}] {description}")
    print("-" * 70)
    try:
        result = subprocess.run(
            [sys.executable, script],
            capture_output=True,
            text=True,
            timeout=8
        )
        # stdout만 출력 (stderr는 생략하여 깔끔하게)
        output = result.stdout.strip()
        if output:
            print(output)
        if result.returncode != 0 and result.stderr:
            # 에러가 있으면 표시
            error_lines = [line for line in result.stderr.split('\n') 
                          if 'DeprecationWarning' not in line and line.strip()]
            if error_lines:
                print("⚠️ 에러:", '\n'.join(error_lines))
    except subprocess.TimeoutExpired:
        print("⚠️ 실행 시간 초과")
    except Exception as e:
        print(f"⚠️ 실행 실패: {e}")

print("\n" + "=" * 70)
print("전체 실행 완료")
print("=" * 70)
print("\n📝 프로토콜 설명:")
print("  • Port 13 (Daytime): 텍스트 형식의 날짜/시간 정보")
print("  • Port 37 (Time): 32비트 바이너리 타임스탬프 (1900년 기준)")
print("  • 로컬 서버 사용: 127.0.0.1 (포트 13013, 13037)")
print("\n💡 서버가 실행 중이어야 합니다: python3 time_server.py")
print("=" * 70)
