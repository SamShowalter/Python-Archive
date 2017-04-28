n = int(input().strip())
alist = [int(num) for num in input().strip().split(" ")]

def insertionSort(alist):
   for index in range(1,len(alist)):
       currentvalue = alist[index]
        position = index
        while position>0 and alist[position-1]>currentvalue:
              alist[position]=alist[position-1]
              print(*alist, sep = ' ')
              position = position-1

          alist[position]=currentvalue

insertionSort(alist)
print(*alist, sep = ' ')
