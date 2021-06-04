def solution(arr):
    result = []
    done = []
    for n in arr:
        if not n in done:
            c = arr.count(n)
            done.append(n)
            if c != 1:
                result.append(c)

    if len(result) == 0:
        result.append(-1)

    print(result)
    return result

arr = [3, 5, 7, 9, 1]

solution(arr)