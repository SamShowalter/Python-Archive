
#Lots and lots of inputs
list = [int(num) for num in input().strip().split(' ')]
food = [int(food) for food in input().strip().split(' ')]
bill = int(input().strip())

n = list[0]
gross = list[1]
                            
shePays = (sum(food) - food[gross])//2

if shePays == bill:
    print("Bon Appetit")
else:
    print(bill - shePays)
