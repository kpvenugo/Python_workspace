my_list = [x for x in range(10)]
print(my_list)
my_dict = [x for x in range(10) if x > 5]
print(my_dict)


a = lambda x, y:[i for i in range(10)] + x + y

print(a([11], [12]))


g = list(range(10))
print(map(lambda b: b * 10, g))

print(filter(lambda a: a > 5, g))   # note map and filter is different

print(reduce(lambda a, b : a + b, g)) # first 2 arg from list return one argument and use  next element from list and the result for next

print(reduce(lambda a, b : a + " " + b, "networking"))