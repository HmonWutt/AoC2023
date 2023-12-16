with open ("day14_test.txt") as f:
    file = [[j for j in i.strip()] for i in f]

row_max = len(file)
col_max = len(file[0])


def roll_north(row,col):
    while 0<=row-1<= row_max-1 and file[row-1][col] == '.':
        file[row][col] = "."
        row = row -1
    file[row][col] = 'O'
           
def replace():
     for row_ind in range(row_max):
        for col_ind in range(col_max):
            if file[row_ind][col_ind] == "O":
                roll_north(row_ind,col_ind)


replace()
load = row_max
total_load = 0
for row in file:
    row_load = row.count("O") *load
    load-=1
    total_load+=row_load
print("part one answer: ",total_load)
