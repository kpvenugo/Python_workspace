def construct_dict(input_string):
    count_dict = {}
    for s in set(input_string):
        count_dict[s] = 0
    for c in input_string:
        count_dict[c] += 1
    return count_dict


def isAnagram(input_string1, input_string2):
    if len(input_string1) != len(input_string2):
        return 0
    count_dict1 = construct_dict(input_string1)
    count_dict2 = construct_dict(input_string2)
    if count_dict1 == count_dict2:
        return 1
    return 0


print("Enter the input strings")
input_string1 = input()
input_string2 = input()
if isAnagram(input_string1, input_string2):
    print("yes")
else:
    print("no")
