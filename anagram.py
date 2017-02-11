MAX_CHARS = 256


def populate_count_list(count_list, input_string):
    for c in input_string:
        count_list[ord(c)] = +  1
    return count_list


def isAnagram(input_string1, input_string2):
    if len(input_string1) != len(input_string2):
        return 0
    count_list1 = MAX_CHARS * [0]
    count_list2 = MAX_CHARS * [0]
    count_list1 = populate_count_list(count_list1, input_string1)
    count_list2 = populate_count_list(count_list2, input_string2)
    if count_list1 == count_list2:  # Awesome python supports 2 list comparison
        return 1
    return 0


print("Enter the strings")
input_string1 = input()
input_string2 = input()
if isAnagram(input_string1, input_string2):
    print("Yes")
else:
    print("No")
