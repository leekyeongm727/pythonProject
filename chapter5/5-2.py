import time
from collections import  deque

start_time = time.time()

n,m = map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]

result=1

def bfs(x,y): # queue를 이용한 bfs를 쓴 이유는? =>상하좌우 살펴보고 전체를 훑어볼 수 있는 방법
    global result
    global graph

    queue=deque()
    queue.append((x,y))

    while queue:

        x,y=queue.popleft()
        for i in range(4): # 상하좌우 4방향 확인
            n_x = x +dx[i]
            n_y = y +dy[i]
            if n_x<0 or n_x>=n or n_y<0 or n_y>=m: #틀을 벗어나는 경우 무시
                continue
            if graph[n_x][n_y]==0: #괴물이 있는 경우 무시(skip)
                continue

            if graph[n_x][n_y]==1:
                queue.append((n_x,n_y))
                graph[n_x][n_y]=2
                #result+=1
            #최단거리만을 더해주게 어떻게 만들어야 할까
    return result

print(bfs(0,0))