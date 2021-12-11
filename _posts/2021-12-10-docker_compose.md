---
title: Docker Compose
date: 2021-12-10 00:00:00 +0800
categories: [Docker]
tags: [tool, docker, docker compose]
---         
# Docker Compose       
docker가 많은 편의를 제공하는 것은 사실이지만, run 명령어로 컨테이너를 실행할 때의 옵션의 개수가 너무 많아 복잡하다는 아쉬운 점이 있다. [볼륨, 포트 설정 등등]      
이를 개선하기 위해 docker compose가 등장했다.      
컨테이너 실행 시 필요한 옵션을 docker-compose.yml 파일에 미리 적어두어 자동으로 실행되게 할 수 있다.               
또한 각각의 컨테이너에 대한 설정 외에도, 컨테이너 간 실행 순서 및 의존성을 관리할 수 있다.         
한마디로, docker compose는 여러 개의 컨테이너로 구성된 애플리케이션을 관리하기 위한 오케스트레이션 도구이다.      
            
### docker-compose 사용법          
* docker-compose.yml 파일은 프로젝트 루트에 위치해야 한다.       
* docker-compose.yml 파일 내에 아래와 같은 항목을 명시하여 애플리케이션의 환경, 그리고 애플리케이션을 구성하고 있는 서비스를 구체적으로 정의한다.     
            
__version__     
docker-compose의 맨 위에 파일의 version을 명시한다.     
ex       
~~~
version: '3'          
~~~
         
__services__        
services 항목의 하위 항목으로 실행하고자 하는 컨테이너들을 정의한다.         
docker-compose에서는 컨테이너 대신 서비스라는 개념을 사용한다.       
ex       
~~~
  services:         
    db:         
     `!@#!!%$    
    frontend:        
      `!@#$%         
~~~
               
__volumes__      
기본적으로는 컨테이너 내에서의 데이터 변경 사항은 저장되지 않으며, 다른 컨테이너 간의 데이터 공유도 불가능하다.      
데이터를 컨테이너 내에서 관리하기 때문에 컨테이너 폐기 시 데이터도 같이 폐기되며 데이터가 컨테이너 별로 독립적으로 관리되기 때문이다.        
이때 docker volumes 항목을 이용하여 컨테이너 내의 디렉토리와 호스트의 디렉토리를 연결시킬 수 있다.          
디렉토리 지정 시 상대 경로로 지정할 수도 있다.       
ex     
~~~
db:       
  volumes:         
  - ./docker/data:/var/lib/postgresql/data         
  [./docker/data라는 호스트 내의 디렉토리를 컨테이너 내의 디렉토리인 /var/lib~~에 연결]       
~~~
    
__environment__           
컨테이너의 환경 변수를 설정한다.         
ex        
~~~
environment:        
  - POSTGRES_DB=sampledb        
  - POSTGRES_USER=sampleuser       
~~~
        
__build__       
docker build 명령어를 실행할 디렉토리 경로를 설정한다(context).       
또한 Dockerfile이 아닌 다른 이름의 파일로 빌드를 하거나, 빌드 인자를 넘겨야 하는 경우에는 하위 항목을 사용하여 구체적으로 설정해준다(dockerfile).       
ex       
~~~
build:       
  context: ./app        
  dockerfile: Dockerfile-dev      
~~~      
     
__ports__    
외부에 개방할 포트와 내부에서 열어줄 포트를 설정한다.       
ex     
~~~
ports:
  8080:8080
~~~
    

---
__공부 자료__          
[생활코딩]생활코딩 Docker 입문수업: https://www.youtube.com/watch?v=Ps8HDIAyPD0        
[44bits]도커 컴포즈를 활용하여 완벽한 개발 환경 구성하기: https://www.44bits.io/ko/post/almost-perfect-development-environment-with-docker-and-docker-compose         
[DaleSeo]Docker Compose 설정 방법: https://www.daleseo.com/docker-compose-file/          