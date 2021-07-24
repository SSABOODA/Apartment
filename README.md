# Final Assignment - 아파트 현관 출입 시스템의 보고서 API

> Description

<!-- 프로젝트에 대한 간단한 설명을 기술한다. 어떠한 일을 수행하기 위한 프로젝트인지, 어떠한 서비스를 위한 것인지를 작성하면 된다. 너무 길게 작성하기 보단 간결하고 명료하게 작성하는 것이 좋다. 프로젝트의 가치를 전달하는 것도 좋다. -->
아파트 관리비 시스템 보고서 API를 만드는 프로젝트입니다. 
관리자의 권한을 이용해 세대별 정보(관리비, 세대호수, 비밀번호)등 확인이 가능하고, 세대원 권한을 이용하면 자신의 세대호수, 비밀번호를 이용하여 오직 자신만의 관리비와 정보를 확인할 수 있도록 API를 구현하였습니다. 

> Environment
<!-- 실행환경에 대해 작성하면 된다. OS나 컴파일러 혹은 Hardware와 관련된 환경을 작성하면 된다. Multicore 환경에서 돌아가는 프로그램이라면 CPU나 RAM 같은 것들을 작성해도 좋다. -->
- mac OS
- Python 3.8
- Django rest framework
- Conda
- Mysql
- Docker

> Prerequisite

1. docker 설치
- 도커 공식 홈페이지에서 도커를 설치합니다.
- <a href="https://www.docker.com/" target="blank">도커 공식 홈페이지</a>

2. docker-compose 명령어 실행
```
# docker-compose 명령어
$ docker-compose up
```

> Files
- requirement.txt : 프로젝트 실행을 위한 모든 설치파일들의 목록을 txt 형식으로 저장해놓은 파일
- my_settings.py : Github에 올라가면 안되는 프로젝트 설정 파일들이 있는 파일 ex(DATABASE, SECETKEY_KEY)
- Dockerfile : Dcoker image를 생성하기 위한 파일
- Docker-compose.yml : docker-compose를 실행하기 위한 명령어를 적어둔 파일이다.
- clients : admin 유저의 token 인증을 위한 파일
- api/admins : 관리자 권한을 가진 사용자가 API 호출 기능을 구현한 파일
- api/publics : 세대원들이 자신의 관리비를 보기 위한 API 기능을 구현한 파일


> Usage

git clone 명령어

```
git clone <현재 repository 주소>
``` 


> tree
```
├── Dockerfile
├── README.md
├── apartment
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── api
│   ├── admins
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── publics
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── urls.py
├── clients
│   ├── token-auth.py
├── docker-compose.yml
├── manage.py
├── my_settings.py
├── requirements.txt
```

> API

- Admins
  - api/admins(관리자 권한 필요 : 로그인 필요)
  ```
  {
    "detail": "Authentication credentials were not provided."
  }
  ```
  - api/admins
  ```

  HTTP 200 OK
  Allow: GET, POST, HEAD, OPTIONS
  Content-Type: application/json
  Vary: Accept

  [
    {
        "id": 1,
        "name": "한성봉",
        "password": "1111",
        "household_number": "0101",
        "payment": "10000.000"
    },
    {
        "id": 2,
        "name": "노성우",
        "password": "2222",
        "household_number": "0102",
        "payment": "20000.000"
    },
    {
        "id": 3,
        "name": "배찬영",
        "password": "3333",
        "household_number": "0103",
        "payment": "30000.000"
    }
  ]
  ```
  - api/admins/<<int:pk>> ex) pk=1
  ```
  [
    {
        "id": 1,
        "name": "한성봉",
        "password": "1111",
        "household_number": "0101",
        "payment": "10000.000"
    }
  ]
  ```
- Publics
  - api/publics (엔드포인트 진입 시 다른 세대원의 정보는 볼 수 없음.)
  ```
  {
    "detail": "Method \"GET\" not allowed."
  }
  ```
  - api/publics
  ```
  # household_number : 0101
  # password : 1111
  {
    "id": 1,
    "name": "한성봉",
    "password": "1111",
    "household_number": "0101",
    "payment": "10000.000"
  }
  ```
  - api/publics (세대 호수, 비밀번호 틀릴 시)
  ```
  HTTP 400 Bad Request
  Allow: POST, OPTIONS
  Content-Type: application/json
  Vary: Accept

  {
    "MESSAGE": "입력하신 정보와 일치하지 않습니다."
  }
  ```
  
  