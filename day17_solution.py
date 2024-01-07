from heapq import heappush, heappop
import time
with open ('day17_input.txt') as f:
    file = [[int(j) for j in i.rstrip()] for i in f]

def print_board(board):
    for line in board:
        print(line)
visited = set()
pq = [(0,0,0,0,0,0)]
path = [[l for l in m] for m in file]

while pq:
    heatloss, row,col, direction_row, direction_col , direction_count = heappop(pq)
    if row == len(file)-1 and col == len(file[0])-1:
        print("PART ONE ASNWER:  ",heatloss)
        break

    if (row,col, direction_row, direction_col , direction_count) in visited:
        continue

    visited.add((row,col, direction_row, direction_col , direction_count))
    #for next_row, next_col in [(0,1),(0,-1),(1,0),(-1,0)]:

    if direction_count < 3 and (direction_row,direction_col) != (0,0):
        next_row = row+direction_row
        next_col = col+direction_col
        if 0<=next_row <=len(file)-1 and  0<=next_col <=len(file[0])-1:
            heappush(pq,(heatloss+ file[next_row][next_col], next_row, next_col,direction_row, direction_col, direction_count+1))

    for new_row, new_col in [(0,1),(0,-1),(1,0),(-1,0)]:
        if (new_row,new_col) != (direction_row,direction_col) and (new_row,new_col) != (-direction_row,-direction_col):
            next_row = row + new_row
            next_col = col+new_col           
            if 0<=next_row <=len(file)-1 and  0<=next_col <=len(file[0])-1:
                heappush(pq,(heatloss+ file[next_row][next_col], next_row,next_col, new_row, new_col, 1))


#####################################part 2###########################################
                
pq2 = [(0,0,0,0,0,0)]
visited2= set()
while pq2:
    heatloss, row,col, direction_row, direction_col , direction_count = heappop(pq2)
    
    if row == len(file)-1 and col == len(file[0])-1 and direction_count>=4:
        print("PART TWO ANSWER:      ",heatloss)
        break
    
    if (row,col, direction_row, direction_col , direction_count) in visited2:
        continue
 

    visited2.add((row,col, direction_row, direction_col , direction_count))
    while direction_count<4 and  (direction_row,direction_col) != (0,0):
    
        direction_count+=1
        row += direction_row
        col+=direction_col
        heatloss+=file[row][col]
        visited2.add((row,col,direction_row,direction_col, direction_count))
    
    heappush(pq2,(heatloss, row, col,direction_row, direction_col, direction_count))
    if direction_count < 10 and (direction_row,direction_col) != (0,0):
        next_row = row+direction_row
        next_col = col+direction_col
        if 0<=next_row <=len(file)-1 and  0<=next_col <=len(file[0])-1:
            heappush(pq2,(heatloss+ file[next_row][next_col], next_row, next_col,direction_row, direction_col, direction_count+1))
            
    for new_row, new_col in [(0,1),(0,-1),(1,0),(-1,0)]:
     
        if (new_row,new_col) != (direction_row,direction_col) and (new_row,new_col) != (-direction_row,-direction_col):
                     
            if 0<=row + (new_row*4)<=len(file)-1 and  0<=col+(new_col*4) <=len(file[0])-1:
                next_row = row + new_row
                next_col = col+new_col  
                heappush(pq2,(heatloss+ file[next_row][next_col], next_row,next_col, new_row, new_col, 1))






