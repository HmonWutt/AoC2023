import re
from collections import OrderedDict

with open('day4_input.txt') as f:
    file = [line.rstrip('\n') for line in f]
file_stripped = [i.strip().split(':')[1] for i in file]

two_halves = []
for i in file_stripped:
    index = i.index('|')
    tmp = [i[0: index].strip(), i[index+1 :].strip()]
    two_halves.append(tmp)

# total = 0
# for i in two_halves:
#     count = []

#     first_half = i[0].replace(' ', '|')
#     second_half = i[1].replace(' ', ',')
#     print(first_half,second_half)
#     tmp_count = re.findall(r'(%s)' % first_half, second_half)
#     print(tmp_count)
#     for each in tmp_count:
#         count.append(each)
#     if len(count) > 0:
#         power =  pow(2, len(count)-1) 
#         print(len(count),power)
#         total+=power
    
# print(total)

total_1 = 0

def get_count(each):
  
    first_half = each[0].split(' ')
    second_half = each[1].split(' ')

    count_1 = 0
    for index,first in enumerate(first_half):

        if first in second_half and first != "":
            count_1+=1
        
        
    return count_1

    
def calculate_count (count_1):
    total_1 = 0 
    if count_1 > 0:
        power =  pow(2, count_1-1) 
       
        total_1+=power
    return total_1



total_cards = []

for i in two_halves:
      
    count= get_count(i)
    total_cards.append(count)
    power = calculate_count(count) 
    total_1+=power 

           
#print(total_cards)
print("part one:",total_1)


total_cards_dict = OrderedDict()
count_dict = OrderedDict()

for index,i in enumerate(total_cards):
    total_cards_dict[index] = i
    count_dict[index] = 1


for  key, value in total_cards_dict.items():
    for i in range(count_dict[key]):
        for j in range(key+1, key+value+1):
            count_dict[j] +=1

total_2=0

for key,value in count_dict.items():
    total_2 += value
print("part two",total_2)