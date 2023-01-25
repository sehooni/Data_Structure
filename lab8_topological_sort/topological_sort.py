'''<Lab 11: Topological Sort>
we will implement an algorithm for topological sorting.
When a graph structure (i.e. a set of nodes and edges) is given, your program prints a list of nodes as a result of topological sort.
As we have discussed in class, topological sorting needs queue ADT in order to save the nodes that do not have any in-degree during the sorting process.

1. Input and Output
Read a set of vertices in the first line and a set of edges in the second line from the given input file.
Each line is described below. You may assume that the node is represented by an integer.

•	Vertices are given in the first line. Each vertex is separated by a space.
•	Edges are given in the second line. Each edge is represented by a pair of vertices. For example, “1-3” represents an edge from the vertex 1 to 3.

'''
from collections import deque

# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')


def read_file(file):
    f = open(file, 'r', encoding='UTF-8')
    content = f.readlines()
    return content


if __name__ == "__main__":

    file = 'input.txt'
    documents = read_file(file)
    vortex = documents[0].split()
    vortex_num = len(vortex)

    # # 간선의 갯수 구하기
    edge_info = documents[1].split()
    edge_num = len(edge_info)

    # 노드의 개수와 간선의 개수를 입력 받기
    v, e = int(vortex_num), edge_num

    # 모든 노드에 대한 진입차수는 0으로 초기화
    indegree = [0] * (v + 1)

    # 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
    graph = [[] for i in range(vortex_num + 1)]

    # 방향 그래프의 모든 간선 정보를 입력 받기
    for _ in range(e):
        for _, line in enumerate(documents[1:]):
            input_oper = line.strip().split()
            start = 0
            for _ in input_oper:
                edge = input_oper[start].split('-')
                a, b = int(edge[0]), int(edge[1])
                graph[a].append(b)  # 정점 A에서 B로 이동 가능
        # 진입 차수를 1 증가
                indegree[b] += 1
                start += 1

    topology_sort()