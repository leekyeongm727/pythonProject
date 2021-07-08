'''최소 횟수로 1 만들기'''
while True:
    n,k = map(int,input().split())
    if n >= k:
        break
    print("n>=k인 값을 입력하세요")

result=0
while True:
    if n%k == 0:
        n = n//k
        result += 1
    else:
        n=n-1
        result += 1
    if n == 1:
        break

print("n을 1로 만드는 최소 횟수는", result)
