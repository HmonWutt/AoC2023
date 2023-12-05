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

new_file.append(file[-3:])########add the last item ########

dict ={}
dict_keys = []
dict_values = []
seed_list = []
soil_list = []
def map(new_file):
    seed_list = []
    soil_list =[]
    for  map in new_file:
        if len(map.split(' ')) >0:
            ranges = int(map.split(' ')[2]) 
            soil=  int(map.split(' ')[0])
            seed = int(map.split(' ')[1])
            seeds = []
            soils = []

            for i in range(ranges):
                seed_add = seed+i
                seeds.append(seed_add)
                soil_add = soil+i
                soils.append(soil_add)
            seed_list+=seeds
            soil_list+=soils
    return seed_list, soil_list
seed_list,soil_list = map(new_file[0][1:])

def linkmaps(list1, list2):
    linkedmap = {}
    for ind, i in enumerate(list1):
        
        linkedmap[i] = list2[ind]
    return linkedmap

seed_to_soil = linkmaps(seed_list,soil_list)
print(seed_to_soil)

soil_list_2, fertilizer_list = map(new_file[1][1:])

soil_to_fertilizer = linkmaps(soil_list_2, fertilizer_list )

fertilizer_list_2, water_list = map(new_file[2][1:])

fertilizer_to_water = linkmaps(fertilizer_list_2,water_list)

water_list_2, light_list = map(new_file[3][1:])
water_to_light = linkmaps(water_list_2, light_list)

light_list_2, temperature_list = map(new_file[4][1:])

light_to_temperature = linkmaps(light_list_2, temperature_list)

temperature_list_2, humidity_list = map(new_file[5][1:])

temperature_to_humidity = linkmaps(temperature_list_2, humidity_list)

humidity_list_2, location_list = map(new_file[6][1:])
humidity_to_location = linkmaps(humidity_list_2, location_list)
      
seeds_to_be_planted = file[0].split(':')[1].strip()
seeds_to_be_planted = [int(seed) for seed in seeds_to_be_planted.split(' ')]

seed_to_be_planted_and_corresponding_soil = {}


def matched_output(list,dict):
    matched_output_dict = {}
    matched_output_list = []
    for i in list:
    
        if i in dict:
            matched_output_list.append(dict[i])
            matched_output_dict[i] = dict[i]
            #print("match found", i ,dict[i] )
        else:
            matched_output_list.append(i)
            matched_output_dict[i]= i
            #print("match not found", i , i )
    #print(matched_output_dict)
    return matched_output_list

seed_to_match_to_soil = matched_output(seeds_to_be_planted, seed_to_soil)

soil_to_match_to_fertilizer = matched_output(seed_to_match_to_soil,soil_to_fertilizer)

fertilizer_to_match_to_water= matched_output(soil_to_match_to_fertilizer, fertilizer_to_water)
water_to_match_to_light =  matched_output(fertilizer_to_match_to_water, water_to_light)
light_to_match_to_temperature = matched_output(water_to_match_to_light, light_to_temperature)
temperature_to_match_to_humidity = matched_output(light_to_match_to_temperature, temperature_to_humidity)
humidity_to_match_to_location = matched_output(temperature_to_match_to_humidity, humidity_to_location)



print(min(humidity_to_match_to_location))
