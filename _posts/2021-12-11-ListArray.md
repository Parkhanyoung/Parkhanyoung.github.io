---
title: List Array
date: 2021-12-11 00:00:00 +0800
categories: [Computer Science, Data Structure]
tags: [data structure, python, list, array]
---     
배열과 리스트는 가장 기본적인 순차적(sequential) 자료구조이다.        
파이썬에서는 배열이 아닌 리스트를 이용한다.        
배열과 리스트의 차이점을 알아두자.         

1. 파이썬 리스트에는 정수 객체의 메모리 주소가 담긴다. 그에 비해 c언어 배열은 메모리에 정수(4byte)가 직접 담긴다.         
2. 파이썬 리스트는 append, pop, insert, index 등의 편의를 위한 메소드를 제공한다. 그에 비해 C의 배열에서는 사용자가 필요에 따라 함수를 만들어 사용해야 한다.           
3. 파이썬 리스트는 용량이 자동조절된다(dynamic array). 예를 들어 append를 실행할 때에는 추가적인 메모리공간이 필요하므로 용량이 자동으로 커지고, pop을 실행할 때에는 불필요한 공간이 생기므로 용량이 자동으로 작아진다(python이 대신 해줌). 그에 비해 C의 배열에서는 malloc 등의 함수를 이용하여 사용자가 직접 조정해야 한다.         
      
![ArrayList](/assets/img/post-img/list_array.png)
       
__공부 자료__         
[Chan-Su Shin 자료구조]순차적 자료구조 배열과 리스트: https://www.youtube.com/watch?v=Lqd8o7vL2Z8&list=PLsMufJgu5933ZkBCHS7bQTx0bncjwi4PK&index=6
