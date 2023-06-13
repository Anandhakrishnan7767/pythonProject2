class student:
    def __int__(self,mark,name):
        self.name=name
        self.mark=mark
    def getdetail(self):
        self.name=input('enter the name')
        self.mark=int(input('enter the mark'))
    def putd(self):
        print(self.mark,self.name)
class teacher(student):
    def display(self):
        print('verified')
# obj=student() //op:error
obj=teacher( )
obj.getdetail()
obj.putd()
obj.display()




