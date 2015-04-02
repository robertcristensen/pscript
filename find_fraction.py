def  find_fraction(summ):
    max = (0,0)
    if summ%2 == 0 and summ: ch = int(summ/2) - 1
    else: ch = int(summ/2)         
    zn = summ - ch
    while ch:
        nsd = 1
        for i in range(2, int(ch/2) + 1):
            if ch%i == 0 and zn%i == 0: nsd = i
        if nsd == 1: 
            max = (ch,zn)
            ch = 1    
        ch-=1
        zn+=1
    if max[1] == 0: return False
    else: return max    

def bouquets(narcissus_price, tulip_price, rose_price, summ):
    count = 0
    n = t = r = 0
    max_iter = int(summ / min(narcissus_price, tulip_price, rose_price))
    max_n = int(summ/narcissus_price)
    max_t = int(summ/tulip_price)
    max_r = int(summ/rose_price)
    for n in range(max_n+1):
        for t in range(max_t+1):
            if (n+t)%2 == 0: range_r = range(1,max_r+1,2)
            else: range_r = range(0,max_r+1,2)
            for r in range_r:
                if (n*narcissus_price + t*tulip_price + r*rose_price) <= summ and (n+t+r)%2 != 0: count +=1   
    return count      
    
#print(bouquets(10,199,99,20000))     
print(bouquets(22,44,150,20000))    