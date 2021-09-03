# 모험가 길드
n = int(input())
data = list(map(int,input().split())) #n명의 공포도 & n 이하의 정수
data.sort(reverse=True) #공포도 내림차순으로 정렬

max=data[0]
result=1

for i in range(n+1):
    if i>max:
        max += data[i-1]
        result += 1

print(result)