with open('day7_input.txt') as f:
    file= [i.rstrip('\n') for i in f]
hand_strength_score = []
label_strength = {'A':13,'K':12, 'Q':11, 'J':10, 'T':9,'9':8, '8':7, '7':6, '6': 5, '5':4, '4':3, '3':2,'2':1}
label_strength_ = {'A':13,'K':12, 'Q':11, 'T':10,'9':9, '8':8, '7':7, '6': 6, '5':5, '4':4, '3':3,'2':2, 'J':1}


for i in file:
    [hand,score] = i.split(' ')
    count = 0
    #print(hand)
    strength_list =[]
    checked =[]
    for each_card in hand:   
        if count == 5:
            strength_list.append(count)
            break
        elif each_card in checked:
            continue
        else:
            count = hand.count(each_card)
        checked.append(each_card)
        strength_list.append(count)
    strength_list.sort(reverse= True )

    tmp = [hand,score, strength_list]
    hand_strength_score.append(tmp)

            
###########################################################################
def compare_labels (hand1, hand2,label_strength):

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
        length = len(hand2[2])
    else:
        length = len(hand1[2])

    for i in range(length+1):
       
        hand1_current = hand1[2][i]
        hand2_current = hand2[2][i]
        
        if hand1_current < hand2_current:
            #print("winner", hand1)
            return hand1
        elif hand1_current > hand2_current:
            #print("winner" , hand2)
            return hand2
        else:
            continue

def order_by_score(list,label_strength):
    ordered_list = []
    while list:
        reference = list[0]
        for i in list:
            if i == reference:
                continue
            elif i[2] == reference[2]:
                reference = compare_labels(i,reference, label_strength)   
            else:
                reference = compare_scores(i,reference)        
        list.remove(reference)
        ordered_list.append(reference)
    return ordered_list

ordered_by_score = order_by_score(hand_strength_score, label_strength)


def get_count(ordered_by_score):
    total_1 = 0
    for ind,i in enumerate(ordered_by_score):
        
        rank= ind+1
        score = int(i[1])
        total_1+= rank*score
    return total_1


print("part one total: ",get_count(ordered_by_score))

print("")
################################################## part two #######################################################


hand_strength_score_ = []
for each in file:
    hand_,score_ = each.split(' ')
    count_ = 0
    j_count = 0
    strength_list_ =[]
    checked_ =[]
    for card in hand_:   
        if hand_.count(card) == 5:
            strength_list_.append(hand_.count(card))
            break
        
        else:
            if card in checked_:
                continue
            elif card == 'J':
                j_count = hand_.count(card)
            else:
                count_= hand_.count(card)
                strength_list_.append(count_)
        checked_.append(card)
   
    if strength_list_[0] != 5 : 
        strength_list_.sort(reverse= True )
        max_of_strength = [strength_list_[0]+j_count]
        the_rest_of_strengths = strength_list_[1:] 
        strength_list_ = max_of_strength+ the_rest_of_strengths
        tmp_ = [hand_,score_, strength_list_]
        hand_strength_score_.append(tmp_)
    else:
        tmp_ = [hand_,score_, strength_list_]
        hand_strength_score_.append(tmp_)

ordered_by_score_ = order_by_score(hand_strength_score_, label_strength_)


print("part two total: ", get_count(ordered_by_score_))

