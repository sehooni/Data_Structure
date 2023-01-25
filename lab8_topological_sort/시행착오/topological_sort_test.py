
class DAG:
    def __init__(self, vertex_num):
        self.adj_list = [[] for _ in range(vertex_num)]
        self.visited = [False for _ in range(vertex_num)]

    def add_edge(self, u, v):
        # u : tail, v: head
        self.adj_list[u].append(v)

    def topological_sort(self):
        self.init_visited()
        ts_list = []
        for i in range(len(self.visited)):
            if not self.visited[i]:
                self.dfs(i, ts_list)
        ts_list.reverse()
        return ts_list

    def init_visited(self):
        for i in range(len(self.visited)):
            self.visited[i] = False

    def dfs(self, v, ts_list):
        self.visited[v] = True
        adj_v = self.adj_list[v]
        for u in adj_v:
            if not self.visited[u]:
                self.dfs(u, ts_list)

        ts_list.append(v)


def read_file(file):
    f = open(file, 'r', encoding='UTF-8')
    content = f.readlines()
    return content


if __name__ == "__main__":
    file = 'input.txt'
    documents = read_file(file)
    vortex = documents[0].split()
    vortex_num = len(vortex)
    print(vortex)
    print(vortex_num)
    d = DAG(vortex_num+1)

    for _, line in enumerate(documents[1:]):
        input_oper = line.strip().split()
        print(input_oper)
        start = 0
        for i in input_oper:
        # for i in range(10):
            edge = input_oper[start].split('-')
            print(edge)
            d.add_edge(int(edge[0]), int(edge[1]))
            # d.add_edge(edge[0], edge[1])
            start += 1

    ts_list = d.topological_sort()

    for i in ts_list:
        print(i, end=" ")
    #     input_oper[0]