def to_days(date_str):
    year, month, day = map(int, date_str.split('.'))
    return year * 12 * 28 + month * 28 + day

def is_over(today, agree_day, month):

    today_days = to_days(today)
    agree_days = to_days(agree_day)
    
    expiry_days = agree_days + int(month) * 28 - 1

    return today_days > expiry_days


def solution(today, terms, privacies):
    
    
    # term to dict
    term = {}
    for i in terms:
        n, m = i.split(" ")
        term[n] = m
    
    answer = []
    # pricacies check
    for idx, i in enumerate(privacies):
        date, n = i.split(' ')
        if is_over(today, date, term[n]):
            answer.append(idx+1)
    return answer
    
