# 9개의 서로 다른 자연수가 주어짐
n = 9
max_v = 0
max_index = 0

# 최댓값 찾기
for i in range(1, n+1):
    new_v = int(input())
    if max_v < new_v:
        max_v = new_v
        max_index = i
        
print(max_v)
print(max_index)