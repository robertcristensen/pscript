class SuperStr(str):
    def __init__(self,instr):
        self.s=instr
    def is_repeatance(self,instr):
        if not type(instr)==str: return False
        elif not self.s: return False
        elif not instr: return False
        if len(self.s)%len(instr)==0:
            k = int(len(self.s)/len(instr))
            if instr*k == self.s:
                return True
        return False        
    
    def is_palindrom(self):
        if not type(self.s)==str: return False
        if self.s[::-1].lower() == self.s.lower():
            return True
        else: return False    
            