# 싱가폴 여행카페

## 목표
- 여행카페를 Django로 CRUD & 인증 구현 및 배포

## 개발환경
- asgiref==3.7.2
- Django==4.2.3
- sqlparse==0.4.4
- typing_extensions==4.7.1

## 개발기간
- 2023.07.17 ~ 2023.07.20

## 배포 URL
- http://15.165.212.195/

## ERD 기획
![ERD](./architecture/django-project1.png)

- 처음 기획할 당시 2단계를 목표로 구현하여 Reply에 테이블에 대한 고려가 없었습니다. 구현하다보니 reply테이블을 추가구현하였으나 ERD상에서는 반영되지 않았습니다. Reply 테이블을 Comment테이블과 비슷하나, Post를 foreinkey로 참조하지 않았습니다. 

## 기능 기획
![기능](./architecture/service%20mindmap.png)
 
 - 처음 기획할 당시 위와 같이 기능을 정리해 보았습니다. 

## 2.x 단계 페이지 구현
- 메인페이지
![메인](./README-IMG/image-2.png)
- 회원가입
![회원가입](./README-IMG/image-3.png)
- 로그인
![로그인](./README-IMG/image-4.png)
- 게시글 작성
![글작성](./README-IMG/image-6.png)
- 게시글 목록
![글목록](./README-IMG/image-5.png)

- 게시글 상세보기 (오류: 해시태그 삭제가 안되는 문제가 발생하였으나 잡지못하고 넘어가는 한계)
![상세1](./README-IMG/image-7.png)
![상세2](./README-IMG/image-8.png)

- 게시글 검색: 해시태그 테이블을 구현하여, 해시태그별로 글을 검색할수있게 기능 구현(e.g 여름이라는 해시태그를 가진 글 필터)
![글검색](./README-IMG/image-9.png)
- 게시글 수정
![글수정](./README-IMG/image-10.png)
- 게시글 삭제(아래 글 삭제한 후 목록으로 리다이렉션)
![글삭제1](./README-IMG/image-11.png)
![글삭제2](./README-IMG/image-12.png)
- 코멘트 작성 & 삭제
![댓글작성 및 삭제](./README-IMG/image-14.png)
- 대댓글 작성 & 대댓글 삭제
![대댓글 작성 및 삭제](./README-IMG/image-15.png)
- static 파일 (css파일에 컬러 설정, 적용이 반영 되었습니다.)
![static1](./README-IMG/image-18.png)
![static2](./README-IMG/image-17.png)
![static3](./README-IMG/image-16.png)


## 프로젝트를 진행하면서 힘들었던 점
1. aws 로컬환경에서 실행 -> 오류, 아래와같이 수정했더니 드디어 실행이 되었습니다.
    - aws 방화벽 TCP포트 추가 80,8000,8080
    ![포트](./README-IMG/image.png)
    - settings.py 수정
    ![allowed host](./README-IMG/image-1.png)

2. uwsgi 및 nginx 환경설정파일 수정이 정말 어려웠습니다.
3. 대댓글 기능을 구현하는 중, 코멘트에 재귀적으로 구현하는것이 정말 어려웠습니다. 그리하여 Reply 테이블을 새로 만들어서 구현하는 방법으로 해결하였습니다.

## 마치며
장고를 처음 배우고, aws 서버에 띄우는 경험을 처음 경험해보았습니다. aws에 배포 페이지가 뜬 순간 희열이 엄청 났습니다. 이 경험을 바탕으로 더욱 정진할 수 있는 동기부여가 된 프로젝트이기에 기억에 많이 남을 것 같습니다.