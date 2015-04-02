conf = {
'exam_max': 30, # кількість балів, доступна за здачу екзамена
'lab_max': 7, # кількість балів, доступна за виконання 1 практичної роботи
'lab_num': 10, # кількість практичних робіт в курсі
'k': 0.61, # частка балів від максимума, яку необхідно набрати для отримання сертифікату
}.


class Student:
    def __init__(self, name, conf):
        self.labs={}
        for i in range(0,conf['lab_num']):
            self.labs[i]=0        
        self.exam=0
        self.conf=conf
        self.name=name
        
    def make_lab(self, m, n=None):
        i=0
        if n==None:
            while self.labs[i] and i < self.conf['lab_num'] - 1:                
                i+=1
            if m <= self.conf['lab_max'] and i < self.conf['lab_num']:
                self.labs[i]=m
            else:
                if i < self.conf['lab_num']: self.labs[i]=self.conf['lab_max']                
        else: 
            try:
                if m <= self.conf['lab_max'] and n < self.conf['lab_num']:
                    self.labs[n]=m
                else:
                    if n < self.conf['lab_num']: self.labs[n]=self.conf['lab_max']  
            except KeyError:
                pass
        return self
        
    def make_exam(self, m):
        if m <= self.conf['exam_max']:
            self.exam = m
        else:
            self.exam = self.conf['exam_max']
        return self   
        
    def is_certified(self):
        sum_max=sum=0
        flag = False
        for i in range(0,self.conf['lab_num']):
            sum_max+=self.conf['lab_max']
        sum_max+=self.conf['exam_max'] 
        for i in range(0,self.conf['lab_num']):
            sum+=self.labs[i]
        sum+=self.exam
        if sum >= sum_max*self.conf['k']:
            flag = True
        return (sum, flag)    