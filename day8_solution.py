import re
import collections
from math import lcm
with open('day8_input.txt') as f:
    file = [i.rstrip('\n') for i in f]

#print(file)
node_dict = {}

for ind, node in enumerate(file[2:]):
   result = re.split(r"(\b[A-Z0-9]+\b).+(\b[A-Z0-9]+\b).+(\b[A-Z0-9]+\b).", node)
   
   #print("result",result)
   node_dict[result[1]] =  [result[2], result[3]]

instructions = collections.deque(file[0])
steps = 0

current = 'AAA'
def findend(current, instruction):
    if instruction == 'L':
        current = node_dict[current][0]

    else:
        current = node_dict[current][1]
    return current
 
def give_instructions ( instructions ):
    instruction = instructions.popleft()
    instructions.append(instruction)
    return instruction

def count_steps(current,end):
    steps = 0
    while current not in end:
        instruction = give_instructions(instructions)
        current = findend(current, instruction)
        #print(instruction, current)
        steps+=1
    return steps
    
print("part one answer: ", count_steps('AAA',['ZZZ']))
current = '11A'


starts = []
ends = []
        
for  node, value in node_dict.items():
    if node[2] =='A':
        starts.append(node)
    if node[2] == 'Z':
        ends.append(node)


print('')
print('')
counts = []
current = starts[5][1]
sEt = set()

total = 1
for i in starts:
    counts.append(count_steps(i,ends))
for i in counts:
    tmp = i/293
    total =tmp * total

print(total *293)


print("part two answer: ",lcm(*counts))

