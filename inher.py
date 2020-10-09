from classes import First
class Second(First):
    b="Hello"
    c=3
    d=5
    def __init__(self,d,e):
        self.definition=d
        self.explanation=e
        First.__init__(self,self.definition,self.explanation)


    def secondFunc(self):
        print('Second Func Called')



sec=Second(1,1)
print(f'I am from first a {sec.a}')
sec.total_sum(3)
print(sec.f1)
print(sec.f2)