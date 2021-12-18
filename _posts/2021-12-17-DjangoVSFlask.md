---
title: PyCon - Django vs Flask
date: 2021-12-17 00:00:00 +0800
categories: [Web, Django]
tags: [pycon, django, flask, web framework]
---
# Django vs Flask
         
## 웹 프레임워크?     
**웹:** 인터넷 상 연결된 컴퓨터들 간에 정보를 공유할 수 있는 전세계적 정보 공간.    
**프레임워크:** 특정 종류의 소프트웨어를 개발할 때 같은 작업을 반복하지 않을 수 있도록, 필수적으로 거쳐야 하는 과정들을 우아하게 해결해 놓은 도구(클래스, 라이브러리)들의 모음, 혹은 그 구조.    
    
웹을 구현하기 위해서는 생각보다 많은 작업이 필요하다.         
HTTP 요청 처리, URL 파싱, 보안 관련 처리, DB 관련 작업 등등 셀 수 없이 많다.        
이러한 작업을 일일이 구현한다면 시간이 엄청나게 오래 걸릴 뿐만 아니라, 완성도도 심각하게 안 좋을 것이다.     
그리하여 사용자가 웹의 내용적인 측면에 집중하여 프로그래밍할 수 있도록 판을 깔아주는 것이 Django와 Flask 같은 웹 프레임워크이다.        
      
**Django:** 마감 시간이 있는 완벽주의자의 프레임워크    
**Flask:** 마감 시간이 없는 완벽주의자의 프레임워크     

## Django vs Flask 대응되는 요소
* Django ORM vs SQLAlchemy
* Form vs flask-wtf
* Template Engine vs Jinja2
* Admin page vs flask-admin
* south(migrate, makemigrations) vs alembic
* Middleware vs before_request, after_requrest
* manage.py vs flask-scripts
* manage.py test vs unittest or flask-test
* def view(request) vs flask.request      
      
## Django vs Flask 차이점
**1. 로그인, 회원가입:** 장고에는 기본 유저 모델 및 로그인 기능이 정형화되어 있지만, Flask에서는 구현하는 방법이 천차만별이다. 
**2. ManyToMany Field:** Django에는 ManyToMany Field가 있지만, Flask에서는 매핑해주는 모델을 따로 만들어주어야 한다.
**3. get_object_or_404, get_or_create:** Flask에는 없는 Django의 편리함 중 하나이다.
**4. jsonify, return 문자열:** Django에는 없는 Flask의 편리함 중 하나이다. Django에서는 json을 응답하기 위해서 json.dumps()를 통해 바이너리 형태로 만들어준 후, content_type을 명시해서 HttpResponse로 응답해야 했다[1.7 이후에 JsonResponse가 추가되긴 했음]. Flask에서는 'return jsonify(data)' 형태로 간편하게 응답한다. 또한 문자열을 반환하는 것도 가능하다.
**5. REST API:** 게시판과 같이 정형화된 작업을 할 때에는 Django가 유리하고, 커스텀을 많이 해야하는 작업일 경우에는 Flask가 유리하다. DRF는 커스텀이 까다롭기 때문이다. 
**6. 정형성:** Django는 프로젝트 구조가 보통 정형화되어 있는 반면, Flask는 프로젝트마다 구조가 많이 다르다. 
      
## 기타 유의점
1. Admin page는 Django의 큰 장점 중 하나로 꼽힌다. 그런데 관리자가 개발자가 아닌 경우, 혹은 관리자 페이지를 많이 수정해야 하는 경우에는 Django나 Flask나 코드양이 비슷하다. Admin page가 장점이 될 수 있는 건 커스텀이 많이 필요없을 때까지만이다.     
2. Django와 같은 풀스택 프레임워크를 나중에 하는 것이 좋다는 의견이 있다. 필요성을 느끼지 못한 채 사용하는 도구는 제대로 활용할 수 없기 때문이다.       
3. Flask가 가볍다는 것은 쉽다는 게 아니라, 프레임워크가 제공하는 틀이 작고 그만큼 자유도가 높다는 뜻이다. 직접 조립해야 하는 부분이 많으므로 입문자에게 적합하지 않을 수 있다.      
        
### 요약    
Django에서는 많은 고민거리(세션 저장 위치, ORM, REST, Migration 등)에 대해 일반적인 상황에서 가장 합리적인 방안을 미리 마련해두었다. 따라서 그 고민거리에 대해 직접 고민하기에는 경험과 지식이 부족하다면, Django가 제공하는 기존의 해결 방법들을 사용하고 익히며 웹 프로그래밍의 큰 구조를 파악해나가는 것이 좋을 수 있다.     
그에 반해 Flask는 사용자에게 높은 자유도를 주기에, 상황에 맞추어 스스로 더 나은 방법을 고민할 수 있는 사용자에게 적합하다고 볼 수 있다.   
이렇게 여러 도구들을 비교하는 과정은 개발자에게 필수적이다. 프로그래밍은 변화와 발전이 빠른 분야인 만큼 더더욱 필수적이다. 자신에게 맞는, 혹은 자신의 상황에 맞는 도구를 찾아가는 고민을 게을리해서는 안 된다.     
      
__공부 자료__       
[PyCon 김도현]Django vs Flask, 까봅시다!: https://www.youtube.com/watch?v=cX8n7pRA670     
[digrr 개인 블로그]언제 Django를, 언제 Flask를 사용해야 할까?: https://dingrr.com/blog/post/%EC%96%B8%EC%A0%9C-django%EB%A5%BC-%EC%96%B8%EC%A0%9C-flask%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%B4%EC%95%BC-%ED%95%A0%EA%B9%8C      