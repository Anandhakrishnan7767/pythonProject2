# using set

# a={1,4,3,2,5,66,77,55}
# b={6,7,8,9,77,33,44}
# print(a)
# print(b)
# a.add(33)
# print(a)
# print(a|b)
# print(a&b)
# print(a-b)
# print(b-a)

# using inheritence

class hospital:
    def __int__(self,adminname,docname,sisname,dept):
        self.adminname=adminname
        self.docname=docname
        self.sisname=sisname
        self.dept=dept
    def getd(self):
        self.adminname=input('enter  admin name')
        self.docname=input('enter doc name')
        self.sisname=input('enter sister name')
        self.dept=input('enter dept')
    def putd(self):
        print(self.adminname,self.docname,self.sisname,self.dept)
class department(hospital):
    def display(self):
        print('detail')
class patient(department):
    def __int__(self,patientname,age,num,disease):
        self.patientname=patientname
        self.age=age
        self.num=num
        self.disease=disease
    def putdet(self):
        self.patientname=input('patent name')
        self.age=int(input("enter age"))
        self.num=int(input("enter mobile no"))
        self.disease=input('enter disease')
    def getdet(self):
        print(self.patientname,self.disease,self.age,self.num)





obj=department()
obj.getd()
obj.putd()
obj.display()

obj=patient()
obj.putdet()
obj.getdet()