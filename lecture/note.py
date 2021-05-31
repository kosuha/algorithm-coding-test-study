a = list(range(3, 10))

# enumerate
for index, value in enumerate(a):
    print(index, value)

# all
if all(x < 3 for x in a):
    print("a가 전부 조건에 맞을 경우 참")
else:
    print("하나라도 아니면 거짓")

# any
if any(x < 4 for x in a):
    print("a가 하나라도 조건에 맞을 경우 참")
else:
    print("하나도 안 맞으면 거짓")