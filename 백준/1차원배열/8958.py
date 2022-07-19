# 테스트 케이스의 개수
n = int(input())

# 테스트 케이스 입력
for i in range(n): # 각 테스트 케이스 출력위한 반복문

    case = input()
    score = 0                # 출력을 위한 값
    cnt = 0                  # 'O'가 연속일 때 증가하기 위한 값
    
    for j in case:
        
        if j == 'X':         # 'X'일 경우에 cnt 변수를 0으로, 그리고 건너뛰기
            cnt = 0
            continue
            
        cnt += 1             # 'O'일 경우에, cnt 변수를 1씩 증가, score 변수에 cnt 값 추가
        score += cnt
        
    print(score)