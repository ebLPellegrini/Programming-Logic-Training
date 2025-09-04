def main():
    graph = Graph()
    graph.addVertex('A')
    graph.addVertex('B')
    graph.addVertex('C')
    graph.addEdge('A', 'B')
    graph.addEdge('B', 'C')
    graph.display()
    print(graph.hasEdge('C', 'B'))
    graph.removeEdge('A', 'B')
    graph.removeVertex('A')
    graph.display()
    
class Graph:
    def __init__(self):
        self.adjacencyList = dict()
        
    def addVertex(self, vertex):
        if vertex not in self.adjacencyList.keys():
            self.adjacencyList[vertex] = set()
            
    def removeVertex(self, vertex):
        if vertex not in self.adjacencyList.keys():
            return
        for adjacentVertex in self.adjacencyList.keys():
            self.removeEdge(vertex, adjacentVertex)
        del self.adjacencyList[vertex]
        
    def addEdge(self, vertex1, vertex2):
        if vertex1 not in self.adjacencyList.keys():
            self.addVertex(vertex1)
        if vertex2 not in self.adjacencyList.keys():
            self.addVertex(vertex2)
        self.adjacencyList[vertex1].add(vertex2)
        self.adjacencyList[vertex2].add(vertex1)
        
    def removeEdge(self, vertex1, vertex2):
        if self.hasEdge(vertex1, vertex2):
            self.adjacencyList[vertex1].remove(vertex2)
            self.adjacencyList[vertex2].remove(vertex1)
        return
        
    def display(self):
        for vertex in self.adjacencyList:
            print(vertex, ' -> ', *self.adjacencyList[vertex])
            
    def hasEdge(self, vertex1, vertex2):
        return vertex2 in self.adjacencyList[vertex1]
    
main()