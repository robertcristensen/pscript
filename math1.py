import sys, math

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

verse = "la"+"-la"*(x-1)
song = (verse + " ")*y
song = song.strip()
coda = "!"*z + (".")*(z-1)**2

res = "Everybody sing a song:"+song+coda
 
print(res)