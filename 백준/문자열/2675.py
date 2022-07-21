# 테스트 케이스의 개수 T 입력
t = int(input())

# 각 테스트 케이스 입력
for i in range(t):
    cnt, test = map(str, input().split())
    for j in test:
        print(j * int(cnt), end='')
    print()