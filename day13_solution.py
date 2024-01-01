import numpy as np
import pandas as pd
f =  open('day13_input.txt','r').read()
original_file =  f.split('\n')

tmp = []
original_split = []
for each_row in original_file:

    if len(each_row) > 0:
        tmp.append(each_row)
      
    else:
        original_split.append(tmp)
        tmp=[]

def transposer(file):
    tmp = [[a for a in b] for b in file]
    transposed  = [''.join(list(j)) for j in np.transpose(tmp)]
    return transposed


def find_reflection_point( file):
    for i in range(len(file)-1):
        if file[i] == file[i+1]:
            if check_if_reflection(i,i+1,file)==True:
                return i,i+1

    
def check_if_reflection(current,next,file):
    count = 0
    
    while current-1 >=0 and next+1 <= len(file)-1:
        if file[current-1] != file[next+1]:
            return  False 
        else:
            current -=1
            next +=1  
            count+=1  
    return True
   
            
def calculate_result (file):
    result = 0

    if find_reflection_point(file) :
        current, next = find_reflection_point( file)
        result = (current+1) *100
        return result
       
    else:
        current, next = find_reflection_point(transposer(file))
        result = current+1
        return result
  
total = 0

for ind,each in enumerate(original_split[:-1]):
    result = calculate_result(each)

    total+=result
print("PART ONE ANSWER: ", total)



def find_smudge(current_ind, next_ind, file):
    difference = 0
    current = file[current_ind]
    next = file[next_ind]
    for i in range(len(current)):
        if difference > 1:
            break
        if current[i] != next[i]:
            difference+=1
    return difference


def count_smudge(current, next, file):
    smudge = 0
    while current >= 0 and next <= len(file)-2:
        if find_smudge(current,next,file) >=2:
            break
        if find_smudge(current, next,file) == 0:
            current-=1
            next+=1

        if find_smudge(current, next,file) == 1:
            smudge+=1
            current-=1
            next+=1
    return smudge


def check_if_one_smudge(file):
    for i in range(len(file)-1):
        current = i
        next = i+1
        if find_smudge(current, next, file) == 1 and check_if_reflection(current,next,file) == True:
            return current,next        
        if file[current]== file[next] and count_smudge(current, next, file) == 1:
            return current,next
    return -1
        
        
        

total_2 =0           
for ind,file in enumerate(original_split[:-1]):
    print("id-------------------,",ind,len(file))
    if check_if_one_smudge(file) != -1:
        current, _ = check_if_one_smudge(file)
        result = (current+1)*100

    else:
        if check_if_one_smudge(transposer(file)) == -1:
            print("This should never happen", ind, check_if_one_smudge(transposer(file)))
            for i in file:
                print(i)

            print('')
            for i in transposer(file):
                print(i)
        else:
            current,_ = check_if_one_smudge(transposer(file))
            result = current+1
    total_2+=result
print("part two answer:  ", total_2)



 
