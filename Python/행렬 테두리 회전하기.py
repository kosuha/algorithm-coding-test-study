queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]


def solution(rows, columns, queries):
    result = []
    nums = {}
    
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            nums[f'{i}, {j}'] = columns * (i - 1) + j

    
    for q in queries:
        coords = []

        # q[0],q[1] - q[0],q[3]
        for i in range(q[1], q[3] + 1):
            coords.append([q[0], i])
        # q[0],q[3] - q[2],q[3]
        for i in range(q[0], q[2] + 1):
            if not [i, q[3]] in coords:
                coords.append([i, q[3]])
        # q[2],q[3] - q[2],q[1]
        for i in range(q[3], q[1] - 1, -1):
            if not [q[2], i] in coords:
                coords.append([q[2], i])
        # q[2],q[1] - q[0],q[1]
        for i in range(q[2], q[0] - 1, -1):
            if not [i, q[1]] in coords:
                coords.append([i, q[1]])

        print(coords)
        
        values = []
        for c in coords:
            values.append(nums[f'{c[0]}, {c[1]}'])

        values.insert(0, values.pop())
        
        i = 0
        for c in coords:
            nums[f'{c[0]}, {c[1]}'] = values[i]
            i += 1
        values.sort()
        result.append(values[0])
        print(nums)

    return result

print(solution(6, 6, queries))