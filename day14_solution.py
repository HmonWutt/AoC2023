import tqdm
with open ("day14_input.txt") as f:
    file = [[j for j in i.strip()] for i in f]

row_max = len(file)
col_max = len(file[0])


def roll_north(row,col): 
    while 0<=row-1<= row_max-1 and file[row-1][col] == '.':
        file[row][col] = "."
        row = row -1
    file[row][col] = 'O'

def roll_south(row,col):
    while 0<=row+1<= row_max-1 and file[row+1][col] == '.':
        
        file[row][col] = "."
        row = row+1
    file[row][col] = 'O'  

def roll_east(row,col):
    while 0<=col+1<= col_max-1 and file[row][col+1] == '.':
        file[row][col] = "."
        col = col +1
    file[row][col] = 'O'  

def roll_west(row,col):
    while 0<=col-1<= col_max-1 and file[row][col-1] == '.':
        file[row][col] = "."
        col = col -1
    file[row][col] = 'O'  

def displace_north(file):
     for row_ind in range(row_max):
        for col_ind in range(col_max):
            if file[row_ind][col_ind] == "O":
                roll_north(row_ind,col_ind)
     return file

def displace_west(file):
     for row_ind in range(row_max):
        for col_ind in range(col_max):
            if file[row_ind][col_ind] == "O":
                roll_west(row_ind,col_ind)
     return file


load = row_max
total_load = 0

def displace_south(file):
     for row_ind in range(row_max-1,-1,-1):
        for col_ind in range(col_max):
            if file[row_ind][col_ind] == "O":
                roll_south(row_ind,col_ind)
     return file
def displace_east(file):
     for row_ind in range(row_max-1,-1,-1):
        for col_ind in range(col_max-1,-1,-1):
            if file[row_ind][col_ind] == "O":
                roll_east(row_ind,col_ind)
     return file



def spin(file):
    file = displace_north(file)
    # print("after north")
    # print(file)
    file = displace_west(file)
    # print("after west")
    # print(file)
    file = displace_south(file)
    # print("after south")
    # print(file)
    file = displace_east(file)
    # print("after east")
    # print(file)
    
    
    return file

start = 6

for cycle in tqdm.tqdm(range(1000)): 
    file = spin(file)
    total_load2 = 0
    load = row_max
    for row in file:
        row_load = row.count("O") *load
        load-=1
        total_load2+=row_load
print(total_load2)

#6,13,20,34,55,90,..993, 10002


