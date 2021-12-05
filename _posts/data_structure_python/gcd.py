# 빼기: 횟수가 많아 비효율적
def gcd_sub(a, b):
    while not (a == 0 or b == 0):
        if a > b:
            a= a - b
        elif (a <= b):
            b = b - a
    return a + b

# 나누기: 효율적
def gcd_mod(a, b):
    while not (a == 0 or b == 0):
        if a > b:
            a = a % b
        elif (a <= b):
            b = b % a
    return a + b

# 재귀: 위와 동일
def gcd_rec(a, b):
    while not (a == 0 or b == 0):
        if a > b:
            return gcd_rec(a%b, b)
        elif a <= b:
            return gcd_rec(a, b%a)
    return a + b

def assert_equal(a: int, b: int):
    print(gcd_sub(a, b) == gcd_mod(a, b) == gcd_rec(a, b))
    print('value: ' + str(gcd_mod(a, b)))

assert_equal(144, 12)
