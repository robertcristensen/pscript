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

def encode_morze(str_in):
    signal_dic = {"-":"^^^",".":"^"}
    signal_code = {}
    signal = ""
    for mcode_index in morse_code:
        for mel in morse_code[mcode_index]:
            signal += signal_dic[mel]+"_"
        signal_code[mcode_index]=signal[:-1]    
        signal =""    
    str_morze = ""
    str_out = ""
    encoded_word = ""
    str_in = str(str_in)
    str_in = str_in.upper().split(" ")
    for word in str_in:
        for letter in word:
            if letter in signal_code.keys():
                encoded_word += signal_code[letter]+"___"
        str_morze += encoded_word[:-3]   
        if encoded_word: str_morze +="_______" 
        encoded_word = "" 
    str_out = str_morze[:-7]       
    return str_out
    
print(encode_morze(str(1)))    
    
    
    
    
    