class First:
    a=200
    def __init__(self, c , d):
        self.f1=c
        self.f2=d
        


    def total_sum(self,b):
        print((First.a+b) *(self.f1+self.f2))


obj=First(1,3)
obj.total_sum(2)