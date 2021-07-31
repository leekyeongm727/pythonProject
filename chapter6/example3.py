import time

start_time = time.time()
n,k = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort() # a오름차순 정리
b.sort(reverse=True) # b내림차순 정리

for x in range(k):
    if a[x]<b[x]:
        a[x],b[x]=b[x],a[x]
    else:
        a[x],b[x]=a[x],b[x]

result=0
for x in range(n):
    result += a[x]
    x-=1
print(result)

end_time = time.time()
print("time:", end_time-start_time)