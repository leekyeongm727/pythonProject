import time
start_time= time.time()

n = int(input()) # 정수 n (시각)입력받기

result = 0
for i in range(n+1): #시
    for j in range(60): #분
        for k in range(60): #초
            n_time = str(i)+str(j)+str(k)
            if '3' in n_time:
                result+=1
print(result)

end_time = time.time()
print("time:", end_time-start_time)
