import random

while True:
	i = random.randint(1,10)#number of files
	fh = open(str(i) + ".txt", 'w')
	fh.write("you can't delete me XD")# text in the files
