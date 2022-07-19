# 테스트 케이스 개수 입력 N
n = int(input())

# 각 테스트 케이스 학생의 수(Students)와 점수(Scores) 입력

for i in range(n):
    info = list(map(int, input().split()))
    meanScore = sum(info[1:]) / info[0]
    meanStudents = len([i for i in info[1:] if i > meanScore])
    print("{:.3f}%".format(round(meanStudents / info[0] * 100, 3)))