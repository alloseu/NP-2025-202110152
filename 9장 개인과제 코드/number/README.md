# NP-2025-202110152

## 9장 과제 - Number Client/Server

간단한 TCP 숫자 합 계산기 예제입니다.

### 구성
- `number_server.py` : 서버(클라이언트로부터 숫자 하나를 받아 1..n 합을 반환)
- `number_client.py` : 상호작용형 클라이언트
- `number_client_test.py` : non-interactive 테스트 클라이언트 (자동 전송)

### 실행 방법
1. 서버 실행:
```bash
python number_server.py
```

2. 클라이언트 실행(새 터미널):
```bash
python number_client.py
```

### 문제 해결
- 서버가 포트를 이미 사용 중이면 다른 포트를 사용하거나 해당 프로세스를 종료하세요.
- Windows에서 연결 오류가 계속되면 방화벽 설정을 확인하세요.
