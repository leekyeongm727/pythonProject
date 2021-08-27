n,m = map(int, input().split()) #n번, m개의 연산

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

parent = [0]*(n+1)

for x in range(n+1):
    parent[x]=x

result=[]
for i in range(m):
    sign, a, b = map(int, input().split())
    if sign == 0: #0일 때는 합치기 연산
        union_parent(parent,a,b)
    if sign == 1: #같은 팀 여부 확인
        if find_parent(parent,a)==find_parent(parent,b):
            result.append("YES")
        else:
            result.append("NO")

for x in result:
    print(x)