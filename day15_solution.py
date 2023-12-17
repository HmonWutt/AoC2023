import tqdm
with open ('day15_input.txt') as f:
    file = [i.split(',') for i in f][0]

ascii = {}
for i in range(0, 128):
    ascii[chr(i)] = i
print(file)
def find_total(string):
    total = 0
    tmp_total = 0
    for each_letter in string:
        times17 = (total+ascii[each_letter]) *17
        tmp_total = times17 % 256
        total =tmp_total
    return total
total_1 = 0
for string in tqdm.tqdm(file):
    tmp = find_total(string)
    total_1+=tmp
print("part one answer: ", total_1)
print("")
boxes = {}
for strng in tqdm.tqdm(file):
    if strng[-2] == '=':
        letter = strng.split('=')[0]
        number = strng.split('=')[1]
       
        if find_total(letter) not in boxes:
            boxes[find_total(letter)] = [letter+ " " + number]
       
        else:
            box = [i.split(' ')[0] for i in boxes[find_total(letter)]]
               
            if letter in box:
                match_ind = box.index(letter)
                boxes[find_total(letter)][match_ind]= letter+ " " + number
                
                    #çprint("here", strng, boxes,boxes[find_total(letter)])
            else:
                boxes[find_total(letter)].append(letter+ " " + number)

    else:
    
        letter = strng.split('-')[0]
        number = strng.split('-')[1]
        if find_total(letter) in boxes:
            box = boxes[find_total(letter)]
        
            for each in box:    
                if letter == each.split(' ')[0]:
                    boxes[find_total(letter)].remove(each)
       
#print("final",boxes)
total_2 = 0
for box_num,values in boxes.items():
    if values:
        for slot,value in enumerate(values):
            focal_length = value.split(' ')[1]
            focusing_power = (box_num+1)*(slot+1) * int(focal_length)
            total_2+=focusing_power


print("part two answer:  ",total_2)