def solution(survey, choices):
    habit = {
        'R' : 0,
        'T' : 0,
        'C' : 0,
        'F' : 0,
        'J' : 0,
        'M' : 0,
        'A' : 0,
        'N' : 0
    }
    for s, c in zip(survey, choices):
        # 4보다 크면 뒤쪽, 작으면 앞쪽
        if c>4:
            habit[s[1]] += c-4
        elif c<4:
            habit[s[0]] += abs(c-4)
        else:
            continue
    
            
    answer = ''
    if habit['R']<habit['T']:
        answer+="T"
    else:
        answer+="R"
    if habit['C']<habit['F']:
        answer+="F"
    else:
        answer+="C"
    if habit['J']<habit['M']:
        answer+="M"
    else:
        answer+="J"
    if habit['A']<habit['N']:
        answer+="N"
    else:
        answer+="A"
    
    return answer