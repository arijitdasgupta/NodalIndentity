#Parser program for creating the 2D point set.
#Author: Arijit Dasgupta

from csv import reader
from math import ceil
from random import randint

filename = raw_input("Enter the data filename (in CSV) (Default test_data.csv) : ")
if  filename.strip() == '':
	filename = "test_data.csv"

ip_file = open(filename,'r')
csvReader = reader(ip_file)

tree = {}
dot_counter = 0

class PointData:
	def __init__(self, x, y, depth):
		self.x = x
		self.y = y
		self.depth = depth

max_depth = 0
		
for row in csvReader: #Parsing the tree data structure
	temp = tree
	depth_counter = 0
	for val in row:
		depth_counter += 1
		if val in temp.keys():
			temp = temp[val][1]
		else:
			temp[val] = [None,{}]
			dot_counter += 1
	if depth_counter > max_depth:
		max_depth = depth_counter
			
#Data structure tree-type parsing done!

#Setting the positions for each node points		
square_side = int(ceil(dot_counter ** (0.5)))
square = square_side ** 2
print square, square_side
#A recursve function for traversing the tree
counter = 0
positions_taken = []

def walkDic(struct, depth):
	global counter
	if struct != {}:
		for i in struct:
			counter += 1
			while True:
				init_x = randint(0, square_side - 1) #Simple random position generator, can be improved!
				init_y = randint(0, square_side - 1)
				if (init_x, init_y) not in positions_taken:
					positions_taken.append((init_x, init_y))
					break
			struct[i][0] = PointData(init_x, init_y, depth)
			print '(x = %i, y  = %i) depth = %i'%(struct[i][0].x, struct[i][0].y, struct[i][0].depth)
			walkDic(struct[i][1], depth + 1)
	else:
		return

walkDic(tree, 0)
#Tree travserse done!
# print tree
print counter

#Making the node wise points
ip_file = open('test_data.csv','r')
csvReader = reader(ip_file)

op_file = open('ID_plotter/data.txt', 'w', True) #The Data that would be fed into the processing system
op_file2 = open('ID_plotter/names.txt', 'w', True) #The Data that is to be used to name reference
for row in csvReader:
	temp = tree
	for i in row:
		op_file.write('(%i,%i,%i) '%(temp[i][0].x, temp[i][0].y, temp[i][0].depth))
		op_file2.write('%s '%(i))
		temp = temp[i][1]
	op_file.write('\n')
	op_file2.write('\n')
op_file.close()
op_file2.close()

op_file = open("ID_plotter/params.txt", 'w', True)
op_file.write('%i\n'%(square_side))
op_file.write('%i\n'%(max_depth))
op_file.close()

	
	
