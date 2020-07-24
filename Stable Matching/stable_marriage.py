# Problem from: https://www.codechef.com/problems/STABLEMP

import numpy as np

def stable_matching(n_marriages, man_preference, woman_preference):
    available_man = [i+1 for i in range(n_marriages)]
    counter_proposals = [0]*n_marriages
    husbands = [0]*n_marriages
    wives = [0]*n_marriages

    while available_man:
        
        man = available_man.pop(0) # Get the lucky boy
        
        for i in range(counter_proposals[man-1], n_marriages): # Iterating from number of proposals and total of marriages

            woman = man_preference[man-1][i]
            counter_proposals[man-1] += 1

            if wives[woman-1] == 0: # If the woman was alone, she marries the guy
                wives[woman-1] = man
                husbands[man-1] = woman
                break
            
            else: # If she has someone, she evaluates her choices in life
                her_preference = list(woman_preference[woman-1])
                
                current_husband = wives[woman-1]

                # If she rather be with the new guy
                if her_preference.index(man) < her_preference.index(current_husband):
                 
                    wives[woman-1] = man
                    husbands[man-1] = woman
                    available_man.append(current_husband) # The current one gets back to the end of the line
                    counter_proposals[current_husband-1] = list(man_preference[current_husband-1]).index(woman) + 1 # We keep his proposal info based on his last wife
                    break
    
    for i in range(n_marriages):
        print(i+1, husbands[i])

if __name__ == '__main__':
    
    # Reading the input 

    n_test_cases = int(input())

    for _ in range(n_test_cases):

        n_marriages = int(input())
        woman_preference = []
        man_preference = []

        temp = []

        # Getting women preferences
        for _ in range(n_marriages):
            temp = input().split()
            for i in range(n_marriages):
                woman_preference.append(int(temp[i+1])) 
        
        woman_preference = np.reshape(np.array(woman_preference), [n_marriages,n_marriages])
        
        # Getting man preferences
        for _ in range(n_marriages):
            temp = input().split()
            for i in range(n_marriages):
                man_preference.append(int(temp[i+1]))
        
        man_preference = np.reshape(np.array(man_preference), [n_marriages,n_marriages])

        stable_matching(n_marriages, man_preference, woman_preference)