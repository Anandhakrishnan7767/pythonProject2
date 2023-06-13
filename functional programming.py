a=int(input("enter  the no"))
# b=int(input('enter the no'))
# c=int(input("enter the no"))
# def addition(a,b):
#     return(a+b)
# def sqr(c):
#     return c*c
#
#
# result=sqr(addition(a,b))
# print(result)

# lambda

# x=lambda a,b,c:a+30+b+c
# print(x(7,7,4))

# using if function

def fun(a):
    return lambda b:a*b
print()
x=fun(a)
print(x(4))
