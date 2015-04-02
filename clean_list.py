def file_search(folder, filename):
    if isinstance(folder,list):
        if filename in folder:
            return folder[0]+'/'+filename            
    else: return False    
    path = ''
    for sub_folder in folder:
        if file_search(sub_folder, filename):
            path += folder[0]+'/'+file_search(sub_folder, filename)
    if path == '': return False
    else: return path
    

      
   
print(file_search(['C:', 'backup.log', ['newfolder']],'ideas.txt'))
#print(file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py'))
    
def super_fibonacci(n, m):
    lstm=[]
    for i in range(m): 
        lstm.append(1)
    summ = 0
    if n>m:
        for j in range(n-m):
            for i in range(m):
                summ+=lstm[m-i-1]
            del lstm[0]
            lstm.append(summ)
            summ=0
    else:
        return 1
    return lstm[m-1]
           
#print(super_fibonacci(9,3))

def clean_list(lst):
    i=j=0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            if type(lst[i]) == type(lst[j]) and lst[i] == lst[j]:
                lst.pop(j)
                j-=1
            j+=1
        i+=1
    return lst
                
#res = clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5])
#res = clean_list([])
#print(res)

def counter(a,b):
    a=str(a)
    b=str(b)
    count=0
    nums=range(0,10)
    for i in nums: 
        i = str(i)
        if (i in b) and (i in a):
            count+=1
    return count
    
#print(counter(123, 45))