import time

def dfs(i,j):
    global graph
    if i<0 or i>=n or j<0 or j<=m:
        return -1
    if graph[i][j]==0:
        graph[i][j]=1
        print("hh")
        dfs(i+1, j)
        dfs(i-1, j)
        dfs(i, j+1)
        dfs(i, j-1)

start_time= time.time()
n,m = map(int, input().split()) # n,m 각각 입력받기

graph=[] # graph입력 받을 리스트
for i in range(n):
    graph.append(list(map(int, input())))

count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            dfs(i,j)
            count += 1
print(count)
#머르겟다..

end_time=time.time()
print("time:", end_time-start_time)


