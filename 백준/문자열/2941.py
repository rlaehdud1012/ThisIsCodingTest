cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 크로아티아 알파벳 입력
s = input()

for i in cro_alpha:
    s = s.replace(i, 'a')
    
print(len([i for i in s]))