with open('day6_input.txt') as f:
    file = [i.rstrip("\n") for i in f]

clean_file= [i.split(':') for i in file  ]
# time_tmp = [i.strip() for i in clean_file[0]][1].split('  ')  ########for test data
# distance_tmp= [i.strip() for i in clean_file[1]][1].split('  ') ###########for test data
time_tmp = [i.strip() for i in clean_file[0]][1].split('   ')
distance_tmp= [i.strip() for i in clean_file[1]][1].split('   ')

times = [int(i) for i in time_tmp]
records  = [int(i) for i in distance_tmp]
simulated = []
for time in times:
    each_game = []
    for ind in range(time):
        time_charged = ind 
        time_left = time- time_charged
        speed = time_charged * time_left
        distance_travelled = time_charged * time_left
        each_game.append(distance_travelled)
    simulated.append(each_game)

wins = 1

for round, each in enumerate(simulated):
    #wins = [i for i in each for record in records in [f(i)]if i > record]
    
    wins_each_round = 0
    for i in each: 
        if i > records[round] :
            wins_each_round+=1
    wins = wins * wins_each_round

print("part one answer:", wins)


########################part 2#############################
print(clean_file)

record_time = int(clean_file[0][1].replace(' ',''))


record_distance= int(clean_file[1][1].replace(' ',''))

# reversed = range(record_time, -1,-1)
# losses_left = 0
# for ind in reversed:
#     if (record_time * ind)-ind < record_distance:
#         losses_left  = (record_time  - ind) +1
#         break


for index in range(record_time):

    if ( record_time- index) * index  < record_distance: 
        losses_right = index
    else:
        break

print("part two answer",(record_time - (losses_right *2) )-1)