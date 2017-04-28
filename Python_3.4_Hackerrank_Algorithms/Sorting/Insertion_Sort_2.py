
n = int(input().strip())
sort = [int(num) for num in input().strip().split(' ')]

def insertionSort(sort):
    for i in range(1, len(sort)):
        temp = sort[i]
        j = i
        while j > 0 and temp < sort[j-1]:
            sort[j] = sort[j-1]
            j -= 1
        sort[j] = temp
        print(' '.join(str(num) for num in sort))

insertionSort(sort)
            
        
