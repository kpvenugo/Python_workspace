print ("enter the hieght of the inverted tree")
max_hieght = int(input())
for hieght in range(max_hieght, -1, -1) :
	print((max_hieght - hieght) * "\t" + (hieght + 1) * "*\t\t") 
