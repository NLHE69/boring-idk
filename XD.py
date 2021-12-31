import random

while True:
	i = random.randint(0,10)
	fh = open(str(i) + ".txt", 'w')
	fh.write("you can't delete me XD")
