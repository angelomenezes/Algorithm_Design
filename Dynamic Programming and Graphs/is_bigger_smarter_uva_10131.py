class elephant:
    def __init__(self, weight, iq):
        self.weight = weight
        self.iq = iq
    def __lt__(self, other): # For sorting based on IQ
        return self.iq > other.iq
    def __eq__(self, other): # For removing duplicates with "hash and set"
        return self.weight == other.weight and self.iq == other.iq
    def __hash__(self):
        return hash(('weight', self.weight,'iq', self.iq))

def get_longest_sequence(elephants):
    # Sorting and getting rid of repeated elements
    sorted_elephants = sorted(list(set(elephants)))
   
    n_of_elephants = len(sorted_elephants)
    lis = [1] * n_of_elephants

    #for i, elephant in enumerate(sorted_elephants):
    #    print('{} {} {}'.format(i+1, elephant.weight, elephant.iq))

    for i in range(1, n_of_elephants):
        for j in range(0, i):
            if sorted_elephants[i].weight > sorted_elephants[j].weight and sorted_elephants[i].iq < sorted_elephants[j].iq and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
    
    maximum = 0
    for i in range(n_of_elephants):
        maximum = max(maximum, lis[i])

    print(maximum)
    
    # Get sequence index on sorted list
    temp = maximum
    
    # Checking consistency of data
    last_iq = -1
    last_weight = 10001

    indexes = []

    for i in range(n_of_elephants-1, -1, -1):
        if lis[i] == temp:
            if sorted_elephants[i].iq > last_iq and sorted_elephants[i].weight < last_weight:
                indexes.append(i)
                temp -= 1
                last_iq, last_weight = sorted_elephants[i].iq, sorted_elephants[i].weight
    
    indexes = sorted(indexes)

    # For displaying indexes based on original sequence
    for i in indexes:
        j = elephants.index(sorted_elephants[i])
        print(j+1)
        #print('{} {}'.format(elephants[j].weight, elephants[j].iq))


if __name__ == "__main__":

    elephant_list = []
    try:
        while True:
            weight, iq = map(int, input().split())
            elephant_list.append(elephant(weight, iq))
    except:
        pass

    get_longest_sequence(elephant_list)

