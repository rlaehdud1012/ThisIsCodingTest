# 높이가 V미터인 나무 막대
# 낮에 A미터 올라갈 수 있음
# 밤에자는 동안 B미터 내려감
# but, 정상에 올라간 후에는 내려가지 x
# 달팽이가 나무 막대를 모두 올라가려면 며칠이 걸리는지?

# A(낮), B(밤), V(최종)
a, b, v = map(int, input().split())

if v <= a:
    print(1)
else:
    if (v-a)%(a-b) != 0:
        print( ((v-a)//(a-b)) + 2)
    else:
        print( ((v-a)//(a-b)) + 1)