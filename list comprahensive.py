# result=[]
# for i in "inmakes":
#     result.append(i)
# print(result)


# in list comprahensive

result=[i for i in "inmakes"]
print(result)


# old method
result=["python","inmakes","papaya","papa","peppepe"]
# new=[]
# for i in result:
#      if 'p' in i:
#          new.append(i)
# print(new)

# new method using list
new=[i for i in result if 'p'in i]
print(new)

# new=[ i for i in range(10)]
# print(new)

# new=[i.upper() for i in result]
# print(new)
# num=[1,2,3,4]
# nom=[i+i for i in num]
# print(nom)

# list formatting
