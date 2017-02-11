string_list = list("abc")


def list_print(string_list):
    print(''.join(string_list))


def getPermutation(left, right):
    if(left == right):
        list_print(string_list)
    for i in range(left, right + 1):
        string_list[left], string_list[i] = string_list[i], string_list[left]
        getPermutation(left + 1, right)
        string_list[left], string_list[i] = string_list[i], string_list[left]


getPermutation(0, len(string_list) - 1)
