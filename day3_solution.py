import re
file = open('day3_input.txt','r').readlines()

fileStripped = [i.rstrip() for i in file]
matrix = []
for row_num,row in enumerate(fileStripped): ### all the lines
    matrix.append([])
    for col_num, col in enumerate(row):
        matrix[row_num].append(col)


coordinates_lst ={}

for row, i in enumerate(fileStripped):
    coordinates = [(m.start(0), m.end(0)) for m in re.finditer('\d+', i)]
    coordinates_lst[row] = coordinates
maxcol= len(fileStripped[0])
maxrow = len(fileStripped)
passed = []

        
symbol_coordinates_list = []

for row, i in enumerate(fileStripped):
    coordinates = [m.start(0)for m in re.finditer(r'[^a-zA-Z\d\s:.]', i)]
    for j in coordinates:
        symbol_coordinates_list.append([row,j])

#print(symbol_coordinates_list)


def check_bound (current, max):
    if current > 0 and current < max:
        return [current-1,current, current+ 1]
    elif current == 0:
        return [current, current+ 1]
    else:
        return [current-1,current]


def check_symbol(symbol_lst):
    symbol_coverage= []
    for row,col in symbol_lst:
        rows = check_bound(row,maxrow)
        cols = check_bound(col,maxcol)
        for each_row in rows:
            for each_col in cols:
                symbol_coverage.append([each_row,each_col])
    return symbol_coverage

symbol_coverage = check_symbol(symbol_coordinates_list)
#f = open('f.txt', 'w') 
def check_if_neighbour(symbol_coverage, num_coordinates_dict):
    valid = set()
    for [row,col] in symbol_coverage:
        number_coordinates = num_coordinates_dict[row]
        for (start,end) in number_coordinates:
            if col in range(start,end):
                valid.add((row, start, end))

    return valid



valid = check_if_neighbour(symbol_coverage, coordinates_lst)
valid_list = []
total = 0
for row, col_start, col_end in valid:
    passed = fileStripped[row][col_start:col_end]
    valid_list.append(passed)
    total+= int(passed)


print(total)


    ######################part 2###############################

gear_ratio_list = []

for row, i in enumerate(fileStripped):

    gears = [m.start(0)for m in re.finditer(r'\*', i)]
    for j in gears:
        gear_ratio_list.append([row,j])


def check_asterisk(gear_ratio_list):
    gear_coverage= []
    for row,col in gear_ratio_list:
        rows = check_bound(row,maxrow)
        cols = check_bound(col,maxcol)
        for each_row in rows:
            for each_col in cols:
                gear_coverage.append([row,col, each_row,each_col])
    return gear_coverage
gear_coverage = check_asterisk(gear_ratio_list)

def check_if_shared_asterisk(gear_coverage, num_coordinates_dict):
    valid = set() 
   
    for [asterisk_row,asterisk_col, row,col] in gear_coverage:
        number_coordinates = num_coordinates_dict[row]
        for (start,end) in number_coordinates:
            if col in range(start,end):
            
                valid.add((str(asterisk_row) + str(asterisk_col) +","+ str(fileStripped[row][start:end])))
        

    return valid

output = check_if_shared_asterisk(gear_coverage, coordinates_lst)
output_split = {}
for i in output:
    split = i.split(",")
    if split[0] not in output_split:
        output_split[split[0]] = [split[1]]
    else:
        output_split[split[0]].append(split[1])
   


total_2 = 0
for key, values in output_split.items():
    if len(values) ==2:
        total_2 += int(output_split[key][0])* int(output_split[key][1])


print(total_2)