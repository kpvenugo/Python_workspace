def isPalindrome(input_string):
    length = len(input_string)
    if length == 1:
        return 1
    if input_string[0] != input_string[len(input_string) - 1]:
        return 0
    return(isPalindrome(input_string[1:len(input_string) - 1]))


if isPalindrome("malayalam"):
    print("Yes")
else:
    print("No")

