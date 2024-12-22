class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range (V)]

    def addEdge(self, h, j):
        self.adj[h].append(j)
        self.adj[j].append(h)
    
    def DFS(self, temp, h, visited):
        visited[h] = True
        temp.append(h)
        for i in self.adj[h]:
            if visited[i] == False:
                temp = self.DFS(temp, i , visited)
        
        return temp
    
    def connect(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for h in range(self.V):
            if visited [h] == False:
                temp = []
                cc.append(self.DFS(temp, h, visited))
        return cc


g = Graph(5)
g.addEdge(1,0)
g.addEdge(2,3)
g.addEdge(3,4)
cc = g.connect()
print("Here art thines connected compononononents: ")

print(cc)