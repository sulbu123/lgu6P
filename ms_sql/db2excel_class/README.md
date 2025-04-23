# 프로젝트 개요
- 잠깐씩 사용

# 기능 명세서
- 이 프로젝트 안에는 00 기능이 있다.

## Main Function
- MS-SQL, MYSQL을 파이썬과 연동 및 쿼리 기능 지원 (클래스 구현)
    + DB2EXCEL 클래스
        - 연결기능
        - 쿼리실행기능
        - 액셀 내보내기
- 웹 대시보드를 통해서 간단하게 테스트 할 수 있다.
    + 포트번호 입력
    + 사용자 입력
    + 패스워드 입력

## 기대효과
- 웹 배포 후, 전국 어디에서든지, 쿼리 연습 가능

## DB
- MS-SQL 링크 : https://
- MYSQL 링크 : https://

# 사용법
- 셀프 테스트 방법
-개발환경 조건 및 설치
- 파이썬 3.11.6 버전에서 진행
- 가상환경 설치
- 라이브러리 실행
- streamlit 웹 실행

'''bash
git clone https://
virtual venv
source venv/Scripts/activate  
(venv)  streamlit run app.py

## 개선사항
- 한글 인코딩 문제 발생 (현재 버그 수정 중)