import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
N = 0

def add_zero(str_in):
    str_in=str_in[::-1]
    if len(str_in) < 6: 
        for i in range(len(str_in),6):
            str_in = str_in + "0"
    res = str_in[::-1]
    return res

def is_lucky(str):
    if int(str[0]) + int(str[1]) + int(str[2]) == int(str[3]) + int(str[4]) + int(str[5]):
        return "TRUE"
    else: return "FALSE"

while x <= y:
    if is_lucky(add_zero(str(x))) == "TRUE":
        N+=1
    x+=1

print(N)
