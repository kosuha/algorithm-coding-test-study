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

def f23(input):
    rows = input.split(" \n")
    N = len(rows)
    for i in range(N):
        rows[i] = list(map(int, rows[i].split(" ")))

    print(rows)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for row in rows:
        if sorted(row) != numbers:
            print('NO')
            return 0

    for i in range(9):
        check_row = []
        for j in range(9):
            check_row.append(rows[i][j])
        
        if sorted(check_row) != numbers:
            print('NO')
            return 0

    
    for i in range(3):
        for j in range(3):
            check_square = []
            check_square += rows[i * 3][j * 3:j * 3 + 3]
            check_square += rows[i * 3 + 1][j * 3:j * 3 + 3]
            check_square += rows[i * 3 + 2][j * 3:j * 3 + 3]

            if sorted(check_square) != numbers:
                print('NO')
                return 0


    print('YES')
    return 0

input = '''
2 4 3 6 2 8 5 7 8 
4 7 2 1 3 9 4 6 9 
9 8 6 7 5 4 2 3 1 
3 9 1 5 4 2 7 8 6 
4 6 8 9 1 7 3 5 2 
7 2 5 8 6 3 9 1 4 
2 3 7 4 8 1 6 9 5 
6 1 9 2 7 5 8 4 3 
8 5 4 3 9 6 1 2 7
'''

f23(input)