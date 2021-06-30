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

# 사과나무(다이아몬드)
def f20(input):
    rows = input.split(" \n")
    N = len(rows)
    for i in range(N):
        rows[i] = list(map(int, rows[i].split(" ")))

    apples = 0
    for i in range(N):
        if i > N/2:
            r = N - i - 1
        else:
            r = i

        apples += sum(rows[i][int((N-1)/2) - r : int((N-1)/2) + r + 1])

    print(apples)
    return apples

# 곶감(모래시계)
def f21(input, orders):
    rows = input.split(" \n")
    N = len(rows)
    for i in range(N):
        rows[i] = list(map(int, rows[i].split(" ")))

    orders = orders.split(" \n")
    M = len(orders)
    for i in range(M):
        orders[i] = list(map(int, orders[i].split(" ")))
    
    for row in rows:
        print(row)

    for order in orders:
        move_time = order[2] % N
        if order[1] == 0:
            move_time = N - move_time

        rows[order[0] - 1] = rows[order[0] - 1][-1 * move_time:] + rows[order[0] - 1][:N - move_time]

    total = 0
    s = 0
    e = N
    reverse = False
    for row in rows:
        total += sum(row[s:e])

        if s + 1 == e:
            reverse = True

        if reverse:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print(total)
    return 0

# 봉우리
def f22(input):
    rows = input.split(" \n")
    N = len(rows)
    for i in range(N):
        rows[i] = list(map(int, rows[i].split(" ")))

    for i in range(N):
        rows[i] = [0] + rows[i] + [0]

    rows = [[0] * (N + 2)] + rows + [[0] * (N + 2)]

    count = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            center = rows[i][j]
            if center > rows[i - 1][j] and center > rows[i + 1][j] and center > rows[i][j + 1] and center > rows[i][j - 1]:
                count += 1

    print(count)
    return 0

input = '''53 57 18 34 9 11 6 43 17 70 6 28 49 48 7 53 44 8 26 64 9 32 62 17 46 28 67 94 53 90 43 78 24 22 73 57 90 41 79 31 72 96 48 58 26 55 14 1 51 39 
36 59 30 34 11 95 34 25 53 49 6 70 74 13 21 81 63 62 61 81 49 82 47 7 60 12 94 26 27 66 35 71 73 56 65 3 36 64 44 22 8 96 28 87 44 97 50 77 13 1 
34 20 43 4 39 89 5 62 63 6 70 96 20 93 93 11 69 62 85 29 13 3 9 99 49 4 83 59 85 47 10 35 40 85 34 73 55 54 71 64 19 46 52 31 66 85 13 97 52 11 
23 96 13 7 23 38 54 25 37 57 68 15 34 46 100 45 73 93 2 39 10 90 43 71 52 51 68 18 48 100 76 56 21 71 20 31 50 41 47 63 26 53 16 63 98 96 18 80 20 68 
91 36 35 61 30 80 99 64 59 21 2 26 22 42 31 24 14 98 18 89 19 6 84 69 44 2 37 27 86 69 51 70 35 28 53 11 66 14 100 10 7 45 12 57 57 60 50 61 75 53 
48 40 48 77 57 31 74 58 19 69 16 72 19 35 86 24 32 25 21 84 3 29 52 99 41 63 39 68 16 49 54 32 55 4 96 81 1 62 28 88 5 97 3 54 51 63 28 87 73 72 
52 47 72 93 34 50 81 95 6 2 52 88 76 62 51 39 48 21 82 82 67 3 82 34 33 87 91 23 52 74 63 66 3 31 80 43 64 91 85 16 19 39 19 45 29 27 77 19 40 50 
82 10 87 40 34 22 44 18 24 81 20 64 58 41 2 71 78 77 92 34 67 44 26 62 27 54 77 37 64 34 27 55 56 4 88 58 10 16 25 100 81 35 58 94 39 75 1 76 30 69 
68 18 38 42 95 29 95 46 15 21 76 22 55 33 73 79 37 42 45 88 87 93 38 15 67 92 49 66 99 97 77 85 45 71 99 22 78 1 24 17 81 38 70 38 50 88 48 87 76 99 
43 26 28 100 16 87 15 41 92 93 89 23 38 91 83 83 52 12 14 20 21 64 41 66 97 17 29 63 5 44 79 94 100 98 62 61 46 9 41 49 1 48 11 21 77 21 5 27 88 56 
32 98 6 81 4 41 5 13 28 79 80 67 91 83 41 56 26 61 40 79 55 18 34 11 61 96 3 41 13 42 32 14 44 87 15 29 82 28 98 25 3 59 90 34 28 13 17 36 12 56 
19 88 67 69 18 70 23 60 71 46 37 82 30 63 82 14 57 100 19 43 17 37 62 72 58 94 41 53 76 19 60 9 82 63 26 85 98 37 28 32 77 100 46 31 64 57 66 79 87 87 
98 61 25 81 64 89 56 60 52 66 95 3 66 93 73 94 84 68 56 32 34 9 65 31 16 62 38 37 68 59 73 12 40 50 79 73 26 59 69 74 51 1 9 5 13 83 85 40 60 14 
31 95 15 22 92 67 54 7 19 28 79 70 60 100 33 68 2 41 84 70 20 13 67 69 51 86 2 36 80 21 80 8 24 82 64 48 89 100 74 17 71 64 44 31 39 40 5 60 6 66 
22 17 17 90 96 35 79 60 21 75 9 25 70 94 29 61 96 2 1 90 22 5 50 67 31 43 74 19 16 33 71 74 84 36 9 44 5 23 83 53 14 69 25 8 95 39 40 21 45 41 
83 93 87 6 8 71 88 73 50 88 33 49 34 78 29 4 91 14 100 80 79 75 73 26 66 23 55 31 41 28 65 28 35 1 57 81 94 62 22 70 54 69 90 60 62 3 70 73 3 42 
19 10 41 20 81 93 11 52 54 24 78 31 97 36 37 34 56 45 48 75 22 81 22 45 25 43 47 55 75 98 30 31 39 78 79 63 3 59 84 80 64 52 29 67 33 41 46 17 11 39 
72 21 1 3 3 100 79 34 82 28 64 48 99 21 40 100 92 60 63 87 22 92 60 79 62 14 53 62 97 32 87 27 32 70 53 100 87 81 100 88 82 60 9 27 86 12 38 88 41 82 
33 82 40 34 91 26 75 38 57 28 2 100 21 100 19 33 98 47 13 38 31 90 59 73 37 46 75 40 84 40 17 19 73 19 62 88 5 68 62 18 64 2 86 42 15 66 90 6 6 56 
94 18 26 11 54 70 94 29 31 41 4 51 4 42 31 19 61 100 54 43 42 82 47 93 52 37 9 67 92 69 31 21 24 2 3 48 70 6 78 1 61 79 20 67 82 3 6 6 84 48 
94 8 68 41 98 84 12 36 49 60 69 82 87 31 74 64 55 20 67 15 42 34 54 54 29 60 60 38 83 11 59 78 16 77 47 57 29 28 63 89 13 96 57 53 100 61 60 49 74 8 
5 16 26 99 72 30 63 28 73 64 38 10 23 100 17 94 19 69 40 89 4 75 18 85 61 43 87 85 75 69 23 80 37 73 85 17 25 71 89 56 18 79 27 49 27 21 93 86 17 37 
46 70 19 5 52 91 72 58 51 55 94 97 4 59 78 38 1 8 69 74 13 91 85 100 97 49 99 85 12 42 3 1 89 47 100 29 3 39 47 87 14 28 98 7 83 98 1 75 4 71 
35 97 9 98 32 92 82 41 43 96 14 42 68 49 91 74 20 86 99 41 36 71 18 72 81 72 69 68 13 29 43 10 99 70 54 72 71 33 64 91 12 62 38 85 61 86 97 72 62 56 
99 68 21 96 24 58 53 33 2 2 10 98 26 38 85 15 96 27 12 21 84 43 69 19 62 67 96 98 38 12 19 79 73 81 74 100 48 67 98 25 30 87 20 91 40 75 57 62 19 39 
61 98 66 14 19 39 32 70 80 90 32 96 30 32 19 67 29 33 58 18 10 51 100 36 64 36 67 80 96 98 42 69 18 58 53 64 81 58 1 35 49 11 81 40 47 85 78 67 52 33 
9 40 31 49 98 52 93 78 65 54 26 78 90 9 73 43 79 88 19 44 84 61 100 63 78 97 30 43 89 16 66 46 7 36 48 18 78 29 83 71 55 4 77 28 55 66 20 47 26 27 
73 98 11 69 92 28 63 31 88 14 2 3 92 42 82 47 90 58 65 16 75 93 5 47 31 99 69 81 6 41 99 92 32 86 36 6 77 4 36 41 72 67 59 44 45 68 79 25 100 68 
55 55 68 30 38 70 11 43 28 77 12 49 22 72 91 6 25 42 4 41 45 72 78 36 81 10 65 20 98 25 30 82 43 14 58 24 32 6 22 48 4 39 9 75 71 94 94 88 8 37 
16 65 57 39 47 91 56 98 25 10 62 80 12 27 67 12 70 26 81 23 7 30 68 42 33 7 77 59 62 98 21 44 49 90 65 3 66 98 40 27 23 2 9 93 91 68 93 98 87 8 
34 100 26 73 97 51 49 13 90 43 58 62 6 71 71 11 9 91 63 23 92 74 54 72 65 45 86 99 30 8 89 21 95 54 83 57 67 54 43 13 12 61 94 42 69 49 43 36 85 44 
51 33 78 6 39 12 11 87 30 13 90 37 52 99 52 12 91 66 62 66 73 7 100 37 27 65 88 35 85 57 9 42 81 87 64 16 60 66 11 48 2 70 16 37 13 93 45 39 45 13 
33 56 83 11 29 68 19 23 13 44 15 50 48 4 53 87 19 19 96 91 21 95 54 95 62 17 67 35 5 10 13 40 2 51 16 26 29 26 85 7 93 81 11 71 92 22 75 24 51 88 
87 25 76 70 90 46 10 77 75 6 77 6 80 97 91 4 76 30 82 23 78 7 83 6 12 92 47 2 36 94 100 87 34 25 69 86 87 12 85 40 24 36 65 47 5 22 97 90 27 88 
90 9 68 14 77 38 54 69 42 81 3 57 81 71 32 96 48 69 100 82 79 55 94 70 89 96 28 29 84 42 30 45 7 47 34 80 65 21 66 71 56 78 21 37 7 49 5 56 41 47 
33 11 88 25 97 4 89 89 30 24 84 16 72 95 41 3 65 62 12 56 39 84 59 47 9 58 66 92 6 43 68 91 30 50 75 15 38 15 60 35 42 81 100 27 37 16 22 49 63 42 
18 99 58 9 69 20 71 13 46 57 14 40 1 14 84 21 46 9 48 29 47 54 100 39 9 79 34 99 97 39 75 41 55 97 69 99 95 34 51 20 71 63 37 14 95 68 31 39 3 18 
91 19 86 69 93 37 52 2 69 20 33 22 26 75 94 59 50 16 29 1 6 36 36 51 80 47 63 76 81 88 87 75 20 46 29 45 80 45 74 13 45 34 51 65 86 29 13 13 69 46 
51 72 71 82 7 17 38 6 1 6 64 52 77 7 22 13 16 22 69 34 94 59 87 83 91 37 2 49 90 46 24 83 61 76 58 8 50 84 39 35 61 99 79 42 55 26 73 43 6 79 
80 4 63 70 21 54 81 49 66 85 74 66 9 9 78 76 28 100 2 65 3 66 79 3 79 77 3 42 82 74 45 36 42 91 4 38 30 83 100 87 83 47 85 78 43 51 75 17 80 8 
39 95 47 43 10 73 87 66 43 17 15 25 99 22 98 27 74 80 63 58 49 7 68 17 78 38 11 89 76 10 62 50 36 35 46 26 99 38 75 54 65 3 39 64 21 5 1 12 5 100 
91 79 13 10 81 70 79 97 56 79 29 12 3 36 43 36 73 59 42 33 91 85 62 13 75 11 15 60 82 43 93 29 18 67 65 36 94 17 82 28 50 33 66 19 70 52 6 7 94 34 
55 71 32 3 97 15 45 30 40 72 49 82 6 51 8 16 32 100 24 68 52 26 25 7 34 2 79 9 82 79 4 92 6 68 69 49 72 36 28 37 42 97 58 26 83 16 54 79 93 87 
99 30 25 48 46 9 11 1 23 51 91 77 92 87 86 15 50 29 53 56 1 32 83 97 74 4 65 54 75 52 79 28 89 43 37 6 100 59 83 6 40 22 92 13 44 60 69 44 40 53 
49 53 34 27 16 79 8 74 96 57 87 84 75 92 48 79 95 67 72 65 31 38 81 34 83 58 3 32 49 97 78 23 68 20 26 50 13 89 48 30 92 78 99 33 21 23 71 10 12 91 
9 79 50 32 39 59 30 9 45 73 11 51 80 77 22 16 70 81 29 12 27 30 33 88 82 13 41 68 30 8 1 63 51 70 26 26 20 41 66 81 39 1 18 97 79 85 26 51 88 81 
10 7 92 64 42 52 36 51 47 87 46 73 11 23 34 56 29 100 75 52 31 19 80 51 64 24 46 85 33 29 95 56 18 11 63 55 9 58 22 86 2 77 14 42 97 2 55 38 48 11 
32 65 33 22 60 74 19 7 69 8 64 43 71 68 70 95 76 59 60 17 63 48 92 14 43 13 82 57 5 33 95 51 32 50 83 15 99 68 12 52 77 90 77 77 53 55 70 44 44 28 
24 34 7 40 19 73 51 55 57 100 72 3 98 91 26 76 62 14 46 16 23 75 12 95 100 6 44 75 41 45 90 49 68 32 34 86 8 43 4 33 87 33 37 66 9 40 10 16 90 54 
76 14 20 1 97 55 31 95 4 30 93 63 51 8 62 32 53 90 2 51 78 9 36 87 43 49 27 13 93 68 19 100 26 74 23 94 93 66 36 67 58 78 20 34 38 56 76 74 95 8
'''

f22(input)