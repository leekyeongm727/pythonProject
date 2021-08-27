#커리큘럼
#위상정렬 (방향성에 거스르지 않도록 순서대로 나열)

import time
from collections import deque
import copy

n = int(input())  # 강의 수
indegree = [0] * (n + 1)  # 모든 노드에 대한 진입차수는 0으로 초기화
graph = [[] for i in range((n + 1))]  # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
running = [0] * (n + 1)  # 강의 시간

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    running[i] = data[0]
    x = 1
    while data[x] != -1:  # 선수 과목이 주어진다면
        graph[data[x]].append(i)
        indegree[i] += 1  # 진입차수를 1 증가
        x += 1


# 위상 정렬 함수
def topology_sort():
    # result=[] # 알고리즘 수행 결과를 담을 리스트
    result = copy.deepcopy(running)
    q = deque()  # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:  # 큐가 빌 때까지 반복
        now = q.popleft()  # 큐에서 원소 꺼내기
        for i in graph[now]:  # 현재원소와 연결된 노드 처리
            result[i] = max(result[i], result[now] + running[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])


topology_sort()