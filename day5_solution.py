import re
with open ('day5_input.txt') as f:
   
   file = [i.rstrip('\n') for i in f]

new_file = []
tmp=[]
to_match = file[1]
for i in file[2:]:
    if i!= to_match:
       tmp.append(i) 
    else:
       new_file+=[tmp]
       tmp=[]

#new_file.append(file[-3:])########add the last item ########
print("new_file",new_file,"new")

dict ={}
dict_keys = []
dict_values = []


seeds_to_be_planted_1 = file[0].split(':')[1].strip()
seeds_to_be_planted = [int(seed) for seed in seeds_to_be_planted_1.split(' ')]

print("seeds", seeds_to_be_planted)



def map(seed_to_plant, seed_soil_range_list):
    soil_position = seed_to_plant
    for each in seed_soil_range_list:

        [soil,seed, ranges] = each.split(' ')
        #print("range", ranges, "seed",seed, "soil", soil)
        bound = int(ranges)
        start = int(seed)
        end = int(seed) +bound
        #print("start",start, "end", end)
        if start <= seed_to_plant  <= end: 
            
            #soil_index = seed_to_plant  - int(seed)
            #print(seed_to_plant, seed, soil, bound, start,end)
            soil_index =   seed_to_plant - start
            #print("witin range", soil_index)
            soil_position = int(soil) + soil_index
            break
    
    return soil_position
        
seed_soil = new_file[0][1:]
seed_to_soil = []
for i in seeds_to_be_planted:
    seed_to_soil.append(map(i,seed_soil))

print("seed to soil", seed_to_soil)
soil_fertilizer = new_file[1][1:]
soil_to_fertilizer = []
for i in seed_to_soil:
    soil_to_fertilizer.append(map(i,soil_fertilizer))
print("soil to fertilizer", soil_to_fertilizer)

fertilizer_water = new_file[2][1:]

fertilizer_to_water = []
for i in soil_to_fertilizer:
    fertilizer_to_water.append(map(i,fertilizer_water))

print("fert to water", fertilizer_to_water)

water_light = new_file[3][1:]
water_to_light = []
for i in fertilizer_to_water:
    water_to_light.append(map(i,water_light))
print("water to light", water_to_light)

light_temp = new_file[4][1:]
light_to_temp = []
for i in water_to_light:
    light_to_temp.append(map(i, light_temp))


temp_humidity = new_file[5][1:]
temp_to_humidity =[] 
for i in light_to_temp:
    temp_to_humidity.append(map(i, temp_humidity))

humidity_location = new_file[6][1:]
humidity_to_location = [] 
for i in temp_to_humidity:
    humidity_to_location.append(map(i, humidity_location))
print("part one answer",min(humidity_to_location))