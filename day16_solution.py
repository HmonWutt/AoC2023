import re
with open('day16_input.txt') as f:
    file =[i.strip() for i in f]

light_direction_dict = {'right':0, 'left':1, 'up': 2, 'down':3}
dict = {
    "-": [[0,1,'right'],[0,-1,'left'],[[0,1,'right'],[0,-1,'left']],[[0,1,'right'],[0,-1,'left']]], 
    "|":[[[-1,0,'up'],[1,0,'down']],[[-1,0,'up'],[1,0,'down']],[-1,0,'up'],[1,0,'down']],
    "\\":[[1,0,'down'],[-1,0,'up'],[0,-1,'left'],[0,1,'right']],
     "/":[[-1,0,'up'],[1,0,'down'],[0,1,'right'],[0,-1,'left']],
    ".":[[0,1,'right'],[0,-1,'left'],[-1,0,'up'],[1,0,'down']]
        }

row_max = len(file)
col_max = len(file[0])


class Node:
    def __init__(self,surface, row,col ):
        self.surface = surface
        self.row = row
        self.col = col

empty_matrix = []
new_file = []
for row_num, row in enumerate(file):
    tmp = []
    tem = []
    for col_num, col in enumerate(row):
        node = Node(col, row_num, col_num)

        tmp.append(node)
        tem.append('.')
    new_file.append(tmp)
    empty_matrix.append(tem)
path=set()

current_row = 0
current_col = 0
current_surface= file[current_row][current_col]
print("current surface",current_surface)
current_node = new_file[current_row][current_col]

direction ='right'
current_direction= light_direction_dict[direction]

path.add(current_node)
current_point = dict[current_surface][current_direction]
to_visit = []
to_visit.append(current_point)
visited = set()
visited.add(f'{current_row},{current_col}, {direction}')
print("current point", current_point)
empty_matrix[current_row][current_col] = "#"

while to_visit :

    current_point = to_visit.pop()
    
    # print("current point",current_point)
    # print("todo", to_visit)
    empty_matrix[current_point[0]][current_point[1]] = "#"

    new_surface =  file[current_point[0]][current_point[1]]
    # print("current surface",new_surface)

    current_direction = light_direction_dict[current_point[2]]
    new_point = dict[new_surface][current_direction]
    # print("newpoint",new_point)
    if len(new_point) == 2:

        for each in new_point:
            #print("each", each)
            tmp_row = current_point[0]+each[0]
            tmp_col = current_point[1]+each[1]
            if (0<= tmp_row <=row_max-1 and 0<= tmp_col <= col_max-1) and (f'{tmp_row},{tmp_col}, {each[2]}'not in visited):

                visited.add(f'{tmp_row},{tmp_col}, {each[2]}')
                current_node = new_file[tmp_row][tmp_col]
                
                if current_node not in path:
                    path.add(current_node)
        
                to_visit.append([tmp_row,tmp_col, each[2]])
    else:
        tmp_row = current_point[0]+new_point[0]
        tmp_col = current_point[1]+new_point[1]
       
        if (0<= tmp_row <=row_max-1 and 0<= tmp_col <= col_max-1) and (f'{tmp_row},{tmp_col}, {new_point[2]}' not in visited):
            visited.add(f'{tmp_row},{tmp_col}, {new_point[2]}')
            
            if current_node not in path:
                path.add(current_node)
            to_visit.append([tmp_row,tmp_col, new_point[2]])

count = 0
for row in empty_matrix:
    for col in row:
        if col =="#":
            count+=1

print("PART ONE ANSWER:   ",count)  


 

