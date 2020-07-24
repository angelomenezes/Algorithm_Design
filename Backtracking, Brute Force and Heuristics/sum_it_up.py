# Aluno: Angelo Garangau Menezes
# NUSP: 11413492

import ast

def find_sums(current_index, current_sum, integer_list):

    if current_sum == total_sum:
        solutions[str(integer_list)] = True
        return
    
    if current_sum > total_sum or current_index == n_integers: return
    
    for i in range(current_index, n_integers):
        integer_list.append(input_set[i])
        find_sums(i+1, current_sum + input_set[i], integer_list)
        integer_list.pop()

if __name__ == "__main__":
    
    while True:

        input_set = input().split()
        total_sum = int(input_set[0])
        n_integers = int(input_set[1])
        
        if total_sum == 0 and n_integers == 0:
            break
        else:
            input_set = [int(input_set[i]) for i in range(2, len(input_set))]
            input_set.sort(reverse=True)
            solutions = {}
            
            find_sums(0,0,[])
            print('Sums of {}:'.format(total_sum))
            if solutions:
                for key in solutions.keys():
                    solution = ast.literal_eval(key)
                    print(*solution, sep='+')
            else:
                print('NONE')             
            