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
new_file = []


def get_to_visit(current_row, current_col, file, direction):
    visited = set()
    to_visit = []
    empty_matrix = []

    for row_num, row in enumerate(file):
        tem = []
        for col_num, col in enumerate(row):

            tem.append('.')
        empty_matrix.append(tem)
    current_surface = file[current_row][current_col]
    empty_matrix[current_row][current_col] = "#"
    current_direction= light_direction_dict[direction]
    current_point = dict[current_surface][current_direction]

    if len(current_point) ==2:
        for point in current_point:
            to_visit.append([point[0]+current_row,point[1]+current_col, point[2]])
            visited.add(f'{point[0]+current_row},{point[1]+current_col},{point[2]}')
    else:
        to_visit.append([current_point[0]+current_row,current_point[1]+current_col, current_point[2]])
        visited.add(f'{current_point[0]+current_row},{current_point[1]+current_col}, {current_point[2]}')
    return visited,to_visit, empty_matrix


def mark_energised_tiles ( current_row,current_col,file,direction):
    visited,to_visit,empty_matrix = get_to_visit(current_row, current_col,file,direction)
    while to_visit :

        current_point = to_visit.pop()
        
        #print("current point",current_point)
        #print("todo", to_visit)
       
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
            
                    to_visit.append([tmp_row,tmp_col, each[2]])
        else:
            tmp_row = current_point[0]+new_point[0]
            tmp_col = current_point[1]+new_point[1]
        
            if (0<= tmp_row <=row_max-1 and 0<= tmp_col <= col_max-1) and (f'{tmp_row},{tmp_col}, {new_point[2]}' not in visited):
                visited.add(f'{tmp_row},{tmp_col}, {new_point[2]}')
                
                to_visit.append([tmp_row,tmp_col, new_point[2]])
    count = 0
    for row in empty_matrix:
        for col in row:
            if col =="#":
                count+=1
    return empty_matrix, count


_, part_one_count = mark_energised_tiles(0,0,file,"right")

print("PART ONE ANSWER:   ",part_one_count)  

start_energised_tile = []

def check_tiles (current_row, current_col, file, direction):
    filled_matrix= []
    visited, to_visit, empty_matrix = get_to_visit(current_row, current_col, file,direction)
    filled_matrix ,count =  mark_energised_tiles(visited,to_visit,empty_matrix)
    return  filled_matrix,count
    
top_row = []
for top_ind in range(1,len(file)-1):

    _,count = mark_energised_tiles(0,top_ind,file,"down")
    top_row.append([0,top_ind,count])


for left_ind in range(len(file)):

    _,count = mark_energised_tiles(left_ind,0,file,"right")
    top_row.append([left_ind,0,count])

for right_ind in range(len(file)):

    _,count = mark_energised_tiles(right_ind,row_max -1 ,file,"left")
    top_row.append([right_ind,row_max-1,count])

for bottom_ind in range(1,len(file)-1):

    _,count = mark_energised_tiles(0,bottom_ind,file,"up")
    top_row.append([0,bottom_ind,count])
bigger = 0
for r,c,cnt in top_row:
    if cnt > bigger:
        bigger = cnt
print('')
print("PART TWO ANSWER:   ",bigger)
