# 숫자의 개수 N 입력
n = int(input())

# N개의 숫자의 합을 출력
number_l = str(input())

print(sum([int(i) for i in number_l]))