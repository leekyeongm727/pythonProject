#플로이드 워셜 알고리즘 => 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

n = int(input()) #노드의 개수 및 간선의 개수를 입력받기
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)] #2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화

for a in range(1,n+1): #자기 자신에서 자기 자신으롤 가는 비용은 0으로 초기화
    for b in range(1,n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m): #각 간선에 대한 정보를 입력받아, 그 값으로 초기화
    a,b,c = map(int, input().split()) # A에서 B로 가는 비용은 C라고 설정
    graph[a][b] = c

for k in range(1, n+1): # 점화식에 따라 플로이드 워셜 알고리즘을 수행
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1,n+1): #수행된 결과를 출력
    for b in range(1,n+1):
        if graph[a][b] == 'INF': #도달할 수 없는 경우, 무한(INFINITY)이라고 출력
            print("INFINITY", end=" ")
        else: #도달할 수 있는 경우, 거리를 출력
            print(graph[a][b], end=" ")
    print()