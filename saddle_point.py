def saddle_point(matrix):
    s_i = s_j = None
    i=j=0
    tr_matrix=[]
    tr_row=[]
    while i < len(matrix[0]):
        while j < len(matrix):
            tr_row.append(matrix[j][i])
            j+=1
        tr_matrix.append(tr_row)
        tr_row=[]
        i+=1
        j=0
    i=j=0
    while j < len(matrix):
        while i < len(matrix[0]):
            if matrix[j][i] == min(matrix[j]) and matrix[j].count(matrix[j][i]) == 1:
                if matrix[j][i] == max(tr_matrix[i]) and tr_matrix[i].count(matrix[j][i]):
                    s_i = i
                    s_j = j
            i+=1
        j+=1
        i=0
    if s_i == None and s_j == None: 
        return False
    else:    
        return (s_i, s_j) 
            
            
        
    


print(saddle_point([[5,5,5], [5,5,6], [5,4,5]]))    