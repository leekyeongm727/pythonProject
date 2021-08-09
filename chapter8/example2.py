import time

n=int(input())
array=list(map(int, input().split()))

start_time = time.time()

d=[0]*1000
d[1]=array[0] #첫번째 저장
d[2]=max(array[0],array[1]) # 첫번째와 두번째 중 더 큰 수 선택해서 저장

#해당 칸 포함 저장할 경우, 바로 앞칸 선택 불가능
for i in range(3,n+1):
    d[i]=max(d[i-1],d[i-2]+array[i-1])

print(d[n])

end_time=time.time()
print("time:", end_time-start_time)