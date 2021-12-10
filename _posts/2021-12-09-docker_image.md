---
title: Docker Image
date: 2021-12-09 00:00:00 +0800
categories: [Docker]
tags: [docker, container, docker image, tool]
---
# Docker Image      
Docker를 사용하다 보면 이미지를 단순히 pull 받아 사용할 뿐만 아니라 직접 만들어야 하는 상황이 발생한다.       
이미지를 직접 만드는 방법을 기록해보고자 한다.     
          
### image 생성 방법     
**1) commit:** 현재 사용하고 있는 컨테이너를 이미지로 만들고 싶을 때 이용한다. 백업의 느낌이다.        
**2) Dockerfile + build:** Dockerfile에 만들고 싶은 이미지의 세부 사항을 기입하고, build 명령어를 통해 이미지를 생성한다. 이미지를 제대로 생성하고자 할 때 사용한다.       
    
### Case: git이 깔려 있는 ubuntu 이미지 생성     
__1) commit__      
1. docker pull ubuntu [우분투 이미지를 dockerhub에서 다운받는다.]       
2. docker run -it --name -myubuntu ubuntu bash [우분투 이미지로 myubuntu라는 이름의 컨테이너를 생성하고, 그 컨테이너를 배쉬에서 실행시킨다.]      
3. 컨테이너 상에 git 설치     
4. docker commit myubuntu hy:git-ubuntu [hy라는 디렉토리에 git-ubuntu라는 이름의 이미지를 생성한다.]       
      
__2) Dockerfile + build__      
1. dockerfile에 세부 사항 입력                
   FROM ubuntu:20.04        
   RUN sudo apt-get -y update
   RUN sudo apt-get -y install git      
2. docker build -t git-ubuntu [git-ubuntu라는 이름으로 이미지를 생성한다. *t는 tag의 이니셜로, 이미지 이름을 설정한다는 의미이다.]       
         
dockerfile 명령문      
* FROM: 새로운 이미지를 생성할 대 기반으로 사용할 base 이미지 지정한다.       
* WORKDIR: 쉘의 cd 명령문과 같이, 컨테이너 상에서 작업 디렉토리를 전환한다. 이후의 명령문은 해당 디렉토리를 기준으로 실행되게 된다.        
* RUN: 이미지 빌드 과정에서 필요한 커맨드를 실행한다. 보통 이미지 안에 특정 소프트웨어를 설치하기 위해 사용하는 명령문이다.     
* ENTRYPOINT: 이미지를 컨테이너로 띄울 때 항상 실행시킬 커맨드를 지정한다.      
* CMD: 이미지를 컨테이너로 띄울 때 실행시킬 커맨드나 ENTRYPOINT 명령문으로 지정된 커맨드에 넘길 파라미터를 지정한다.       
* EXPOSE: 리스닝 포트 및 프로토콜을 설정한다. 프로토콜을 명시하지 않으면 TCP가 디폴트로 사용된다.      
* COPY: 호스트 컴퓨터에 있는 디렉토리 혹은 파일을 Docker 이미지로 복사한다. 상대 경로를 사용할 때에는 WORKDIR 명령문으로 지정한 경로를 고려해야 한다.          
* ADD: 기본적으로 COPY와 기능이 동일하다. 다만 ADD는 일반 파일뿐만 아니라 압축 파일이나 네트워크 상의 파일도 사용할 수 있다. 특수 파일을 다루는 것이 아니라면 COPY 사용이 권장된다.       
* ENV: 환경 변수를 설정한다. ENV로 설정한 환경 변수는 이미지 빌드 시는 물론이고, 해당 컨테이너에서 돌아가는 애플리케이션에서도 접근할 수 있다.      
* ARG: docker build 커맨드로 이미지 빌드 시 --build-arg 옵션을 통해 넘길 수 있는 인자를 설정한다.       
     
### image push       
생성한 이미지를 push를 통해 dockerhub에 올릴 수 있다.     
1. docker login       
2. docker push 이미지이름[hy/git-ubuntu:1.0.1]       
        
__공부 자료__    
[생활코딩]생활코딩 Docker 입문수업: https://www.youtube.com/watch?v=Ps8HDIAyPD0    
[DaleSeo]Dockerfile에서 자주 쓰이는 명령어: https://www.daleseo.com/dockerfile/     
