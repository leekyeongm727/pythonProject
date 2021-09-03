# 문자열 뒤집기
# 전부 0 또는 1로 뒤집기 -> 더 작은 경우 선택

s = input()

if s[0]=='0':
    result_0 = 0
    result_1 = 1
else:
    result_0 = 1
    result_1 = 0

# 전부 0으로 뒤집기
for x in range(1,len(s)):
    if s[x] == '0':
        continue
    else:
        if s[x] != s[x-1]:
            result_0 += 1

# 전부 1으로 뒤집기
for x in range(1,len(s)):
    if s[x] == '1':
        continue
    else:
        if s[x] != s[x-1]:
            result_1 += 1

result=min(result_0,result_1)
print(result)