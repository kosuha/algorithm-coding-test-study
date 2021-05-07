import pandas as pd

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]

def solution(record):
    answer = []
    messages = [
        '님이 들어왔습니다.',
        '님이 나갔습니다.'
    ]
    user_list = {}

    records = []
    for r in record:
        records.append(r.split(" "))
    
    for r in records:
        if r[0] == 'Enter' or r[0] == 'Change':
            user_list[r[1]] = r[2]

    for r in records:
        if r[0] == 'Enter':
            answer.append(user_list[r[1]] + messages[0])

        if r[0] == 'Leave':
            answer.append(user_list[r[1]] + messages[1])
    
    return answer

print(solution(record))