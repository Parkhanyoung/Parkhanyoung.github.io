---
title: Docker Basic Commands
date: 2021-12-08 00:00:00 +0800
categories: [Docker]
tags: [docker, container, tool]
---

# Docker 기본 커맨드

### 도커 키워드 비유   
docker hub는 다양한 program을 다운 받는 app store에 비유할 수 있다.   
image는 설치되는 program에 비유할 수 있다.    
container는 program이 실행된 구체적인 형태인 process에 비유할 수 있다.    
    
docker hub에서 image를 받는 행위를 image를 pull한다고 하고, image를 실행시키는 행위를 image를 run한다고 한다.   
    
### docker pull   
기능: docker hub에서 image를 다운받는다.        
명령어: docker pull [options] ImageName[:Tag|@DIGEST]    
docker hub에서 원하는 image를 찾아 상세 페이지로 들어가면 각 image의 이름을 알 수 있다.    
docker browser를 통해서도 다운 받을 수 있다.     
'docker images'라는 명령어를 통해 현재까지 다운 받은 image 리스트를 확인할 수 있다.     
    
### docker run    
기능: image에 기반하여 container를 생성한다.   
명령어: docker run [options] ImageName [command] [arg...]           
ex. docker run --name webserver -p 8080:80 httpd     
[httpd image를 이용하여 webserver라는 이름으로 container를 만들고, 8080포트를 container의 80포트랑 연결시킨다.]    
docker run -i: i는 interactive의 약자이다. container와 상호적으로 주고 받겠다는 뜻으로, STDIN(표준입력)으로 container를 생성하겠다는 뜻이다.    
docker run -t: t는 
     
### docker ps    
기능: 생성된 container 정보를 조회한다.    
명령어: docker ps     
docker ps -a: 종료된 container까지 포함하여 조회한다.    
      
### docker stop     
기능: 실행중인 container를 중단시킨다.    
명령어: docker stop ContainerName    
    
### docker start    
기능: 종료했던 container를 다시 시작시킨다.     
[새로 container를 생성하는 것이 아니라 이전에 생성했다가 스탑시킨 container를 다시 실행시키는 것]    
명령어: docker start ContainerName     
     
docker start로 실행시킬 때는 터미널에 로그가 따로 출력되지 않기에 따로 명령어를 입력해야 한다.          
docker logs ContainerName: 해당 container의 로그 출력     
docker logs ContainerName: 해당 container의 로그 지속적 출력     
     
### docker rm    
기능: container를 삭제한다.     
명령어: docker rm [options] ContainerName [container...]     
단, 현재 실행 중인 container는 삭제할 수 없으므로 docker stop으로 중지시킨 후 삭제한다.     
혹은 '—force' 옵션를 이용한다.     
image 삭제의 경우에는 'docker rmi ImageName' 명령어를 사용한다.    
[혹은 image prune이라는 명령어를 이용한다.]     
     
### docker exec       
기능: container의 터미널을 사용한다.       
명령어: docker exec -it ContainerName /bin/sh[/bin/bash]     
    
### 호스트와 container의 파일 시스템 연결     
container의 효용은 필요할 때 손쉽게 만들고, 필요 없어지면 얼마든지 없앨 수 없다는 데에 있다.      
그런데 container를 삭제할 때마다 container의 소스코드가 날아가면 되겠는가?          
그래서는 안 되기 때문에 호스트와 container가 상호 연결될 필요가 있다.     
파일 수정은 호스트에서 하고, 실행 환경 관련해서는 container에 맡기는 게 이상적일 것이다.   
그것을 위한 명령어 예시: docker run -p 8888:80 -v ~/Desktop/htdocs:/usr/local/apache2/htdocs/ httpd    
['8888포트를 80포트로 매칭시키고, '~/Desktop/htdocs'과 '/usr/local/apache2/htdocs/'를 매칭시켜 httpd container를 만들어라'라는 뜻]     

---
__공부 자료__        
[생활코딩]생활코딩 Docker 입문수업: https://www.youtube.com/watch?v=Ps8HDIAyPD0       
[snowturtle93 github.io]Docker Run 옵션: https://snowturtle93.github.io/posts/Docker-Run-%EC%98%B5%EC%85%98/