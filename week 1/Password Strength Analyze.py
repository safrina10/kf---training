a=input("enter your pass: ")

symbols ="!@#$%^"

digit_lower=False
digit_upper=False
lenght=False
for i in a:
    if i.islower():
        digit_lower=True
    if i.isupper():
         digit_upper=True
    if i in symbols:
          sym=True
    if len(a)>8:
       lenght=True
if digit_lower and digit_upper and sym and lenght:
    print("valid pass")
else:
    print("Try New One")

    #remanning program for practice 

# a=input("enter the name:")
# alpha=False
# length=True
# for i in a:
#     if i.isalpha() and len(a)>5:
#         alpha=True
#     else:
#         alpha=False
#         break

#     # if(len(a)>5):
#     #     if(i.isalpha()):
#     #         alpha=True
#     #     else:
#     #         alpha=False
#     #         break
#     # else:
#     #     length=False
#     # # if len(a)>5:
#     # #     length=True
#     # # else:
#     # #     alpha=False
#     # #     break
# if alpha and length:
#     print("yes")
# else:
#     print("no")

# # name = input("Enter username: ")

# # if len(name) >= 5 and name.isalpha():
# #     print("Valid Username")
# # else:
# #     print("Invalid Username")


# a=int(input("enter the mark: "))
# if a > 100:
#     print(" valid mark")
# else:
#     print("enter valid mark")
# a = input("enter the string: ")

# vowels = "AEIOUaeiou"

# vow = False
# digit = False

# for i in a:
#     if i in vowels:
#         vow = True

#     if i.isdigit():
#         digit = True

# if len(a) > 6 and vow and digit:
#     print("Accepted")
# else:
#     print("Not Accepted")
# Length > 5
# Alphabets only
# Must start with "A"

# # Try writing it yourself using:

# a=input()
# if len(a)>5 and a.isalpha() and a.startswith("A"):
#     print("yes")
# else:
#     print("NO")