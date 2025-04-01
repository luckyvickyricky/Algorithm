from collections import Counter
def solution(id_list, report, k):
    report = list(set(report))
    receive = [x.split()[1] for x in report]
        
    cntl = Counter(receive)
    ban_list = []
    for i in cntl:
        if cntl[i]>=k:
            ban_list.append(i)
            
    answer = [0]*len(id_list)
    for i in report:
        a, b = i.split()
        if b in ban_list:
            idx = id_list.index(a)
            answer[idx]+=1
        
    
    return answer