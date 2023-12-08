import re
import sys
import collections
with open('day8_input.txt') as f:
    file = [i.rstrip('\n') for i in f]


node_dict = {}

for ind, node in enumerate(file[2:]):
   result = re.split(r"(\b[A-Z]+\b).+(\b[A-Z]+\b).+(\b[A-Z]+\b).", node)
   node_dict[result[1]] =  [result[2], result[3]]

instructions = collections.deque(file[0])
steps = 0

current = 'AAA'
while current != 'ZZZ':
   
    instruction = instructions.popleft()
  
    steps+=1
    if instruction == 'L':
        current = node_dict[current][0]
   
    else:
        current = node_dict[current][1]
   
    instructions.append(instruction)

print("part one answer: ",steps)
      