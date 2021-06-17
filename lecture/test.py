### Section 1 ###

# 1부터 n까지 홀수 출력
def f1(n):
    for i in range(1, n + 1):
        if i % 2 == 1:
            print(i)

# 1부터 n까지의 합 구하기
def f2(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    print(result)

# n의 약수 출력하기
def f3(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(n // i)

### Section 2 ###

# k번째 약수
def f4(n, k):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)

    if k > len(divisors):
        return -1
    else:
        return divisors[k - 1]

# k번째 수
def f5(n, s, e, k):
    l = n[s - 1 : e]
    l.sort()
    print(l)
    return l[k - 1]

# k번째 큰 수
def f6(n, k):
    l = list(map(int, n.split(" ")))
    print(l)
    sums = [] # sums = set()
    for i in range(0, len(l) - 2):
        for ii in range(i + 1, len(l) - 1):
            for iii in range(ii + 1, len(l)):
                sums.append(l[i] + l[ii] + l[iii]) # sums.add(l[i] + l[ii] + l[iii])
    
    sums = list(set(sums)) # sums를 처음부터 set으로 선언해도 된다.
    sums.sort()

    return sums[-k]

# 대표값
def f7(arr_str):
    arr = list(map(int, arr_str.split(" ")))
    avg = int((sum(arr) / len(arr)) + 0.5)
    closest = float("inf")
    for i, n in enumerate(arr):
        close = abs(n - avg)
        if close < closest:
            closest = close
            index = i
            num = n
        elif close == closest:
            if num < n:
                index = i
                num = n

    return avg, index + 1

# 정다면체
def f8(N, M):
    arr = []
    for n in range(1, N + 1):
        for m in range(1, M + 1):
            arr.append(n + m)

    max_nm_count = 0
    for a in arr:
        c = arr.count(a)
        if c > max_nm_count:
            max_nm_count = c
            max_nm = [a]
        elif c == max_nm_count:
            if not a in max_nm:
                max_nm.append(a)

    return max_nm

# 자릿수의 합
def f9(input):
    arr = list(map(int, input.split(" ")))

    def digit_sum(x):
        str_x = str(x)
        sum = 0
        for j in str_x:
            sum += int(j)

        return sum

    maximum = 0
    maximum_num = 0

    for i in arr:
        sum = digit_sum(i)

        if maximum < sum:
            maximum = sum
            maximum_num = i

    return maximum_num

# 소수의 개수
def f10(n):
    result = 0
    num_list = [0] * (n + 1)
    
    for i in range(2, n + 1):
        if num_list[i] == 0:
            result += 1
            for j in range(i, n + 1, i):
                num_list[j] = 1

    return result

# 뒤집은 소수
def f11(input):
    def reverse(x):
        x_list = list(x)
        x_list.reverse()

        return int("".join(x_list))

    def isPrime(x):
        for i in range(1, x):
            if x % i == 0 and i != 1:
                return False
        
        return True

    arr = input.split(" ")
    
    result = []
    for n in arr:
        reversed_n = reverse(n)
        if isPrime(reversed_n):
            result.append(str(reversed_n))

    return " ".join(result)

# 주사위 게임
def f12(input):
    input = input.split(' \n')
    for i in range(len(input)):
        input[i] = list(map(int, input[i].split(' ')))

    print(input)

    max_money = 0

    for i in input:
        if i.count(i[0]) == 3:
            money = 10000 + i[0] * 1000
        elif i.count(i[0]) == 2:
            money = 1000 + i[0] * 100
        elif i.count(i[1]) == 2:
            money = 1000 + i[1] * 100
        elif i.count(i[2]) == 2:
            money = 1000 + i[2] * 100
        else:
            money = max(i) * 100
        
        if money > max_money:
            max_money = money

    return max_money

# 점수 계산
def f13(input):
    input = list(map(int, input.split(" ")))
    
    combo = 0
    score = 0

    for i in input:
        if i == 1:
            combo += 1
            score += combo
        else:
            combo = 0

    return score
    
### Section 3 ###

# 회문 문자열 검사
def f14(input):
    input = input.split("\n")
    
    # for i in input:
    #     front = list(i[:len(i)//2])
    #     front.reverse()
    #     front = "".join(front)
        
    #     back = i[len(i)//2 * -1:]
    #     if back.lower() == front.lower():
    #         print('YES')
    #     else:
    #         print('NO')

    for i in input:
        i = i.lower()
        if i == i[::-1]:
            print('YES')
        else:
            print('NO')
