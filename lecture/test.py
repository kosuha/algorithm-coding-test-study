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

# 숫자만 추출
def f15(input):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    input = list(input)

    num = ''
    for i in input:
        if i in numbers: # i.isdecimal() 0~9 까지의 숫자를 찾는 함수
            num += i

    num = int(num)

    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)

    print(num)
    print(len(divisors))

# 카드 역배치
def f16(input):
    input = input.split("\n")
    for i in range(len(input)):
        input[i] = list(map(int, input[i].split(" ")))

    cards = list(range(1, 21))
    # cards = []
    # for i in range(1, 21):
    #     cards.append(i)

    for i in input:
        target = cards[i[0]-1:i[1]]
        cards[i[0]-1:i[1]] = reversed(target)

    return cards

# 두 리스트 합치기
def f17(a, b):
    a = list(map(int, a.split(' ')))
    b = list(map(int, b.split(' ')))
    # result = a + b
    # result.sort()

    result = []

    a_index = 0
    b_index = 0
    for _ in range(len(a) + len(b)):
        if a_index == len(a):
            result.append(b[b_index])
            b_index += 1
        elif b_index == len(b):
            result.append(a[a_index])
            a_index += 1
        elif a[a_index] < b[b_index]:
            result.append(a[a_index])
            a_index += 1
        else:
            result.append(b[b_index])
            b_index += 1

    return result

# 수들의 합
def f18(M, input):
    numbers = list(map(int, input.split(' ')))

    # 시간 초과
    # count = 0
    # for i in range(len(numbers)):
    #     for j in range(i, len(numbers)):
    #         num_sum = sum(numbers[i:j+1])
    #         if num_sum == M:
    #             count += 1
    #             break
    #         if num_sum > M:
    #             break

    count = 0
    
    i = 0
    j = 0

    while i < len(numbers):
        if j < len(numbers):
            num_sum = sum(numbers[i:j+1])
            if num_sum == M:
                count += 1
                i += 1
                j = i
            elif num_sum > M:
                i += 1
                j = i
            else:
                j += 1
        else:
            i += 1

    return count

# 격자판 최대합
def f19(input):
    rows = input.split(" \n")

    for i in range(len(rows)):
        rows[i] = list(map(int, rows[i].split(" ")))
    
    maximum = 0
    for row in rows:
        row_sum = sum(row)
        if row_sum > maximum:
            maximum = row_sum
    
    x_sum = 0
    y_sum = 0
    for i in range(len(rows)):
        col_sum = 0
        
        for row in rows:
            col_sum += row[i]

        if col_sum > maximum:
            maximum = col_sum

        x_sum += rows[i][i]
        y_sum += rows[i][len(rows) - 1 - i]
    
    if x_sum > maximum:
        maximum = x_sum
    
    if y_sum > maximum:
        maximum = y_sum

    print(maximum)
    return maximum

input = '''21 96 57 80 25 42 47 88 54 84 76 9 24 65 42 11 2 5 94 77 98 5 93 12 98 6 52 40 42 32 89 18 82 78 24 43 50 84 7 21 79 54 94 32 7 99 98 98 35 88 
96 57 73 30 52 40 61 89 14 24 12 31 24 73 19 20 78 54 72 3 55 42 26 24 61 15 86 4 47 15 38 54 60 84 25 51 82 32 66 77 88 34 66 91 25 71 68 76 47 85 
71 93 63 87 80 40 9 21 80 6 97 63 64 23 19 28 14 57 17 77 70 30 63 5 22 50 44 84 42 64 30 31 16 31 58 34 35 5 9 92 5 19 46 18 51 79 37 42 92 46 
79 38 72 36 59 30 62 90 85 86 64 39 97 12 74 78 89 64 66 26 34 1 74 65 73 59 10 11 54 77 40 3 73 88 53 20 68 93 62 13 7 32 70 48 50 5 74 40 88 72 
86 77 28 11 90 54 77 42 1 33 41 70 65 29 27 39 99 32 85 65 88 2 19 48 41 13 66 10 2 43 43 87 29 93 71 7 21 77 15 33 61 94 8 20 71 70 53 74 16 29 
76 14 74 53 21 98 36 45 88 18 12 25 26 84 34 78 11 32 96 38 27 34 69 79 1 45 23 92 51 54 16 96 39 93 79 82 61 59 91 96 66 14 15 76 96 41 54 100 68 55 
38 25 72 53 85 66 69 89 80 42 8 78 89 83 47 50 24 49 42 79 22 10 82 1 84 99 35 78 84 59 97 31 31 78 32 11 14 37 32 53 98 12 61 55 5 76 39 52 56 34 
90 9 54 67 58 76 22 13 5 93 100 91 91 45 23 81 5 99 3 3 77 97 57 81 38 32 12 89 61 96 19 65 79 82 26 79 16 94 25 88 27 83 54 92 46 33 87 2 44 18 
80 7 66 36 2 11 83 98 100 4 59 97 53 50 6 33 19 23 84 100 18 43 5 27 47 94 26 94 26 93 57 72 50 95 57 11 40 41 96 17 75 36 15 32 91 49 87 39 95 9 
92 94 52 42 66 38 86 94 99 13 72 86 36 44 28 42 83 17 36 31 60 24 52 97 51 33 28 2 26 52 60 10 39 3 43 1 87 11 91 54 4 69 82 66 25 55 10 20 12 43 
85 21 81 96 24 99 87 55 52 66 42 27 30 3 96 44 67 52 33 40 31 3 14 63 43 59 23 32 68 5 16 69 11 31 17 52 62 86 85 78 48 79 81 1 67 26 100 56 93 44 
22 97 81 66 9 86 72 83 51 12 87 69 34 94 98 2 13 17 82 2 40 75 95 31 1 9 77 85 95 4 20 67 58 95 97 38 1 23 75 64 45 71 30 84 11 46 59 52 64 22 
44 87 51 6 1 88 19 99 80 82 93 75 76 38 99 54 12 74 74 14 94 80 65 60 2 18 27 10 1 18 56 8 57 49 19 90 67 72 2 61 70 23 9 18 82 81 88 65 37 100 
83 22 93 25 55 35 90 43 66 58 92 85 27 22 36 96 84 4 24 49 8 53 89 43 28 32 21 73 56 65 96 39 50 67 66 41 78 30 22 27 48 57 65 19 98 17 10 100 53 80 
96 37 39 11 88 9 7 46 69 72 52 25 22 10 69 30 3 55 20 82 74 3 97 60 11 38 81 25 85 98 72 9 4 3 60 80 68 55 68 12 35 20 48 30 30 71 69 47 87 70 
51 5 99 37 72 83 82 4 72 77 16 60 55 39 95 27 51 8 100 80 39 1 50 71 31 35 8 5 49 78 63 44 28 87 28 94 34 93 27 35 87 86 28 23 87 75 45 73 12 18 
72 48 86 82 78 31 79 69 92 32 15 5 6 16 62 20 37 7 51 18 21 57 61 99 99 88 88 81 90 20 95 42 16 23 43 42 44 55 22 4 63 36 1 71 16 6 83 7 47 38 
59 43 4 52 19 77 80 22 82 8 99 31 75 54 9 1 80 30 63 79 41 51 80 1 20 6 89 50 73 88 89 81 62 12 41 11 1 15 3 56 97 1 63 15 45 95 38 11 3 14 
83 87 4 27 80 7 48 34 18 100 69 48 7 99 35 88 91 46 71 86 8 24 28 27 71 65 17 56 36 79 24 57 81 14 3 91 42 71 69 1 54 57 95 43 90 83 91 28 78 81 
77 38 84 89 44 79 74 57 59 95 14 98 21 75 55 78 10 44 26 71 99 44 78 35 91 36 69 95 78 47 18 92 18 54 31 47 13 73 48 83 55 12 60 92 12 81 40 10 20 25 
4 20 61 90 64 35 89 100 92 58 48 82 56 35 88 31 55 25 75 12 33 48 76 84 74 22 83 39 93 59 82 15 57 31 12 24 18 6 36 78 11 28 53 97 99 14 89 68 46 53 
74 96 66 6 84 27 69 74 56 40 36 87 32 70 48 10 12 57 4 74 33 91 31 61 52 7 80 53 18 42 71 90 21 78 6 98 89 60 68 6 24 97 16 7 22 85 45 71 61 19 
48 20 72 30 27 13 7 56 97 89 22 100 7 60 65 70 45 9 56 84 71 68 82 17 77 47 60 28 69 84 91 34 72 5 57 33 60 4 12 13 41 40 3 67 76 24 59 7 36 74 
69 34 59 86 96 61 92 52 73 13 11 95 5 51 60 40 52 69 28 55 36 2 61 39 79 6 12 68 56 82 90 44 67 23 22 7 100 17 92 12 42 85 47 39 13 74 86 16 4 24 
82 80 83 70 7 7 59 54 95 49 51 79 51 89 75 34 31 19 67 60 5 4 67 39 25 56 21 98 92 75 46 18 43 32 24 90 54 74 3 91 48 55 3 37 87 88 70 28 31 69 
37 90 88 85 68 40 78 18 10 8 78 8 2 14 49 95 36 58 38 90 23 68 71 7 11 20 63 41 14 5 48 75 90 1 24 62 17 59 77 24 63 83 70 87 76 17 47 50 68 93 
24 17 19 78 12 55 8 53 7 59 59 4 85 84 38 6 25 54 41 78 43 12 34 88 62 32 96 2 29 43 98 39 70 37 10 20 28 53 34 80 69 76 43 74 59 76 100 80 100 35 
54 49 71 17 9 14 69 83 9 22 68 24 14 65 67 77 69 71 22 83 61 72 35 67 20 38 61 31 61 84 16 24 86 34 37 72 17 78 40 24 81 37 11 68 6 31 60 49 88 10 
42 63 32 54 80 29 36 89 95 62 81 41 69 21 90 34 93 7 50 52 45 91 66 78 18 54 96 16 63 45 47 26 12 72 97 45 77 100 85 98 45 43 20 93 84 46 38 60 40 55 
76 99 58 68 1 86 61 60 82 97 47 9 10 83 37 26 70 54 24 9 84 42 4 51 38 44 47 31 21 25 17 44 95 72 75 55 82 40 57 93 62 1 13 97 28 48 1 36 4 13 
51 96 100 72 79 30 38 52 41 92 53 56 49 39 78 82 55 1 52 29 34 29 1 85 88 49 75 2 26 48 23 77 14 17 59 13 18 85 22 34 39 93 64 47 30 66 66 30 82 68 
45 48 30 40 6 92 96 21 73 28 86 41 86 26 95 13 67 97 86 22 28 97 79 82 71 6 74 87 39 43 40 5 11 34 63 66 51 27 53 85 35 83 64 55 23 34 76 34 53 63 
54 83 33 70 92 87 46 10 37 24 9 70 6 73 91 62 64 79 46 82 40 61 56 34 53 2 32 58 65 54 33 92 74 2 48 44 74 20 12 79 49 7 60 51 51 18 41 49 38 83 
72 72 32 86 90 22 27 86 82 89 92 23 75 71 75 17 91 97 78 42 15 40 24 90 11 17 7 98 72 87 3 46 13 74 29 42 71 58 68 84 45 64 59 11 98 61 64 31 12 65 
87 27 17 94 17 63 56 88 35 24 50 7 57 36 21 51 64 98 24 99 8 66 29 54 90 33 80 97 29 76 32 9 13 69 35 80 97 81 85 78 57 51 25 82 8 22 87 60 60 71 
25 5 18 69 45 13 3 89 11 24 99 87 43 13 61 6 5 83 43 32 95 88 92 57 2 91 43 70 37 44 37 91 6 79 50 66 43 25 80 26 8 90 48 30 41 16 66 64 18 90 
11 68 86 13 49 29 5 87 58 77 33 44 12 72 15 30 32 23 5 27 96 10 3 18 99 4 22 87 56 13 16 66 6 9 25 3 70 71 42 65 29 76 8 52 92 13 87 41 9 78 
52 83 92 52 51 73 49 37 53 13 88 7 61 47 70 71 21 98 90 39 12 26 45 93 98 19 49 22 79 37 64 61 75 44 63 80 58 62 40 25 71 75 81 49 38 76 34 70 83 63 
38 33 97 14 68 62 42 54 16 62 99 49 29 74 36 55 37 6 82 62 95 65 52 76 47 59 47 74 63 90 53 22 5 41 35 8 13 74 82 56 20 43 79 50 13 16 97 83 2 23 
72 92 78 83 72 45 63 37 76 100 75 11 47 54 43 95 79 100 65 89 28 82 17 56 31 52 2 14 92 89 43 5 60 81 34 4 43 66 63 99 69 51 61 14 19 63 100 80 40 56 
58 66 97 11 55 77 90 74 63 66 23 85 71 77 98 97 86 88 16 50 46 45 53 2 25 9 55 43 85 26 48 77 3 31 5 84 47 62 46 77 69 35 30 46 58 11 57 47 67 92 
77 62 69 55 9 2 84 77 81 12 1 82 17 78 57 7 76 92 100 83 5 96 46 81 23 69 5 64 30 79 87 6 48 25 54 61 5 71 97 27 55 78 80 77 85 8 87 50 97 24 
83 97 96 40 25 64 80 41 75 6 29 50 72 84 21 88 16 75 97 4 36 33 77 10 15 57 70 30 5 80 66 56 54 70 66 24 83 8 19 6 24 59 54 24 90 48 26 22 99 58 
57 5 54 73 13 95 61 16 80 42 67 85 77 19 43 91 17 5 42 5 90 34 73 21 21 4 83 84 62 24 40 52 80 83 42 86 2 82 34 32 81 21 78 18 31 74 66 61 67 78 
5 11 82 51 1 82 2 3 81 79 96 77 74 18 79 90 8 43 47 43 11 63 84 46 81 97 99 32 1 62 25 84 81 83 86 73 48 5 20 5 83 49 1 62 93 33 54 50 37 86 
61 5 99 84 56 41 37 39 87 2 94 96 83 99 96 7 32 41 19 74 20 69 70 77 85 11 22 83 25 93 23 50 56 89 30 19 86 36 80 61 37 79 81 9 21 42 17 4 82 86 
45 52 34 63 1 81 92 47 76 46 100 94 9 71 48 70 32 40 14 32 60 77 30 16 92 35 7 74 24 95 73 98 50 21 10 92 12 8 70 23 35 73 2 67 12 85 56 49 98 34 
67 76 69 68 82 57 53 16 24 94 42 94 41 86 90 12 20 40 19 70 34 74 40 3 81 28 30 60 38 86 11 7 91 18 41 83 77 37 88 18 81 75 6 55 26 24 14 1 87 26 
15 15 9 33 58 22 99 11 38 28 16 92 52 79 88 82 30 65 39 48 75 84 34 100 64 25 40 4 65 16 52 47 71 88 15 20 53 33 77 45 89 89 87 43 92 84 75 37 60 57 
91 40 60 6 31 58 9 19 62 10 16 66 15 6 36 99 48 78 49 20 87 76 13 8 50 100 71 39 92 55 1 5 62 50 50 60 4 45 44 19 9 85 66 77 88 80 37 89 36 75'''

f19(input)