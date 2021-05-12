import math

def solution(n):
    answer = ''
    
    num = get_ternary_reversed(n)

    while True:
        if num[0] == '0':
            num = '4' + get_ternary_reversed(int(num[1::-1], base = 3) - 1)

        answer = num[0] + answer

        if len(num) > 1:
            num = num[1:]
        else:
            break
    
    print(answer)
    return answer

def get_ternary_reversed(n):
    result = ''

    while n >= 1:
        n, rest = divmod(n, 3)
        result += str(rest)
    
    return result



solution(6)

# 1  1  1
# 2  2  2
# 3  4  10

# 4  11 11
# 5  12 12
# 6  14 20

# 7  21 21
# 8  22 22
# 9  24 100

# 10 41 101
# 11 42 102
# 12 44 110

# 13 111 111
# 14 112 112
# 15 114 120

#     121
#     122
#     124

#     141
#     142
# 21  144

#     211
#     212
# 24  214

#     221
#     222
#     224