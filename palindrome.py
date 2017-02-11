# def isPalindrome(input_string):
#     length = len(input_string)
#     i = 0
#     while i < length - 1:
#         if input_string[i] != input_string[length - 1]:
#             return 0
#         i += 1
#         length -= 1
#     return 1


# if isPalindrome("battab"):
#     print("Yes")
# else:
#     print("No")

input_string = "hello"
if(input_string == input_string[::-1]):
    print("yes")
else:
    print("no")
