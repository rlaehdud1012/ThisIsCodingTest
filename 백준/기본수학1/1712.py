# A(고정비용), B(가변비용), C(1대의 노트북 가격)
a, b, c = map(int, input().split())

if (c-b) > 0:
    print( (a // (c-b)) +1)
else:
    print(-1)