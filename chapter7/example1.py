def binary_search(array,target, start, end): #이진탐색 함수
    if start > end:
        return 'no'
    mid = (start+end)//2
    if array[mid] == target:
        return 'yes'
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n=int(input())
n_array = list(map(int,input().split()))
m=int(input())
m_array = list(map(int, input().split()))

for i in range(m):
    result = binary_search(n_array,m_array[i], 0, n-1)
    print(result,end=' ')