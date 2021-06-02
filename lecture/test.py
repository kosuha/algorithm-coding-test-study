### Section 1 ###

# 1부터 n까지 홀수 출력
def a(n):
    for i in range(1, n + 1):
        if i % 2 == 1:
            print(i)

# 1부터 n까지의 합 구하기
def b(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    print(result)

# n의 약수 출력하기
def c(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(n // i)

### Section 2 ###

# k번째 약수
def d(n, k):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    if k > len(divisors):
        return -1
    else:
        return divisors[k - 1]

print(d(6, 5))
