with open('day9_input.txt') as f:
    file = [i.rstrip() for i in f]
new_file =[]
#new_file = [[int(z)for z in j.split(' ')][::-1] for j in file]########get part two answer without writing new functions
new_file = [[int(z)for z in j.split(' ')] for j in file]

def find_diff(list):
    new_list= []
    for k in range(len(list)-1):
        diff = list[k+1] - list[k]
        new_list.append(diff)
    return new_list

#print(find_diff(new_file[0]))      


count = 0
lst = new_file[2]
def find_all_zeros (lst):
    all_zeros = set()
    new_lst = [lst]
    while not(len(all_zeros) ==1  and 0 in all_zeros) :
        lst = find_diff(lst)

        all_zeros = set(lst)
        new_lst.append(lst)

    return new_lst 
 


def find_next_sequence(list): 
    
    for i in range(len(list)-1,0,-1):
        last_item_in_current_list = list[i][-1]
        last_item_in_list_above = list[i-1][-1]
        list[i-1].append (last_item_in_current_list + last_item_in_list_above)
        last_item_in_current_list = last_item_in_list_above
    return list[0][-1]
total= 0
for i in new_file:
    tmp = find_next_sequence(find_all_zeros(i))
    total+=tmp
print("Part one asnwer:",total)

##############################part two ##############################################
def find_diff_2(list):
    new_list= []
    for k in  range(len(list)-1,0,-1):
        diff = list[k] - list[k-1]
        new_list.append(diff)
    return [new_list[i] for i in range(len(new_list)-1,-1,-1)] ####reversed 


def find_all_zeros_2 (lst):
    all_zeros = set()
    new_lst = [lst]
    while not(len(all_zeros) ==1  and 0 in all_zeros) :
        lst = find_diff_2(lst)

        all_zeros = set(lst)
    
        new_lst.append(lst)

    return new_lst 


def find_next_sequence_2(lst): 
    
    for i in range(len(lst)-1,0,-1):
        last_item_in_current_list = lst[i][0]
        last_item_in_list_above = lst[i-1][0]
        lst[i-1].insert (0,last_item_in_list_above - last_item_in_current_list)
        
      

    return lst[0][0]
total_2 = 0
for j in new_file:
    tmp_2 = find_next_sequence_2(find_all_zeros_2(j))
    total_2+=tmp_2
print("Part two asnwer:",total_2)