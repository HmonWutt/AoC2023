from heapq import heappush, heappop
import time
with open ('day17_input.txt') as f:
    file = [[int(j) for j in i.rstrip()] for i in f]

def print_board(board):
    for line in board:
        print(line)
visited = set()

dir_dict = {0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0), -1:(0,0)}
pq = [(0,0,0,-1,0)]



while pq:
    heatloss, row,col, direction , direction_count = heappop(pq)
    if row == len(file)-1 and col == len(file[0])-1:
        print("PART ONE ASNWER:  ",heatloss)
        break

    if (row,col, direction , direction_count) in visited:
        continue
    visited.add((row,col, direction , direction_count))

    if direction_count < 3 and direction!= -1:
        nr,nc = dir_dict[direction]
        next_row = row+nr
        next_col = col+nc
        if 0<=next_row <=len(file)-1 and  0<=next_col <=len(file[0])-1:
            heappush(pq,(heatloss+ file[next_row][next_col], next_row, next_col,direction, direction_count+1))

    for i in range(4):
        nr,nc = dir_dict[i]
        if direction != i and  (i+2)%4!= direction:
            next_row = row + nr
            next_col = col+nc           
            if 0<=next_row <=len(file)-1 and  0<=next_col <=len(file[0])-1:
                heappush(pq,(heatloss+ file[next_row][next_col], next_row,next_col, i, 1))


#####################################part 2###########################################
                
pq2 = [(0,0,0,-1,0)]
visited2= set()
while pq2:
    heatloss, row,col, direction , direction_count = heappop(pq2)
    if row == len(file)-1 and col == len(file[0])-1 and direction_count>=4:
        print("PART TWO ANSWER:      ",heatloss)
        break
    
    if (row,col, direction, direction_count) in visited2:
        continue
 

    visited2.add((row,col, direction , direction_count))
    while direction_count<4 and  direction != -1:
        nr,nc = dir_dict[direction]
        direction_count+=1
        row += nr
        col+=nc
        heatloss+=file[row][col]
        visited2.add((row,col,direction, direction_count))
    
    heappush(pq2,(heatloss, row, col,direction, direction_count))
    if direction_count < 10 and direction != -1:
        nr,nc = dir_dict[direction]
        next_row = row+nr
        next_col = col+nc
        if 0<=next_row <=len(file)-1 and  0<=next_col <=len(file[0])-1:
            heappush(pq2,(heatloss+ file[next_row][next_col], next_row, next_col,direction, direction_count+1))
   
    for i in range(4):
        nr,nc = dir_dict[i]
        if i != direction and  (i+2)%4!= direction:              
            if 0<=row + (nr*4)<=len(file)-1 and  0<=col+(nc*4) <=len(file[0])-1:
                next_row = row + nr
                next_col = col+nc
                heappush(pq2,(heatloss+ file[next_row][next_col], next_row, next_col, i, 1))






