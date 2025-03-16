import sys


N, M = map(int, input().split())

# (학급, 점수) 형태로 받고 점수 기준 정렬하기
arr = []
for i in range(N):
    sub_arr = list(map(int, input().split()))
    for ele in sub_arr:
        arr.append((i + 1, ele))

arr.sort(key=lambda x: x[1])

min_val = float("inf")

# 각 학급의 등장 횟수를 기록
freq = [0] * (N + 1)
distinct = 0  # 현재 윈도우에 포함된 학급 수
ans = float("inf")

left = 0
for right in range(len(arr)):
    class_num = arr[right][0]
    freq[class_num] += 1
    # 해당 학급이 처음 윈도우에 포함되었다면
    if freq[class_num] == 1:  
        distinct += 1

    while distinct == N:
        ans = min(ans, arr[right][1] - arr[left][1])
        left_class = arr[left][0]
        freq[left_class] -= 1
        # 해당 학급이 윈도우에서 빠졌다면
        if freq[left_class] == 0:  
            distinct -= 1
        left += 1

print(ans)


# s = 0
# e = 1

# # 투포인터
# while s < len(arr) - 1:
#     # 더 찾아도 답없으면 종료
#     if len(set([x[0] for x in arr[s:]])) < N:
#         break
#     set_A = set()
#     set_A.add(arr[s][0])
#     while e <= len(arr):
#         # print(arr[s:e])
#         # 중단 조건 : set
#         set_A.add(arr[e - 1][0])
#         if len(set_A) == N:
#             # if len(set([x[0] for x in arr[s:e]])) == N:
#             min_val = min(min_val, arr[e - 1][1] - arr[s][1])
#             # print(f"start={arr[s]},end={arr[e-1]}, min={min_val} ")
#             break
#         e += 1
#     s += 1
#     e = s + 1

# print(min_val)
