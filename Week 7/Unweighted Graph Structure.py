#Vertex Graph
class Vertex:
    def __init__(self,label):

        self.label = label
        self.edges = [] #list of edges connected to the vertex

        self.edgesList = [] #a list to append the labels to for printing 

    def getInfo(self):
        #printing the vertex label and the list of edge labels associated with that vertex
        print("Vertex >> " + str(self.label) + "\nEdges >> " + str(self.edgesList))

    def addEdge(self,vertex2):
        if vertex2 in self.edges:
            pass
        else:
            #adding the edge to each vertex's edges list and adding the labels to edgesList so I can print the values
            (self.edges).append(vertex2)
            (self.edgesList).append(vertex2.label)

            (vertex2.edges).append(self)
            (vertex2.edgesList).append(self.label)

        
    

class Graph:
    def __init__(self):
        self.vertices = [] #list of vertices
        self.verticesList = [] #I append labels to this for printing
        self.numberOfVertices = 0

    def addVertex(self,vertex):
        self.numberOfVertices = self.numberOfVertices + 1
        
        v = Vertex(vertex) #creating the vertex in the vertex class
        (self.vertices).append(v) #adding vertex to vertices list
        (self.verticesList).append(v.label) #adding label to verticesList

        return(v)
        
    def getVertices(self):
        print(self.verticesList)
        
    def getNumberOfVertices(self):
        print(self.numberOfVertices)

    def depthFirstSearch(self,startVertex):
        
        stack = []
        visited = []

        stack.append(startVertex)

        while stack != []:
            u = stack.pop() #pop from top of stack
            if u.label not in visited:
                visited.append(u.label) #vertex has be visited so add the label to the list
                for edge in u.edges: 
                    stack.append(edge) #append the vertex's edges to the stack

        return(visited)

        #writing the data to a file
        f = open("DFS.txt","w")
        f.write("Depth First Traversal >> " + str(visited))
        f.close()





    def breadthFirstSearch(graph,startVertex):
        queue = []
        visited = []

        queue.insert(0,startVertex) #append the vertex to the queue

        while queue != []:
            u = queue.pop() #pop from end of start of queue

            if u.label not in visited:
                visited.append(u.label) #vertex has be visited so add the label to the list

                for edge in u.edges:
                    queue.insert(0,edge) #insert value to the front of the queue 

        return(visited)

        #writing the data to a file
        f = open("BFS.txt","w")
        f.write("Breadth First Traversal >> " + str(visited))
        f.close()


graph = Graph()
v1 = graph.addVertex(6)
v2 = graph.addVertex(5)
v3 = graph.addVertex(4)
v4 = graph.addVertex(3)
v5 = graph.addVertex(2)


v1.addEdge(v2)
v1.addEdge(v3)
v1.addEdge(v2)

v2.addEdge(v4)

v3.addEdge(v4)

v4.addEdge(v5)

v1.getInfo()
v2.getInfo()
v3.getInfo()
v4.getInfo()
v5.getInfo()

print(graph.depthFirstSearch(v3))

print(graph.breadthFirstSearch(v3))




        
        
