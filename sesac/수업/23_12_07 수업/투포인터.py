# 문자열 찾기
a = 'hello'
b = 'ell'

a_len = len(a)
b_len = len(b)

for i in range(a_len-b_len+1):
    cnt = 0
    for j in range(b_len):
        if a[i+j] == b[j]:
            cnt += 1
            continue
        else:
            break
    if cnt == b_len:
        print('찾았음. 인덱스:', i)
        break
else:
    print('못 찾음')