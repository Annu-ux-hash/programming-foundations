s = "hello world" # Strings are immutable
print(s)
# s[0] = "R" # You cannot do this

# python provide built in methods  to manipulate string 

# a = len(s)
# print(a)
# print(s.upper()) #change lower to uper 
# print(s.lower()) # to lower
# print(s.capitalize()) # 1st letter capital
# print(s.title()) # every word 1st letter is capital


text = " \nhello world " 
print(text.strip()) # Output: "hello world" # remove all escape sequence and space 
print(text.lstrip()) # Output: "hello world "
print(text.rstrip()) # Output: " hello world"