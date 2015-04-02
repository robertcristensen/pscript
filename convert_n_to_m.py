def convert_n_to_m(x, n, m):
    digits="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    if type(x) in [str,int,long]:
        pass
    else:
        return False
    x = str(x).upper()    
    if all([smb in digits for smb in x]):
        pass
    else:
        return False
    x_decim=0
    for i in range(len(x)):
        if int(digits.index(x[i])) < n: x_decim+=int(digits.index(x[i]))*(n**(len(x)-i-1))
        else: return False
    x_m = ""
    while x_decim >= m:
        x_m=digits[x_decim%m]+x_m
        if m==1: x_decim = x_decim - 1
        else: x_decim = int(x_decim/m)    
    if m != 1: x_m=digits[x_decim%m]+x_m 
    return x_m    


print(convert_n_to_m(777L, 10, 2))

