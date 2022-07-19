def make_hansu(x):
    hansu_cnt = 0
    for i in range(1, x+1):
        num_l = list(map(int, str(i)))
        if i < 100:
            hansu_cnt += 1
        else:
            if num_l[0] - num_l[1] == num_l[1] - num_l[2]:
                hansu_cnt += 1        
    return hansu_cnt

n = int(input())
print(make_hansu(n))