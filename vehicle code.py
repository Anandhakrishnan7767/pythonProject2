class vehicle:
    def __int__(self,model):
        self.model=model
        self.car=car
        self.bike=bike
    def getspec(self):
        self.model=input('enter vehivcle model')
        self.car=input('car name')
    def getspecb(self):
        self.model=input('enter vehivcle model')
        self.bike=input('bike name')
    def displayspecveh(self):
        print(self.car,self.bike,self.model)
class car(vehicle):
    def getspeccar(self):
        self.model=input('model')
        self.year=input('year')
        self.spec=input('color')

    def  displayspec(self):
        print(self.model ,self.year,self.spec)
        print('abs,ac,5 seaing,air bags')
class bike(vehicle):
    def getspecbike(self):
        self.model=input('enter model')
        self.year=input('year')
        self.spec=input('abs,rear wheal disk,navigatio')

    def displayspec(self):
        print(self.model,self.year,self.spec)
        print("abs,rear wheal disk,navigatio")



obj=car()
obj.getspec()
obj.getspeccar()
obj.displayspec()
# obj.display

obj=bike()
obj.getspecb()
obj.getspecbike()
obj.displayspec()
