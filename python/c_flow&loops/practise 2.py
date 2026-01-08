#Python Conditionals & Loops - Practice Set

#Q1 
'''
a = int(input("enter a number: "))
if(a==0):
    print("zero")
elif(a>0):
    print("positive")
elif(a<0):
    print("negative")

#Q2

age = int(input("age:- "))
if(age>18):
    print("you are elgible for vote")
elif(age==18):
    print("you have your voter ID")
else:
    print("you are not elgible")
    
 #Q3

n = int(input("Enter a Number: "))
if(n %2 == 0):
    print("even")
if(n %2 != 0):
    print("odd")

#Q4

day = int(input("enter a day number (1–7): "))
match day:
    case 1:
        print("monday")
    case 2:
        print("tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thrusday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("wrong no.")
'''
#Q5 

# a = int(input("enter a 1st no.: "))
# c = input("operator (+,-,*,/)")
# b = int(input("enter a 2nd no.: "))
# match c:
#     case '+':
#         print(a+b)
#     case '-':
#         print(a-b)
#     case '*':
#         print(a*b)
#     case '/':
#         print(a/b)
#     case _:
#         print("error")

#Q6

# i = 1
# for i in range(1,11):
#     print(i)

# #Q7
# a = 2
# for a in range(1,11):
#      print("100 X",a,"=",a*100)


# a = 1
# n = int(input("enter a number: "))
# for a in range(1,11):
#      print(n*a)  

# a = 1
# n = int(input("enter a number: "))
# for a in range(1,11):
#      if n >=50:
#          break
#      print(n*a)

# total = 0
# for i in range(0,101):
#      total = total+i
#      print(total)


#Q8

star ="*"
for i in range(1,5):
    print("*"* i)
