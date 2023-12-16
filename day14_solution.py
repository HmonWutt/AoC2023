with open ("day14_test.txt") as f:
    file = [[j for j in i.strip()] for i in f]

row_max = len(file)
col_max = len(file[0])


def checkabove(row,col):
    while 0<=row-1<= row_max-1 and file[row-1][col] == '.':
        file[row][col] = "."
        row = row -1
    
    file[row][col] = 'O'
           
def replace():
     for row_ind in range(row_max):
        for col_ind in range(col_max):
            if file[row_ind][col_ind] == "O":
                checkabove(row_ind,col_ind)


replace()
        
print(file)