def is_over(today, agree_day, month):
    t_y, t_m, t_d = today.split('.')
    a_y, a_m, a_d = agree_day.split('.')
    t_y, t_m, t_d = int(t_y), int(t_m), int(t_d)
    a_y, a_m, a_d = int(a_y), int(a_m), int(a_d)
    month = int(month)
    # # day
    # if a_d == 1:
    #     a_d = 28
    #     if month == 1:
    #         a_y-=1
    #         month = 12
    #     else:
    #         month-=1
    # else:
    #     a_d = a_d-1
    # month
    a_m+=month
    if a_m>12: 
        a_y+=(a_m//12)
        a_m%=12
        if a_m == 0:
            a_y-=1
            a_m=12
        
    # print(f"today : {t_y}.{t_m}.{t_d}")
    # print(f"agree_day+month : {a_y}.{a_m}.{a_d}")
    
    if t_y>a_y or (t_y==a_y and t_m>a_m) or (t_y==a_y and t_m==a_m and t_d>=a_d):
        return True
    
    return False

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