import sys 

n=int(sys.stdin.readline().rstrip())
number=list(map(int,sys.stdin.readline().split()))
plus,minus,multi,divide=map(int,sys.stdin.readline().split())

min_value=1000000001
max_value=-1000000001

def dfs(v,value):
    global plus,minus,multi,divide,min_value,max_value
    
    if v==n:
        min_value=min(min_value,value)
        max_value=max(max_value,value)
        return
    
    if plus>0:
        plus-=1
        dfs(v+1,value+number[v])
        plus+=1
    if minus>0:
        minus-=1
        dfs(v+1,value-number[v])
        minus+=1
    if multi>0:
        multi-=1
        dfs(v+1,value*number[v])
        multi+=1
    if divide>0:
        divide-=1
        dfs(v+1,int(value/number[v]))
        divide+=1
    
    
dfs(1,number[0])

print(max_value,min_value,sep="\n")