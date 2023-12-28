from collections import defaultdict
import sys
sys.setrecursionlimit(1000000000) # fill function is not gentle
with open('day10_input.txt') as f:
    directions =  [[j for j in i.rstrip()] for i in f]

row_max = len(directions)
col_max= len(directions[0])

class Node:
    def __init__(self,name, row,col ):
        self.name = name
        self.row = row
        self.col = col
    
    def findNeighbourLeft(self,graph):
        if 0<= self.row <= row_max-1  and 0<=self.col-1<=col_max-1:
            return graph[self.row][self.col-1]
         
    def findNeighbourRight(self,graph):
        if 0<= self.row <= row_max-1  and 0<=self.col+1<=col_max-1 :
            return  graph[self.row][self.col+1]
    def findNeighbourUp(self,graph):     
        if 0<= self.row -1 <= row_max-1 and 0<=self.col<=col_max-1:
            return graph[self.row-1][self.col]
    def findNeighbourDown(self,graph):     
        if 0<= self.row +1 <= row_max -1 and 0<=self.col<=col_max -1:
            return graph[self.row+1][self.col]
        
    def getAllNeighbours(self,graph):
        self.all_neighbours=[]
        self.left = self.findNeighbourLeft(graph)
        self.up = self.findNeighbourUp(graph)
        self.down = self.findNeighbourDown(graph)
        self.right = self.findNeighbourRight(graph)
        
        if self.left:
            self.all_neighbours.append(self.left)
        if self.right:
            self.all_neighbours.append(self.right)
        if self.up:
            self.all_neighbours.append(self.up)
        if self.down:
            self.all_neighbours.append(self.down)
        return self.all_neighbours
    
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
       

node_graph = []
for row_ind,row in enumerate(directions):
    tmp=[]
    for col_ind, col in enumerate(row):
        name  = directions[row_ind][col_ind]
        node = Node(col,row_ind,col_ind)
        tmp.append(node)
    node_graph.append(tmp)

for row_ind,node in enumerate(node_graph): #########find starting point###############
    for each in node:
        if each.name == "S":
            start = each
   
visited = set()
visited.add(start) 
def dfs(graph, destination,visited): 
    
    for neighbour in destination.getConnectedNeighbours(graph):  

        if neighbour not in visited: 
            visited.add(neighbour)
              
            dfs(graph,neighbour,visited)


dfs(node_graph, start,visited)
print("PART ONE ANSWER: ",len(visited)//2)


def flood_fill(graph, row,col): 
    row_max = len(graph)-1
    col_max = len(graph[0])-1
    old_symbol = '.'
    new_symbol = "O"
    queue = [(row,col)]
    while queue:
        row,col = queue.pop(0)
        if (row <0 or row >row_max) or (col <0 or col>col_max) or graph[row][col] !=old_symbol:
            continue
        else:
            graph[row][col] = new_symbol
            flood_fill(graph,row,col-1)
            flood_fill(graph,row,col+1)
            flood_fill(graph,row-1,col)
            flood_fill(graph,row+1,col)

board = [["." for m in range(3*col_max)] for n in range(row_max*3)]    

def mark_border(board,node,directions):
    row_num = node.row
    col_num = node.col
    middle_row = 3*row_num +1
    middle_col = 3*col_num +1
    if directions[row_num][col_num]=='-':

        board[middle_row][middle_col] = "#"
        board[middle_row][middle_col-1]= '#'
        board[middle_row][middle_col+1] = "#"

    if directions[row_num][col_num]=='|':
        
        board[middle_row][middle_col] = "#"
        board[middle_row-1][middle_col]='#'
        board[middle_row+1][middle_col] = "#"

    if directions[row_num][col_num]=='L':
        
        board[middle_row][middle_col] = "#"
        board[middle_row-1][middle_col]='#'
        board[middle_row][middle_col+1] = "#"
    
    if directions[row_num][col_num]=='J':
        
        board[middle_row][middle_col] = "#"
        board[middle_row-1][middle_col]='#'
        board[middle_row][middle_col-1] = "#"
    if directions[row_num][col_num]=='7':
        
        board[middle_row][middle_col] = "#"
        board[middle_row+1][middle_col]='#'
        board[middle_row][middle_col-1] = "#"

    if directions[row_num][col_num]=='F':
        
        board[middle_row][middle_col] = "#"
        board[middle_row+1][middle_col]='#'
        board[middle_row][middle_col+1] = "#"
    if directions[row_num][col_num] =="S":
        
        board[middle_row][middle_col] = "#"
        board[middle_row+1][middle_col]='#'
        board[middle_row][middle_col-1] = "#"

    

def flood_fill_board(graph, row,col): 
    row_max = len(graph)-1
    col_max = len(graph[0])-1
    old_symbol = '.'
    new_symbol = "O"
    queue = [(row,col)]
    while queue:
        row,col = queue.pop(0)
      
        if (row <0 or row >row_max) or (col <0 or col>col_max) or graph[row][col] !=old_symbol:
            continue
        else:
            graph[row][col] = new_symbol
            queue.append((row,col-1))
            queue.append((row,col+1))
            queue.append((row-1,col))
            queue.append((row+1,col))

for e_node in visited:
    mark_border(board,e_node,directions)

flood_fill_board(board,0,0)
count = 0
for row_num in range(0,len(board),3):
    for col_num in range(0,len(board[0]),3):
        middle_row= row_num+1
        middle_col = col_num+1

        true_counts =0
        for row in range(middle_row-1,middle_row+2):
            for col in range(middle_col-1, middle_col+2):
                if board[row][col] == '.':
                    true_counts+=1
                   
        if true_counts == 9:
            count+=1
                       
print("PART TWO ANSWER: ",count)
newboard = ["".join(i) for i in board]

