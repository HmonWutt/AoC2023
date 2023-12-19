import numpy as np
from itertools import combinations


with open('day11_test.txt') as f:
    file = [[j for j in i.strip()] for i in f]


def find_empty_space(file):
    new_file = []
    empty_space = []
    for i in range(len(file)):
        if '#' not in file[i]:
            new_file.append(file[i])
            empty_space.append(i)
        
        new_file.append(file[i])
    return new_file, empty_space
new_file,empty_rows = find_empty_space(file)
new_file_transposed = np.transpose(new_file)
latest_file,empty_cols = find_empty_space(new_file_transposed)
galaxies ={}
galaxy_id = 1
for row_ind,row in enumerate(latest_file):
    for col_ind,col in enumerate(row):
        if col =="#":
            galaxies[galaxy_id] = [row_ind, col_ind]
            galaxy_id+=1
#print(galaxies)

galaxies_list = list(galaxies.keys())
galaxies_comb = list(combinations(galaxies_list, 2))

#galaxies_distance = {}
def find_distance(galaxies):
    total_distance = 0
    for first_galaxy, second_galaxy in galaxies_comb:
        first_galaxy_row = galaxies[first_galaxy][0]
        first_galaxy_col = galaxies[first_galaxy][1]
        second_galaxy_row = galaxies[second_galaxy][0]
        second_galaxy_col = galaxies[second_galaxy][1]
     
        row_distance = abs(first_galaxy_row-second_galaxy_row)
        col_distance = abs(first_galaxy_col - second_galaxy_col)
        distance = row_distance+col_distance
        #galaxies_distance[f'{first_galaxy,second_galaxy}'] = distance
        total_distance+=distance
    return total_distance


#print(galaxies_distance)
print("total distance: ", find_distance(galaxies))

print(empty_rows,empty_cols)