
n = int(input().strip())

for a0 in range(n):
    x = ""
    s = input().strip()
    #Reverse the order of string s
    r = s[::-1]
    
    for i in range(1,len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
            x = "Not Funny"
    if x == "Not Funny":
        print(x)
    else:
        print("Funny")
        
    
