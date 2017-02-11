# import sys
# if len(sys.argv) != 2:
#     print("Enter exactly one word")
#     sys.exit()


def list_print(string_list):
    print(''.join(string_list))


def generate_permutations(left, right):
    if left == right:
        list_print(string_list)
    for i in range(left, right + 1):
        string_list[left], string_list[i] = string_list[i], string_list[left]
        generate_permutations(left + 1, right)
        # replace back to original postion as part of backtracking
        string_list[left], string_list[i] = string_list[i], string_list[left]


input_string = "1234"
string_list = list(input_string)
generate_permutations(0, len(input_string) - 1)
