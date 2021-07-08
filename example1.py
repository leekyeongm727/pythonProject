n,m,k = map(int,input().split()) # 책 참고

while True:  # N개의 정수 입력받기
    n_number = list(map(int,input().split()))
    if len(n_number) < n:
        print("입력하신 데이터의 개수가 N보다 적습니다.")
    if len(n_number) > n:
        print("입력하신 데이터의 개수가 N보다 많습니다.")
    if len(n_number) == n:
        break

n_number.sort(reverse=True) # 내림차순으로 정렬
max1 = n_number[0] #n_number 리스트의 데이터 중 가장 큰 수
max2 = n_number[1]

result = 0
for x in range(m//(k+1)):
    for y in range(k):
        result = result + max1
    result = result + max2
for x in range(m%(k+1)):
    result = result + max1

print(result)
