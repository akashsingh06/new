class abc:
    def __init__(self,var):
        self.var=var
    def __display(self):
        print(self.var)
    def add(self):
        self.var+=2
        self.display()
obj=abc(10)
obj._abc._display()        
