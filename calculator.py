# 기본 계산기
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def divide(a, b):
    return a/b
  
# 추가 기능
def multiply(a, b):
    return a*b

# 무료 기능
def power(a, b):
    s = 1
    for i in range(b):
        s *= a
    return s
