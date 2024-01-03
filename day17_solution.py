from heapq import heappush, heappop
with open ('day17_test.txt') as f:
    file = [[int(j) for j in i.rstrip()] for i in f]
#print(file)

visited = set()
pq = [(0,0,0,0,0,0)]
while pq:
    heatloss, row,col, direction_row, direction_col , direction_count = heappop(pq)
    if row == len(file)-1 and col == len(file[0])-1:
        print(heatloss)
        break
    
    if (heatloss, row,col, direction_row, direction_col , direction_count) in visited:
        continue
 
    visited.add((heatloss, row,col, direction_row, direction_col , direction_count))
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
            