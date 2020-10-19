# 🎫 TicketPlace-Assignment
- (주)티켓플레이스 주니어 백엔드 엔지니어 과제
***

## 🏹 사용된 기술(Stack)
- Django
- Python
- ASW RDS(MySQL)
- Web Crawling
- CORSHeaders
- Restful API

## 📜 PostmanDoc(EndPoint)
- [Link] [https://documenter.getpostman.com/view/11974452/TVYAffuq]
***

## 💻 AQueryTool(Modeling)
- [Link] [https://aquerytool.com:443/aquerymain/index/?rurl=1ed34911-e566-4df4-9b99-86108c1fb6ec&]
- Password : x17f1d

- 해당 사이트에서 모델링을 진행하였고, 크롤링을 한 사이트는 '다음'입니다.
- [Link] [https://search.daum.net/search?w=tot&q=%EC%97%AD%EB%8C%80%EA%B4%80%EA%B0%9D%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR]
- movies 테이블에서 'country_of_manufacture'라는 필드를 없애고 새로 테이블을 만든 후,
movies 테이블과 1:N 관계를 만들어야 하는데 그러지 못했습니다.

- 크롤링을 진행한 후, csv파일로 migrate된 DB에 db_uploader 파일로 데이터를 넣어줬습니다.
***

## 초기화/빌드/테스트 방법
**❗️manage.py가 있는 곳을 home이라고 칭하겠습니다.**
**❗️Django의 포트는 8000입니다. 따라서 http://localhost:8000/movie로 EndPoint에 접근해 주시면 됩니다.

git clone을 해주세요.
가상환경을 하나 만드시고, `pip install -r requirements.txt`를 해주세요.
가상환경에 MySQL도 설치를 한 후, primary 파일에 해당 Local DB의 정보를 입력해 주세요.(USER, PASSWORD, HOST)
Local DB에 접속 후, `create database ticket_place character set utf8mb4 collate utf8mb4_general_ci;`명령어로 DB를 만들어주세요.
home에서 `python manage.py migrate` 명령어를 실행해 주어 DB에 테이블들을 만들어주세요.
home에서 `python db_uploader.py` 명령어로 csv 파일에 있는 데이터를 DB에 넣어주세요.
home에서 `python manage.py runserver`명령어를 이용해 서버를 실행 해주세요.
PostmanDoc을 보시면서 테스트 해보실 EndPoint에 요청을 보내시면 됩니다.
