import tqdm
with open ('day15_input.txt') as f:
    file = [i.split(',') for i in f][0]
print(file)
ascii = {}
for i in range(0, 128):
    #print(chr(i))
    ascii[chr(i)] = i

def find_total(string):
    total = 0
    tmp_total = 0
    # for each_string in file:
    #     print(each_string)
    for each_letter in string:
        #print(each_letter)
        times17 = (total+ascii[each_letter]) *17
        tmp_total = times17 % 256
        #print("total, tmp_total, times17",total, tmp_total, times17)
        total =tmp_total
    return total
total_1 = 0
for string in tqdm.tqdm(file):
    #print(string)
    tmp = find_total(string)
    total_1+=tmp
print("part one answer: ", total_1)