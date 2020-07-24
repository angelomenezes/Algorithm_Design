import time 

# O(n²)
def count_inversions(vector):
    counter = 0
    for i in range(len(vector)):
        for j in range(i+1, len(vector)):
            if vector[i] > vector[j]: 
                counter += 1
    return counter

# O(n log n)
def merge_sort(array):
    if len(array) < 2:
        return array, 0
    m = len(array) // 2
    left, inv_count_left = merge_sort(array[:m])
    right, inv_count_right = merge_sort(array[m:])
    array_sorted, inv_count = merge(left, right)
    inv_count += (inv_count_left + inv_count_right)
    return array_sorted, inv_count

def merge(left, right):
    result = []
    i, j, inv_count = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        elif right[j] < left[i]:
            result.append(right[j])
            j += 1
            inv_count += len(left) - i
    result += left[i:]
    result += right[j:]
    return result, inv_count

if __name__ == "__main__":

    n_of_cases = int(input())
    #start = time.time()    

    for _ in range(n_of_cases):

        n_of_elements = int(input())

        array = input().split()
        array = [int(item) for item in array]

        _, inv_count = merge_sort(array)
        print('Output: {}'.format(inv_count))
    #stop = time.time()
    #print('Execution time: {:.2f}'.format(stop-start))