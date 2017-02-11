NO_OF_CHARS = 256


def fill_list(count_list, input_string):
    for c in input_string:
        count_list[ord(c)] += 1
    return count_list


count_list = 256 * [0]
print("enter the input string")
input_string = input()
count_list = fill_list(count_list, input_string)
k = 0

for c in count_list:
    if c > 1:
        print(chr(k), c)
    k = k + 1
