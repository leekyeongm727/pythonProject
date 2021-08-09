import time
n = int(input())
start_time = time.time()

d=[0]*1000

for x in range(2,n+1): #5,3,2로 각각 나누었을 때와 1을 뺀 경우 중 연산횟수가 더 작은 값 선택=> +1
    if x%5==0:
        d[x]=min(d[x//5],d[x-1])+1
    elif x%3==0:
        d[x]=min(d[x//3],d[x-1])+1
    elif x%2==0:
        d[x]=min(d[x//2],d[x-1])+1
    else:
        d[x]=d[x-1]+1

print(d[n])

end_time=time.time()
print("time:", end_time-start_time)