# 1=>K=>X
# 양방향 이동 가능
# 최소 이동 시간 출력/불가능할 경우 -1
INF = int(1e9)

n,m = map(int,input().split()) #n:노드 m:간선의 개수
graph = [[INF]*(n+1) for _ in range(n+1)] #2차원 리스트를 만들고, 모든 값을 무한으로 초기화

for a in range(1,n+1): #자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b]=1 #양방향
    graph[b][a]=1

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,1+n):
            graph[a][b]= min(graph[a][b],graph[a][k]+graph[k][b])

x,k = map(int, input().split())

result = graph[1][k]+graph[k][x]

if result >= INF:
    print('-1')
else:
    print(result)