
n = int(input().strip())
s= input().strip()

level = 0
valley = 0

for i in range(len(s)):
    if s[i] == "U":
        level += 1
        status = "up"
    else:
        level -= 1
        status = "down"
    if level == 0 and status == "up":
        valley += 1

print(valley)
