# """
# #match_case also know as switch statement in other languages 
# #syntax= match__:
#             case 'condition':
#             print(")
#             #can be multiple cases
#             case_: the deafault case 
#                 print("if all case false show this")
# """

a = int(input("enter a number b/w 1-9:"))
match a:
    case 1:
        print("you are lucky")
    case 2:
        print("you are not lucky")
    case 4:
        print("you are  very lucky")
    case _:
        print("better luck next time")
