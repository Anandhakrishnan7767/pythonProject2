# w=int(input("enter the weight (kg) "))
# h=int(input("enter the height (m)"))
# def bmi(w,h):
#     print(w/(h)**2)
# bmi(w,h)


# using float
# def bmi(w,h):
#     print(w/(h)**2)
# w=float(input("enter your weight"))
# h=float(input("enter your height"))
# bmi(w,h)

# using return
def bmi(w,h):
    return (w/(h)**2)
w=float(input("enter weight"))
h=float(input("enter height"))
print(w/(h)**2)