#떡을 자르는 높이 H는 가장 긴 길이보다 짧아야 함. 자르는 높이 H = mid
#떡을 잘랐을 때 잘린 떡의 길이 합이 작을 경우 -> mid값 줄이기 & 왼쪽 탐색
#떡을 잘랐을 때 잘린 떡의 길이 합이 클 경우 -> H값이 될 수 있으나 최대값이 아닐 수 있음 & 오른쪽 탐색

n,m = map(int,input().split())
array = list(map(int, input().split()))
array=sorted(array) #오름차순 정렬

start = array[0]
end = array[n-1]
H=0

while (start<=end):
    mid=(start+end)//2
    result=0
    for i in range(n):
        if (array[i]-mid) >0:
            result += array[i]-mid
    if result < m: # 왼쪽 탐색, H값(mid)줄 이기
        end=mid-1
    else:
        H=mid #일단 조건 만족하므로 H 값으로 기록,최대값을 찾기 위해 오른쪽 탐색
        start=mid+1
print(H)

