
inpt = int(input().strip())

def viral(days):
    day = 1
    count = 5
    vsum = 2
    if days == 1:
        return vsum
    else:
        while day < days:
            count = ((count//2)*3)
            vsum += (count//2)
            day += 1
    return vsum

print(viral(inpt))
        
        
