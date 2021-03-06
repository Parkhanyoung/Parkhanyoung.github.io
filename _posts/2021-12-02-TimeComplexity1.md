---
title: Time Complexity 1
date: 2021-12-02 12:00:00 +0800
categories: [Computer Science, Data Structure]
tags: [python, cs, 자료구조]
---
# 알고리즘의 시간 복잡도 1(time complexity)
---
__알고리즘의 성능을 좌우하는 요소__   
1. 소프트웨어 및 하드웨어 환경에 따라 같은 알고리즘이 다른 성능을 발휘한다.
2. 입력값의 크기에 따라 상이한 성능을 보인다.
   
공부하는 과정에서는 위와 같은 요소를 배제한다.   
Virtual Machine + Pseudo Language + Pseudo Code를 상정하여 모든 알고리즘이 같은 환경에서 실행된다고 가정한다.   
   
### 공부하는 과정에서 상정하는 3가지 요소   
__(1) Virtual Machine(가상 컴퓨터)__   
가상 컴퓨터: Turing Machine, RAM(Random Access Machine)   
RAM == CPU + Memory + 기본 연산   
   
가상 컴퓨터의 기본 연산은 모두 같은 단위 시간이 걸린다고 가정한다.   
    
#### 기본 연산   
* 배정, 대입, 복사 연산: a = b
* 산술 연산: +, -, *, / [나머지, 버림, 반올림 등의 연산은 기본 연산에 포함되지 않지만, 이 수업 내에서는 기본 연산으로 가정]
* 비교 연산: >, >=, <, == ...
* 논리 연산: AND, OR, NOT
* 비트 연산: bit-AND, bit-OR, bit-NOT
   
__(2) Pseudo Language(가상 언어)__   
RAM 모델의 기본 연산을 표현할 수 있는 가상의 언어이다.   
배정, 산술, 비교, 논리, bit-논리, 반복문, 함수와 같은 기본 연산을 표현할 수 있는 언어이면 된다.   
   
__(3) Pseudo Code(가상 코드)__   
RAM 모델에서 돌아가는 코드이다.   
실제로 실행되어야 하는 코드가 아니라, 논리적인 설명이 가능한 형태이면 된다.   
   
   
### 다음 시간 - [시간 복잡도 2](https://parkhanyoung.github.io/posts/TimeComplexity2/)   
>기본 연산의 횟수가 늘어날수록 실행 시간이 늘어나는 것이고, 그 말인즉슨 성능이 안 좋아지는 것이다.   
>즉, 기본 연산의 횟수에 의해 알고리즘의 성능이 측정되는 것인데, 연산이 복잡해질수록 일일이 연산 횟수를 측정하는 것이 어려워진다.   
>그렇다면 알고리즘의 수행 시간은 어떻게 측정해야 할까?   