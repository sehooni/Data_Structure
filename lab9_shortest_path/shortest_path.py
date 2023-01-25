'''<Lab 12: Shortest Path>
we will implement Dijkstra’s algorithm for finding the shortest path.
When a graph structure (i.e. a set of nodes and edges) is given, your program prints the shortest path as a result of running Dijkstra’s algorithm.
You may want to use a priority queue to find the node with the smallest distance from the source node.

1. Input
Read a set of vertices from the first line and a set of edges from the second line of the given input file.
Each line is described below.
You may assume that your node is represented by any positive integer.

•	Vertices are given in the first line. Each vertex is separated by a space.
•	Edges are given in the second line.
    Each edge is represented by a pair of vertices and its (positive) weight.
    For example, “1-3-4” represents an edge from the vertex 1 to 3 with the weight value of 4.
'''
from heapq import heappush, heappop


class MinPriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        return heappop(self.heap)


class ShortestPath:
    def __init__(self, s, distance, p):
        self.source = s
        self.distance = distance
        self.p = p

    def print_shortest_path(self, dest):
        if self.source == dest:
            print(dest, end=" ")
            return
        if sp.p[dest] != None:
            self.print_shortest_path(self.p[dest])
        else:
            # print("There is no path")
            print(f"nowhere to go {dest}", end=" ")
            return
        print(dest, end=" ")


class Graph:
    # 모든 가중치보다 충분히 큰 수
    BIG_NUMBER = 2000

    def __init__(self, vertex_num):
        self.adj_matrix = [[None for _ in range(vertex_num+1)] for _ in range(vertex_num+1)]
        self.vertex_num = vertex_num

    def add_edge(self, u, v, w):
        self.adj_matrix[u][v] = w

    def dijkstra(self, s):
        distance = [self.BIG_NUMBER for _ in range(self.vertex_num)]        # 출발 정점에서 S에 있는 정점만 거쳐 v에 도달하는 경로 길이
        p = [None for _ in range(self.vertex_num)]                          # predecessor distance[v]를 구할 때 경로상에서 v의 바로 이전 노드

        S = set()                                                           # 최단 경로가 발견되는 정점 집합
        pq = MinPriorityQueue()
        for i in range(self.vertex_num):
            pq.push((self.BIG_NUMBER, i))                                   # push((distance, v))

        distance[s] = 0
        pq.push((0, s))

        while len(S) < self.vertex_num:
            d, v = pq.pop()
            if distance[v] != d:                                            # relaxation 이전 요소 무시
                continue

            S.add(v)

            adj_v = self.adjacent_set(v)
            for u, w_u_v in adj_v:
                if u not in S and distance[u] > distance[v]+w_u_v:
                    distance[u] = distance[v] + w_u_v
                    p[u] = v
                    pq.push((distance[u], u))

        sp = ShortestPath(s, distance, p)
        return sp

    def adjacent_set(self, v):
        adj_v = []
        for i in range(self.vertex_num):
            w = self.adj_matrix[v][i]
            if w:
                adj_v.append((i, w))
        return adj_v


def read_file(file):
    f = open(file, 'r', encoding='UTF-8')
    content = f.readlines()
    return content


if __name__ == "__main__":

    file = 'input12.txt'
    documents = read_file(file)
    vortex = documents[0].split()
    vortex_num = int(len(vortex))
    # print(vortex_num)
    g = Graph(vortex_num+1)

    # 간선의 갯수 구하기
    edge_info = documents[1].split()
    edge_num = len(edge_info)

    # vortex, edge, weight 분리하기
    for _, line in enumerate(documents[1:]):
        input_oper = line.strip().split()
        start = 0
        for _ in input_oper:
            edge = input_oper[start].split('-')
            # print(edge)
            a, b, c = int(edge[0]), int(edge[1]), int(edge[2])
            g.add_edge(a, b, c)
            start += 1
    while True:
        source = input(f"Start : ")
        sp = g.dijkstra(int(source))

        dest = input(f"End : ")
        sp.print_shortest_path(int(dest))
        print()

        count = 0
        check = input(f"restart?(Y/N) :")
        if check == "N" or check == "n":
            break

        elif check == "Y" or check == "y":
            continue

        else:
            print("Wrong operation")
            break