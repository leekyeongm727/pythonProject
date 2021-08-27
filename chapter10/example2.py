# 도시분할계획 => 유지비가 큰 값을 기준으로 마을 분리하기
# 크루스칼 알고리즘//모든 간선에 대하여 정렬을 수행한 뒤, 가장 거리가 짧은 간선부터 집합에 포함
def find_parent(parent, x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m = map(int, input().split())
parent=[0]*(n+1)

edges=[]
result=0

for i in range(1,n+1):
    parent[i]=i

for _ in range(m):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))

for edge in edges:
    cost, a, b=edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
        max_n=cost #가장 큰 수=>오름차순으로 정렬했기때문에 맨 마지막 값

print(result-max_n)