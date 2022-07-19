### 방법1)
# 세 개의 자연수 A, B, C 입력
a = int(input())
b = int(input())
c = int(input())

# A X B X C 결과
result = str(a * b * c)

# 0~9 숫자 순서대로 출력
for i in range(10):
    print(len([a for a in result if a == str(i)]))
    
    

### 방법2)
from collections import Counter

# 세 개의 자연수 A, B, C 입력
a = int(input())
b = int(input())
c = int(input())

# A X B X C 결과
result = str(a * b * c)
Counter(result)['0']

for i in range(10):
    if str(i) not in Counter(result):
        print(0)
    else:
        print(Counter(result)[str(i)])    