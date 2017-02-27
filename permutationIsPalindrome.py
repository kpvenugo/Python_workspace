def isPermutationPalindrome(input_string):
    input_set = set()
    for c in input_string:
        if c in input_set:
            input_set.remove(c)
        else:
            input_set.add(c)
    if len(input_set) <= 1:
        return 1
    else:
        return 0


print(isPermutationPalindrome("ababax"))  # '0' for Not '1' for Yes
