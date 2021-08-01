import time

start_time = time.time()
n = int(input())

def setting(data):
    return data[1]

array=[]

for x in range(n):
    name,score = input().split()
    array.append((name, int(score)))

result = sorted(array, key=setting)
for x in result:
    print(x[0],end=' ')

end_time = time.time()
print("time:", end_time-start_time)