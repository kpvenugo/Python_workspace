import sys
file_name = sys.argv[1]
if len(sys.argv) != 2:
    print("enter file name")
    sys.exit()
txt = open(file_name)
print(txt.read())
