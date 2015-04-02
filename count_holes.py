morse_code = {
    "A" : ".-", 
    "B" : "-...", 
    "C" : "-.-.", 
    "D" : "-..", 
    "E" : ".", 
    "F" : "..-.", 
    "G" : "--.", 
    "H" : "....", 
    "I" : "..", 
    "J" : ".---", 
    "K" : "-.-", 
    "L" : ".-..", 
    "M" : "--", 
    "N" : "-.", 
    "O" : "---", 
    "P" : ".--.", 
    "Q" : "--.-", 
    "R" : ".-.", 
    "S" : "...", 
    "T" : "-", 
    "U" : "..-", 
    "V" : "...-", 
    "W" : ".--", 
    "X" : "-..-", 
    "Y" : "-.--", 
    "Z" : "--.."
}


def count_holes(n):
    holes={0:1,4:1,6:1,8:2,9:1}
    holes_count = 0
    try:
        int(n)
    except:
        return "ERROR"
    if type(n) == int or type(n) == str or type(n) == long:
        if int(n) < 0: n = n*-1
        n = str(int(n))
        for i in n:
            digit = int(i)
            if digit in holes.keys():
                holes_count += holes[digit]
        return holes_count        
    else:
        return "ERROR"

print(count_holes(69))    