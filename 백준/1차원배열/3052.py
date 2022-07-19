# 10개의 서로 다른 숫자를 42로 나눈 나머지로 입력
result = [] 

for i in range(10):
    new_v = int(input())
    result.append(new_v%42)
    
# 서로 다른 나머지 개수 출력
print(len(set(result))) # 중복값을 제거하기 위해 set()을 사용