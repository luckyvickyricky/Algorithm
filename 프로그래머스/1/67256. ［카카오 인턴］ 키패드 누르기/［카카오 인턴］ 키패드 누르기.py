from collections import deque

def get_distance(a,b):
    key_map = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
    10: (3, 0), 11: (3, 1), 12: (3, 2)
    }
    x1, y1 = key_map[a]
    x2, y2 = key_map[b]
    return abs(x1 - x2) + abs(y1 - y2)

def solution(numbers, hand):
    # 처음에 왼손은 *, 오른손은 #에서 시작
    r_hist = deque([12])    
    l_hist = deque([10])
    answer = ''
    
    for n in numbers:
        if str(n) in "147":
            l_hist.append(n)
            answer+="L"
        elif str(n) in "369":
            r_hist.append(n)
            answer+="R"
        else:
            if n == 0:
                n = 11
            l_dis = get_distance(l_hist[-1], n)
            r_dis = get_distance(r_hist[-1], n)
            # print(f"input:{n} l_dis:{l_dis} r_dis:{r_dis}")
            
            # 거리같은 경우, 본인 hand
            if l_dis == r_dis:
                if hand == "right":
                    r_hist.append(n)
                    answer+="R"
                else:
                    l_hist.append(n)
                    answer+="L"
            # 거리가 다른 경우, 가까운 손
            elif l_dis > r_dis:
                r_hist.append(n)
                answer+="R"
            else:
                l_hist.append(n)
                answer+="L"
                
    return answer