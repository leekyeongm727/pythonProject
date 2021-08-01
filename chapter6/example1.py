import time
start_time= time.time()

n = int(input()) #개수 N을 입력받기
array=[] #n개의 정수를 입력받을 리스트

for x in range(n): #빈 리스트에 정수 추가
    array.append(int(input()))

array = sorted(array, reverse=True) #내림차순으로 array정리
# print(array) # [리스트로 출력]

for x in array:
    print(x,end=' ')

end_time = time.time()
print("time:", end_time-start_time)
