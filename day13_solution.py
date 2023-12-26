import numpy as np
f =  open('day13_test.txt','r').read()
original_file =  f.split('\n')

tmp = []
original_split = []
for each_row in original_file:
    if each_row != '':
        tmp.append(each_row)
    else:
        original_split.append(tmp)
        tmp=[]
#print(original_split)
def transposer(file):
    tmp = [[a for a in b] for b in file]
    transposed  = [''.join(list(j)) for j in np.transpose(tmp)]
    return transposed


def find_reflection_point( file):

    for i in range(len(file)-1):

        if file[i] == file[i+1]:
            print("reflction point",i,i+1)

            return i,i+1

            
def check_if_reflection(current,next,file):
   
    while current-1 >=0 and next+1 <= len(file)-1:
    
        if file[current-1] != file[next+1]:
            return False
        current -=1
        next +=1       
    return current,next
            
            
def calculate_result (file):
    result = 0
    current,next = find_reflection_point(file)
    
    if check_if_reflection(current,next, file)==False:
       
        current, next = find_reflection_point(transposer(file))
        
        result = current +1

    else:
       
        
        row = current+1
        result = row*100

    return result


    
total = 0

for each in original_split:
    print("each",each)
    result = calculate_result(each)
    total+=result
print("PART ONE ANSWER: ", total)
   



        


