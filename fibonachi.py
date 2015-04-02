import sys

n = int(sys.argv[1])

f1 = 0
f2 = 1
curr = f1

if n > 0:
    for i in range(n):    
        f1 = f2
        f2 = curr
        curr = f1+f2
		
print(curr) 