from random import choice

def make_sudoku(size):
    sudoku = []
    square = []
    numbers = []
    cube_nums = []
    cross_nums = []

    for t in range(1,size**2+1):
        numbers.append(t)
             
    for i in range(size**2):   
        for k in range(len(numbers)): cube_nums.append(numbers[k])
        while len(cube_nums)>0:
            cel_num = size**2 - len(cube_nums)
            for col in range(int(i%size), i, size):
                print(col)
            n = choice(cube_nums)
            square.append(n)
            cube_nums.remove(n)       
        sudoku.append(square)
        square = []    

    

    return sudoku    
      
   

print(make_sudoku(2))    