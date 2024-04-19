
## * Description

   * ### Project name : Sparta Market 
스파르타만의 중고거래 플렛폼을 구현

   * ### Project duration : 2024-04-12 ~ 2024-04-09
개인프로젝트이므로 본인이 설계 구현 모두 담당

*  ## Environment & Tech stack
Window 환경에서 Pycham 사용. 

Python(3.10) , Django Framework (4.2.11) 사용

SQLite3 사용

* [![Bootstrap][Bootstrap.com]][Bootstrap-url]

### Prerequisite

Package|Version
---|---|
asgiref            |3.8.1
backports.zoneinfo |0.2.1
Django             |4.2.11
django-environ     |0.11.2
pip                |24.0
setuptools         |68.2.0
sqlparse           |0.5.0
typing_extensions  |4.11.0
tzdata             |2024.1
wheel              |0.41.2


*  ## Roadmap

- [x] 회원기능 (Accounts, app name: account)
    - [x] 회원가입, 로그인, 로그아웃
    - [x] 관리자계정
- [x] 프로필 페이지
  - [x] 찜 기능 (check_users:products/model/Post)
  - [x] 팔로우 기능 (followings:accounts/model/User)
  - [ ] 개인프로필 설정(이미지, 태그)
- [x] 게시글 CRUD (Products, app name: post)
    - [x] 게시글 기능(제목, 내용, 가격)
    - [x] 로그인 권한을 바탕으로 CRUD 구현
    - [x] 댓글 CRUD


-  TODO
- [ ] 이미지(media, Pillow)
    - [ ] 개인프로필
    - [ ] 게시글 이미지첨부
- [ ] 게시글 검색 및 정렬