import re
from collections import Counter
file = open('day2_input.txt','r')
#file = open('test.txt','r')
fileSplitOnNewline = file.read().strip().split('\n')
fileSplitOnGameID = [i.split(':') for i in fileSplitOnNewline] 

fileIsolatedGameID = [{int(i[0].split(' ')[1]):i[1].split(';')} for i in fileSplitOnGameID]


def count(string):
    red = 0
    green=0
    blue=0
    if re.search('red', string):
        m = re.search('red', string)
        red += int(string[1:m.start()-1])
    elif re.search('green', string):
        m = re.search('green', string)
        green += int(string[1:m.start()-1])
 
    else:
        m = re.search('blue', string)
        blue+=int(string[1:m.start()-1])
   
    return red,green,blue
  

total = 0
games = set()
for i in fileIsolatedGameID:
    for game,rounds in i.items(): 
        for number, round in enumerate(rounds):
            tmp = round.split(',')
            #print(game, number,tmp)
            red = 0 
            green = 0
            blue = 0  
            total_red = 0
            total_green = 0
            total_blue = 0
            for each_color in tmp:
                
                red,green,blue = count(each_color)
                total_red+=red
                total_green+=green
                total_blue +=blue
            if total_red > 12 or total_green > 13 or total_blue > 14:
                #print("rejected:", "red:", total_red, "green:", total_green, "blue:", total_blue)
                games.add(game)
            
            else:
                #print("passed:", "red:", total_red, "green:", total_green, "blue:", total_blue)
                pass
                
allgames = set()
for i in range(1,len(fileIsolatedGameID)+1):
    allgames.add(i)

difference = allgames.difference(games)
for i in difference:
    total+=i
print(total)
##################################part 2#############################
part_2_total = 0
for i in fileIsolatedGameID: 
    game_total = 0
    for game,rounds in i.items(): 
       
        total_red = []
        total_green = []
        total_blue = []
        for number, round in enumerate(rounds):
            tmp = round.split(',')
            #print(game, number,tmp)
            red = 0 
            green = 0
            blue = 0  
           
            for each_color in tmp:
                red,green,blue = count(each_color)
                total_red.append(red)
                total_green.append(green)
                total_blue.append(blue)
        game_total = (max(total_red) * max(total_green)* max(total_blue))
        
        part_2_total +=game_total
print(part_2_total)