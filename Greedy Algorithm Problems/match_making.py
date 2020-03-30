from bisect import bisect_left

def get_closest(myList, item): # Binary search in a sorted list
    
    pos = bisect_left(myList, item)
    
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    
    before = myList[pos - 1]
    after = myList[pos]
    
    if after - item < item - before:
       return after
    else:
       return before

def match_making(n_bachelor, n_spinster, bachelor_ages, spinster_ages):

    # Sorting arrays only once

    bachelor_ages.sort() 
    spinster_ages.sort()
    
    while len(bachelor_ages) != 0 and len(spinster_ages) != 0:

        match = bachelor_ages.pop()
        spinster_ages.remove(get_closest(spinster_ages, match))
    
    if len(bachelor_ages) == 0:
        return 0, 0
    
    return len(bachelor_ages), bachelor_ages.pop(0)

if __name__ == "__main__":
    
    end_reached = False
    case = 0

    while not end_reached:
        case += 1
        input_set = input().split()
        n_bachelor = int(input_set[0])
        n_spinster = int(input_set[1])

        if n_bachelor == 0 and n_spinster == 0:
            end_reached = True
        else:
            bachelor_ages = [0]*n_bachelor
            spinster_ages = [0]*n_spinster
            
            for i in range(n_bachelor):
                bachelor_ages[i] = int(input()) 

            for i in range(n_spinster):
                spinster_ages[i] = int(input())

            left_bachelors, age_of_bachelor = match_making(n_bachelor, n_spinster, bachelor_ages, spinster_ages) 
            
            if left_bachelors == 0:
                print(f'Case {case}: {left_bachelors}')
            else:
                print(f'Case {case}: {left_bachelors} {age_of_bachelor}')