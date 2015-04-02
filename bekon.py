import sys

str_in = sys.argv[1].replace(' ','')
str_curr=''
str_out=''

N = len(str_in)-len(str_in)%5

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'


for i in range(0,N):
    if str_in[i].isupper(): str_curr += 'b'
    else: str_curr += 'a'
    if len(str_curr.replace(' ',''))%5 == 0: str_curr += ' '

str_curr = str_curr.strip()
str_curr = str_curr.split(' ')

for i in range(0, len(str_curr)):
    str_out+=alphabet[key.find(str_curr[i])]

print(str_out)
