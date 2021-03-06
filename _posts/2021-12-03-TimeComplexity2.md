---
title: Time Complexity 2
date: 2021-12-03 12:00:00 +0800
categories: [Computer Science, Data Structure]
tags: [python, cs, 자료구조]
---
# 알고리즘의 시간 복잡도2(time complexity)

### 알고리즘의 실행 시간을 어떻게 구해야 할까?

__(1) 모든 입력에 대한 기본 연산 횟수의 평균__   
사실 알고리즘의 실행 시간은 input의 사이즈에 따라 달라진다.   
그렇다면 모든 입력에 대한 기본 연산 횟수를 더한 후 평균을 내는 것이 좋을 것 같아 보인다.   
하지만 고려해야 할 입력이 너무나도 많아 쉽지 않아 보인다.   
   
__(2) 가장 오래 걸리게 하는 입력에 대한 기본 연산 횟수__   
실행 시간이 가장 길어지는 입력(worst input)에 대한 기본 연산 횟수를 측정한다.   
이렇게 측정된 시간 복잡도를 worst time complexity라고 한다.   
모든 입력을 반영한 것이 아니기에 정확성의 측면에서 한계가 있다.   
하지만 측정이 용이하고, 어떤 입력이 오더라도 wtc보다 수행 시간이 길지 않다는 사실만큼은 보장할 수 있다.   
   
>보통 알고리즘 수행 시간은 (2)번 방식으로 측정한다.   
>즉, "알고리즘 수행 시간 == 최악의 입력에 대한 기본 연산 횟수"이다.     
>또한 보통 알고리즘 수행 시간은 n(input size)에 관한 식으로 표현된다.     
    
### 예시   
__1번__   
```
algorithm sum1(A, n):
    sum = 0   (1)
    for i = 0 to n-1 do
        if A[i] % 2 == 0:   (2)
            sum += A[i]   (3)
    return sum
```
위의 식에서 최악의 입력을 생각해보면,   
연산문 (3)이 모든 i에 대해 실행되는 경우이다.   
따라서 모든 i가 짝수인 경우가 worst input이다.   
이때의 기본 연산 횟수를 계산해보면,   
(1)에서 1회,   
(2)에서 '%(산술 연산)' 1회, '==(비교 연산)' 1회를 총 n번 반복하므로 2n회,   
(3)에서 '+(산술 연산)' 1회, '=(대입 연산)' 1회를 총 n번 반복하므로 2n회,   
이를 모두 더하면 총 4n + 1이다.   
__따라서 최악의 입력은 A의 요소가 모두 짝수일 경우이고, 이때의 시간 복잡도 T(n) = 4n + 1이다.__   
   
__2번__   
```
algorithm sum2(A, n):
    sum = 0
    for i = 0 to n-1 do
        for j = i to n-1 do
            sum += A[i] * A[j]
    return sum
```
__위의 알고리즘의 시간 복잡도를 n에 대한 식으로 나타내면?__   
   
~~3/2n(n-1) + 1~~   
   
   
### 다음 시간 - [Big-O](https://parkhanyoung.github.io/posts/Big-O/)    
>1번 알고리즘의 수행 시간은 n에 관한 식인 반면, 2번 알고리즘의 수행 시간은 n^2에 관한 식이다.   
>즉 1번 알고리즘은 수행 시간이 n에 비례하고, 2번은 수행 시간은 n^2에 비례한다.   
>1번에 비해 2번이, n의 크기에 훨씬 민감하게 반응한다.   
>다음 시간엔 이러한 시간 복잡도를 보다 간단하게 나타낼 수 있는 법에 대해 배울 것이다.   