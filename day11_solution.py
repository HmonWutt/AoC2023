import numpy as np
from itertools import combinations


with open('day11_input.txt') as f:
    file = [[j for j in i.strip()] for i in f]

def find_empty_space(file):
    new_file = []
    for i in range(len(file)):
        if '#' not in file[i]:
            new_file.append(file[i])   
        new_file.append(file[i])
    return new_file

new_file= find_empty_space(file)
new_file_transposed = np.transpose(new_file)
latest_file = find_empty_space(new_file_transposed)
galaxies ={}
galaxy_id = 1
for row_ind,row in enumerate(latest_file):
    for col_ind,col in enumerate(row):
        if col =="#":
            galaxies[galaxy_id] = [row_ind, col_ind]
            galaxy_id+=1

galaxies_list = list(galaxies.keys())
galaxies_comb = list(combinations(galaxies_list, 2))

def find_distance(galaxies, galaxies_comb):
    total_distance = 0
    for first_galaxy, second_galaxy in galaxies_comb:
        first_galaxy_row = galaxies[first_galaxy][0]
        first_galaxy_col = galaxies[first_galaxy][1]
        second_galaxy_row = galaxies[second_galaxy][0]
        second_galaxy_col = galaxies[second_galaxy][1]
        
        row_distance = abs(first_galaxy_row-second_galaxy_row)
        col_distance = abs(first_galaxy_col - second_galaxy_col)

        distance = row_distance+col_distance
        total_distance+=distance
    return total_distance


print("total distance: ", find_distance(galaxies, galaxies_comb))


times = 10 
def find_distance_times_a_million(galaxies,galaxies_comb,  empty_rows, empty_cols, times):
    total_distance = 0
    for first_galaxy, second_galaxy in galaxies_comb:
        total_row_distance_for_this_pair = 0
        total_col_distance_for_this_pair = 0
        first_galaxy_row = galaxies[first_galaxy][0]
        first_galaxy_col = galaxies[first_galaxy][1]
        second_galaxy_row = galaxies[second_galaxy][0]
        second_galaxy_col = galaxies[second_galaxy][1]
        row_distance = abs(first_galaxy_row-second_galaxy_row)
        col_distance = abs(first_galaxy_col - second_galaxy_col)
        
        empty_row_count = 0
        for row in empty_rows:
      
            if (first_galaxy_row < row <second_galaxy_row  ) or (first_galaxy_row >row >second_galaxy_row  ) :
                empty_row_count+=1
        total_empty_rows = (empty_row_count *times)-empty_row_count       
        total_row_distance_for_this_pair+=(row_distance+total_empty_rows)
    
        empty_col_count = 0
        for col in empty_cols:   
            if (first_galaxy_col <= col <=second_galaxy_col ) or (first_galaxy_col >= col >=second_galaxy_col  ) :
                empty_col_count+=1

        total_empty_cols= (empty_col_count *times) - empty_col_count
        total_col_distance_for_this_pair +=(col_distance + total_empty_cols)
        distance = total_row_distance_for_this_pair+total_col_distance_for_this_pair
        total_distance+=distance

    return total_distance


transposed = np.transpose(file)

def find_empty_rows_cols(file):
    galaxies ={}
    galaxy_id = 1
    empty = []
    for row_ind,row in enumerate(file):
        if '#' not in row:
            empty.append(row_ind)
        for col_ind,col in enumerate(row):
            if col =="#":    
                galaxies[galaxy_id] = [row_ind, col_ind]
                galaxy_id+=1       
    return galaxies, empty


galaxies_2, empty_rows = find_empty_rows_cols(file)
file_transposed = np.transpose(file)
_,empty_cols = find_empty_rows_cols(file_transposed)

galaxies_list_2 = list(galaxies_2.keys())
galaxies_comb_2 = list(combinations(galaxies_list_2, 2))

print("part one answer:  ", find_distance_times_a_million(galaxies_2,galaxies_comb_2, empty_rows,empty_cols, 2))
print("part two answer:  ", find_distance_times_a_million(galaxies_2,galaxies_comb_2, empty_rows,empty_cols, 1000000))

