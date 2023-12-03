import regex as re
file = open('day1_input.txt','r')

count = 0
for i in file.readlines():
    num = re.findall("\d+", i)
    num_list = "".join(num)
    first_plus_last_digit = int(num_list[0] +num_list[-1])
    count+= first_plus_last_digit
print("count1", count)

num_dict  = {'one':1,  'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
count2 = 0       
for i in file: 
    first = re.findall( "\d|one|two|three|four|five|six|seven|eight|nine", i, overlapped=True)[0]  
    if re.match(r"[A-Za-z]", first):
   
        first = str(num_dict[first])
    
    last = re.findall( "\d|one|two|three|four|five|six|seven|eight|nine", i, overlapped=True)[-1]
    if re.match(r"[A-Za-z]", last):
        last = str(num_dict[last])
    count2 += int(first+last)
   
print("count2",count2)