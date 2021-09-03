# 곱하기 혹은 더하기
# 왼->오 계산, +/x 두가지 연산을 이용하여 구할 수 있는 최대값
s = input()

result=0
for i in range(len(s)):
    x=int(s[i]) #정수로 변환
    if x<=1 or result<=1: #0 또는 1인 경우엔 더하기
        result += x
    else:
        result *= x

print(result)