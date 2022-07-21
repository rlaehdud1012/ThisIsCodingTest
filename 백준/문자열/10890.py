# 알파벳 소문자로 이루어진 단어 S 입력
s = input()
s_l = [i for i in s]

# 알파벳 리스트
alphabet = [i for i in 'abcdefghijklmnopqrstuvwxyz']

# 단어에 포함되어 있는 처음 등장하는 위치 출력
for alpha in alphabet:
    for index, s in enumerate(s_l):
        if alpha == s:
            print(index)
            break
        if index >= len(s_l) -1:
            print(-1)
        
    
        