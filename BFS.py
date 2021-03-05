from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, s):
        visited = []
        queue = []

        visited.append(s)
        queue.append(s)

        while queue:
            x = queue.pop()
            print(f"{x}->", end="")
            for neighbour in self.graph[x]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

    def dfs(self ,s):
        visited = []

        def df(graph,v):
            visited.append(v)
            print(f"{v}=>",end="")
            for neighbour in graph[v]:
                if neighbour not in visited:
                    df(graph,neighbour)
        df(self.graph,s)







g = Graph()
g.addEdge('a','f')
g.addEdge('a','e')
g.addEdge('a','b')
g.addEdge('b','h')
g.addEdge('g','f')
g.addEdge('f','h')
g.addEdge('g','h')
g.addEdge('e','g')

#g.bfs('d')
g.dfs('a')

