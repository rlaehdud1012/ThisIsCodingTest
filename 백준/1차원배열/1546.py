# 시험 본 과목의 개수 N 입력
n = int(input())

# 각 과목의 성적 입력
scores = list(map(int, input().split()))

# 새로운 평균 출력
max_v = max(scores)
mean_v = ( (sum(scores) / max_v) * 100 ) / n
print(mean_v)