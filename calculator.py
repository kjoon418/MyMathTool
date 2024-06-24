# 기본 계산기
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

# 추가 기능
def divide_free(a, b):
    return a/b

# 무료 기능
def power(a, b):
    s = 1
    for i in range(b):
        s *= a
    return s

def double(a):
    return a*2
