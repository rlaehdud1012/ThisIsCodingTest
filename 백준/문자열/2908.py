# 두 수 A와 B 입력
a, b = map(str, input().split())
s_a = a[2] + a[1] + a[0]
s_b = b[2] + b[1] + b[0]

if int(s_a) >= int(s_b):
    print(s_a)
else:
    print(s_b)
