def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
res=fact(6)
print(res)