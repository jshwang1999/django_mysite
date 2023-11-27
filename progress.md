# Django Web Project
## ** Progress of week **
### Function to make

### To Do
1. 11/6 ~ 11/27(13주차) 까지 프로젝트 중간 파일 제출하기(소스코드, 파워포인트 자료)

***
2023.11.06(월) - 10주차
수업 진도: model(https://wikidocs.net/73306)

#### 1. DB와 Python 연결
![img.png](assets%2Fimg.png)
- makemigrations: 모델을 생성하거나 모델에 변화가 있을 경우에 실행해야 하는 명령
- model: Django에서의 db 구현방법
  
#### 2. createsuperuser
- createsuperuser로 admin 계정 생성하기(id: admin, pwd: 1111)

#### 3. admin.py에 질문기능 추가
웹앱에 기능을 추가하고 싶다면, "admin.py" 파일 수정

#### 4. pybo.py에 질문 조회기능 추가
- https://wikidocs.net/70736
템플릿을 활용한다.
settings.py 수정 후, (templates, common, pybo) 디렉토리 생성

404 page not found error 처리까지 완료...

구현한 기능:

***
#### 2023.11.13(월) - 11주차
수업 진도:  
"05. URL 별칭"  
"06. 데이터 저장(https://wikidocs.net/73236)"   
"07. 스태틱"
    - static 디렉토리 생성 후 css 파일로 웹페이지 꾸미기
    - style.css 파일 생성
    - question_detail 파일 수정(load static)   
"08. 부트스트랩(https://wikidocs.net/70838)"
![thread_result.png](assets%2Fthread_result.png)
"09. 템플릿 상속"  
"10. 폼"

GET 방식과 POST 방식   
GET 방식: URL에 데이터를 담아 전달하는 방식(2,000자 한도)   
    - 장점: 북마크 기능 이용시 해당 데이터를 보존할 수 있다.   
    - 단점: 데이터가 URL에 공개되기 때문에 보안이 취약하다   
POST 방식: HTTP Request로 데이터를 전달한다.(글자 수 제한 없음)   
    - 장점: 전달되는 데이터가 노출되지 않으므로 안전하다.   
    - 단점: 새로고침 시 데이터가 모두 사라진다.   

구현한 기능:

***
2023.11.20(월) - 12주차
수업 진도: 
"03. 파이보 서비스 개발!"
~ 03-04 답변 갯수 표시 기능
구현한 기능:

***
2023.11.27(월) - 13주차(중간 성과 제출기간)
수업 진도:   
구현한 기능:   
* 회원가입 기능 
* 로그인 기능 
* 게시글 및 질문글 수정/삭제 기능 구현(3.11)

구현하고 있는 기능: allauth로 소셜로그인 기능 구현
* pip install django_allauth, settings.py에 추가 완료
- **To Dos**
  - 기존 게시글 DB에 작성자 속성(Author) 추가로 migration 진행
    - python manage.py makemigrations > 1 > 1   
    - python manage.py migrate
      - github update project 후 common/login 접속 시도시 'Site Query Does not Exist' 에러 발생   
        -> django_site 테이블과 관련이 있음
        -> config/settings.py의 SITE_ID = n 확인

references:
https://velog.io/@justpotato/django-google로그인-구현하기
https://support-u-oneday.tistory.com/103
https://velog.io/@yevini118/Django-allauth-카카오-로그인하기
***
2023.12.04(월) - 14주차
수업 진도:
구현한 기능:

***
2023.12.11(월) - 15주차 최종발표
<mid>- The End -</mid>

최종적으로_구현한_기능 = ['example', 'etc']