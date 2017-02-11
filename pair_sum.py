def isPair(num_collection, s):
    length = len(num_collection)
    i = 0
    group_pair = []
    
    while i < length - 1:
        current_sum = num_collection[i] + num_collection[length - 1]
        if current_sum == s:
            pair = []
            pair.append(num_collection[i])
            pair.append(num_collection[length - 1])
            group_pair.append(pair)
        elif current_sum > s:
            length = length - 1
            continue
        i = i + 1
    return group_pair


num_collection = [-1, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 6]
s = 5
pair = isPair(num_collection, s)
if len(pair) != 0:
    print(pair)
else:
    print("No")
