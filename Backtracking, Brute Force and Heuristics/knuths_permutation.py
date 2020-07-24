# Aluno: Angelo Garangau Menezes
# NUSP: 11413492

def generate_permutations(characters, begin_index, end_index):
    if begin_index == end_index:
        print(''.join(characters))
    else:
        for index in range(begin_index, end_index+1):
            characters[begin_index], characters[index] = characters[index], characters[begin_index]
            generate_permutations(characters, begin_index+1, end_index)
            characters[begin_index], characters[index] = characters[index], characters[begin_index]

if __name__ == "__main__":
    try:
        while True:
            sequence = input()
            if sequence == '':
                break
            else:
                generate_permutations(list(sequence)[::-1],0,len(sequence)-1)
                print(knuth_algorithm_l(sequence))
                print('')
    except EOFError:
        pass