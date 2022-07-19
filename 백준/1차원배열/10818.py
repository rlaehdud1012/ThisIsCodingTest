# N 입력받기
n = int(input())

# N개의 정수 입력받기
n_l = list(map(int, input().split()))

print(min(n_l), max(n_l))