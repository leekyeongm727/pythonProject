import time

n,m = map(int, input().split())
array=[]

for x in range(n):
    array.append(int(input()))

start_time = time.time()

array.sort()
d=[0]*1000
d[0]=0

for x in range(array[n-1]+1): #가장 작은 화폐보다 작은 값=>만들 수 없음 =1000 / 화폐 종류로 주어진 것=1, d에 각각 먼저 고정
    if x < array[0]:
        d[x]=1000
    if x in array:
        d[x]=1

for i in range(1,m+1):
    if d[i]==1000 or d[i]==1: #1000과 1로 저장되어진 d는 패스
        continue
    arr=[] #해당 화폐를 만들 수 있는 경우의 수를 저장하기 위한 빈 리스트
    for j in range(1,i+1): #i에 해당하는 화폐를 만들 수 있는 모든 경우의 수 계산
        if d[j]==1000:
            continue
        arr.append(d[j]+d[i-j])
    d[i]=min(arr) #모든 경우의 수 중 가장 작은 값

if d[m]==1000:
    print('-1')
else:
    print(d[m])


end_time=time.time()
print("time:", end_time-start_time)