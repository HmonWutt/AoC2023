import re
with open('day7_input.txt') as f:
    file= [i.rstrip('\n') for i in f]
hand_strength_score = []
label_strength = {'A':13,'K':12, 'Q':11, 'J':10, 'T':9,'9':8, '8':7, '7':6, '6': 5, '5':4, '4':3, '3':2,'2':1}

for i in file:
    [hand,score] = i.split(' ')
    count = 0
    #print(hand)
    strength_list =[]
    checked =[]
    for j in hand:
        
        
        if count == 5:
            strength_list.append(count)
            break

        elif j in checked:
            continue
        else:
            count = hand.count(j)
        checked.append(j)
        strength_list.append(count)
        #print("count, to be counted, hand",count,j,hand)
    #print("strength_list",strength_list)
        
        
    
    #add_strength = [ hand, score, max(strength_list)]
    strength_list.sort(reverse= True )

    tmp = [hand,score, strength_list]

    hand_strength_score.append(tmp)

            
###########################################################################
def compare_labels (hand1, hand2):

    for i in range(6):
       
        hand1_current = hand1[0][i]
        hand2_current = hand2[0][i]

        if label_strength[hand1_current] < label_strength[hand2_current]:
            
            return hand1
        elif label_strength[hand1_current] > label_strength[hand2_current]:

            return hand2
        else:
            continue
   


def compare_scores (hand1, hand2):
    if len(hand1[2]) > len(hand2[2]):
        length = len(hand2[2])+1
    else:
        length = len(hand1[2])+1

    for i in range(length):
       
        hand1_current = hand1[2][i]
        hand2_current = hand2[2][i]
        #print(hand1_current, hand2_current, hand1,hand2)
        
        if hand1_current < hand2_current:
            #print("winner", hand1)
            
            return hand1
        elif hand1_current > hand2_current:
            #print("winner" , hand2)
            return hand2
        else:
            continue



def order_by_score(list):
    ordered_list = []
    while list:
        reference = list[0]
        for i in list:
            if i == reference:
                continue
            elif i[2] == reference[2]:
                reference = compare_labels(i,reference)   
            else:
                reference = compare_scores(i,reference)        
        list.remove(reference)
        ordered_list.append(reference)
    return ordered_list

ordered_by_score = order_by_score(hand_strength_score)

print("ordered list", ordered_by_score)

total_1 = 0
for ind,i in enumerate(ordered_by_score):
    
    rank= ind+1
    score = int(i[1])
    total_1+= rank*score


print("total",total_1)



