import dis

def my_swap(a, b):
    a, b, c , d = b, a, d, c
print(dis.dis(my_swap)) 
dis.dis