def scarecrow_number(field_spots, field):
    n_scarecrow = 0
    spots = 0

    while spots < field_spots: # If region is fertile, skip two fields
        if (field[spots] == '.'):
            n_scarecrow += 1
            spots += 2
        spots += 1

    return n_scarecrow 

if __name__ == "__main__":
    
    n_test_cases = int(input())

    for case in range(n_test_cases):
        
        field_spots = int(input())
        field = list(input())

        print(f'Case {case+1}: {scarecrow_number(field_spots, field)}')