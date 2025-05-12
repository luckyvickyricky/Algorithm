def solution(diffs, times, limit):
    def search(level):
        time = times[0]
        for i in range(1, len(diffs)):
            if diffs[i] <= level:
                time+=times[i]
            else:
                n = diffs[i] - level
                time += (times[i] + times[i-1]) *n +times[i]
            if time > limit:
                return False
        return True
    
    l = 1
    r = max(diffs)
    answer = r
    
    while l <= r:
        mid = (l+r) // 2
        
        if search(mid):
            answer = mid
            r= mid-1
        else:
            l = mid+1
            
    return answer
    
    answer = 0
    
    return answer