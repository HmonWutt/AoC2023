from collections import defaultdict
import sys
sys.setrecursionlimit(100000) # fill function is not gentle
with open('day10_input.txt') as f:
    directions =  [[j for j in i.rstrip()] for i in f]

row_max = len(directions)-1
col_max= len(directions[0])-1

print(directions)
class Node:
    def __init__(self,name, row,col ):
        self.name = name
        self.row = row
        self.col = col
    
    def findNeighbourLeft(self,graph):
        if 0<= self.row <= row_max  and 0<=self.col-1<=col_max:
            return graph[self.row][self.col-1]
         
    def findNeighbourRight(self,graph):
        if 0<= self.row <= row_max  and 0<=self.col+1<=col_max :
            return  graph[self.row][self.col+1]
    def findNeighbourUp(self,graph):     
        if 0<= self.row -1 <= row_max and 0<=self.col<=col_max:
            return graph[self.row-1][self.col]
    def findNeighbourDown(self,graph):     
        if 0<= self.row +1 <= row_max  and 0<=self.col<=col_max :
            return graph[self.row+1][self.col]
        
     
    def getConnectedNeighbours(self, graph):
        self.left = self.findNeighbourLeft(graph)
   
        self.right = self.findNeighbourRight(graph)
 
        self.up = self.findNeighbourUp(graph)
        self.down = self.findNeighbourDown(graph)
        #print("up down left right",self.name,self.row,self.col,self.up.name,self.down.name,self.left.name,self.right.name)
        self.connected_neighbours = []  
      
    
        if self.name == "S": 
            if self.left and self.left.name not in[ '.',"|","J", "7"]:
              
                self.connected_neighbours.append(self.left)
             
            if self.right and self.right.name not in ['.',"L","F","|"]: 
                self.connected_neighbours.append(self.right) 
            if self.up and self.up.name not in ['.','L',"J","-"]: 
                self.connected_neighbours.append(self.up)
            if self.down and self.down.name not in ['.',"F","7","-"]: 
                self.connected_neighbours.append(self.down)
        
        if self.name == "-":
            if self.left and self.left.name not in ["|",".","J","7"]:
                self.connected_neighbours.append(self.left)
            if self.right and self.right.name not in ["|",".","L","F"]:
                self.connected_neighbours.append(self.right)  
         
        if self.name == "|":
            if self.up and self.up.name in [ "|","F","7"]:
                self.connected_neighbours.append(self.up)
            if self.down and self.down.name in ["|","L","J"]:
                self.connected_neighbours.append(self.down)
            
        if self.name =="L":
            if self.up and self.up.name in ["|","F","7"]:
                self.connected_neighbours.append(self.up)
            if self.right and self.right.name in ["-","J","7"]:
                self.connected_neighbours.append(self.right)

        if self.name =="J":
            if self.up and self.up.name in ["|","7","F"]:
                self.connected_neighbours.append(self.up)
            if self.left and self.left.name in ["-","L" ,"F"]:
                self.connected_neighbours.append(self.left)

        if self.name == "7":
            if self.left and self.left.name in ["-","F","L"]: 
                self.connected_neighbours.append(self.left)
            if self.down and self.down.name in ["|","J","L"]: 
                self.connected_neighbours.append(self.down)

        if self.name == "F":
            if self.right and self.right.name in ["-","7","J"]:
                self.connected_neighbours.append(self.right)
            if self.down and self.down.name in ["|", "L","J"  ]:   
                self.connected_neighbours.append(self.down)
                
        if len(self.connected_neighbours) >0:
            return self.connected_neighbours

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self,row,col):
        self.graph[row]+=col
       
directions_dict = Graph()
print("directions", directions)
node_graph = []
for row_ind,row in enumerate(directions):
    tmp=[]
    for col_ind, col in enumerate(row):
        name  = directions[row_ind][col_ind]
        node = Node(col,row_ind,col_ind)
        empty_list = []
        directions_dict.addEdge(node, [] )
        tmp.append(node)
    node_graph.append(tmp)

for ind,i in enumerate(directions_dict.graph):
    directions_dict.graph[i] += [i.getConnectedNeighbours(node_graph)]


for row_ind,node in enumerate(node_graph): #########find starting point###############
    for each in node:
        if each.name == "S":
            start = each
       
visited = set()
visited.add(start) 
def dfs(graph, visited, destination): 

    for neighbour in destination.connected_neighbours:  

        if neighbour not in visited: #and neighbour.name != ".": 
            #print("neighbour name",neighbour.name,neighbour.row, neighbour.col)
            visited.add(neighbour)          
            dfs(graph,visited,neighbour)

dfs(directions_dict.graph, visited,start)

# for every in visited:
#     print("visited",every.name, every.row, every.col)
print("PART ONE ANSWER: ",len(visited)/2)

            


