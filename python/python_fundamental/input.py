#user input function = we take user input 

#syntax = varname = input("")
#inside (" what input you want from user write that for better looking code")

#vn = input(always string) you have to convert if you want perform any operation.

# two types of convertion method for input function 

# 1st old and time taking 
# a = input("enter 1st number: ")
# USING TYPECASTING 
# a = int(a)
#example =
a = input("enter 1st number: ")
a = int(a)
print(a)
print(type(a))

#2nd type
# syntax: varname = datatype(input("enter______"))

#example:
b = int(input("enter 2nd number: "))
print(b)
print(type(b))


# add two number : take user input 
num_1 = int(input("enter 1st number: "))
num_2 = int(input("enter second number: "))
#always use print when you want to perform operation
print(num_1 + num_2) 



