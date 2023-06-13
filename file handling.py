# file creation
# 1)file opening

# file=open("demo.txt",'w')
# file.close()

# 2) file reading

file=open("demo.txt",'r')
read=file.read()
print(read)
file.close()

# for read  line
# file=open("demo.txt",'r')
# read=file.read(30)
# print(read)
# file.close()

# # for read value
# file=open("demo.txt",'r')
# read=file.readline(50)
# print(read)
# file.close()


# 3)file writing
# file=open("demo.txt",'w')
# file.write("my namee is khann")
# file.close()

# 4)append
file=open("demo.txt",'a')
file.write("/my namee is anandhan")
file.close()