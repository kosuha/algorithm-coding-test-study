import math

def solution(n):
    answer = ''

    while True:
        mok = math.floor(n / 3)
        
        remain = n % 3
        i += 1
        if remain == 0:
            r = 4
        else:
            r = remain

        answer = str(r) + answer
        n = mok

        if mok == 1 and remain == 0:
            break
        if mok == 0:
            break

    print(answer)

    return answer


solution(24)

# 3 9 27
# ^1 ^2 ^3/ 

#     21
#     22 
# 9  24

# 10 41
# 11 42
# 12 44 3*3 + 3

# 13 111 3*3*
# 14 112
#     114

#     121
#     122
#     124

#     141
#     142
# 21    144

#     211
#     212
# 24    214

#     221
#     222
#     224