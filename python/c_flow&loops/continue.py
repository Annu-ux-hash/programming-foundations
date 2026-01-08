i = 1
for i in range (0,21):
    if i % 2 != 0: # # i is divide by 2 then remainder  is not equal to zero = even (telling to skip odd no.)
        continue
    print(i)
    #output : 0 2 4 6 8 10 12 14 16 18 20

# i = 1 
# for i in range (0,21):
#     if i % 2 == 0: # i is divide by 2 then remainder is equal to zero = even (telling to skip even no.)
#         continue
#     print(i)
#  #output = 1 3 5 7 9 11 13 15 17 19

'''
#it is used when a statement is syntactically required, but you don’t want to write logic yet.
pass : do nothing if want to write logic later you can 
'''
i = 1 
for i in range(2,10):
    if i == 2:
        pass
    print(i)