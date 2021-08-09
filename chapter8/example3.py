import time
n = int(input())
start_time = time.time()

d=[0]*1000

d[1]=1
d[2]=3
if n>=3:
    for x in range(3,n+1):
        if x%2 == 0:
            d[x]=(d[x-2]*3)%796796
        else:
            d[x]=(d[x-1]*2-1)%796796

print(d[n])
end_time=time.time()
print("time:", end_time-start_time)