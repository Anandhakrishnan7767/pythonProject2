class add:
    def __int__(self,  x, y):
        self.x = x
        self.y = y
    def __add__(self , adding):
        x = self.x+adding.x
        y = self.y+adding.y
        return add(x, y)
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
p1=add(1, 4)
p2=add(2, 4)
print(p1,p2)