
s = input().strip().replace(" ","")
ref = "abcdefghijklmnopqrstuvwxyz"
result = ""
answer = ""

for i in range(len(s)):
    if s[i].lower() not in result:
            result += (s[i].lower())
        
result = ''.join(sorted(result))

if result == ref:
    print("pangram")
else:
    print("not pangram")
