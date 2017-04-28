
#!/bin/python3

import sys

#Pretty crazy one liner
print(2**((bin(int(input()))).lstrip('0b').count('0')))

