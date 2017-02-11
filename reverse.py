import sys
if len(sys.argv) != 2:
    print("enter 1 string")
sys.exit()
print(sys.argv[1][::-1])
