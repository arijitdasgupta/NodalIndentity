#Test CSV data generator for the tree like dataset
#Author: Arijit Dasgupta

import csv

data_set = [
['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw'],
['Jounin', 'Chounin', 'Genin'],
['Earth', 'Water', 'Air', 'Fire'],
['Blade', 'Gun', 'Liquid Sword'],
['Power User', 'Strength User']] #Allowable sets

data_set_depth = len(data_set)

op_file = open('test_data.csv', 'w', True)
csvWriter = csv.writer(op_file)

combi_list = []

for depth in range(data_set_depth):
	set_len = 1
	d = depth + 1
	lens = []
	for i in range(d):
		set_len *= len(data_set[i])
		lens.append(len(data_set[i]))
	temp_list = []
	counter = 0;
	for i in range(set_len): #Combinatorial routine
		rem = i
		divisor = set_len
		temp_list.append([])
		for index, div in enumerate(lens):
			divisor /= div
			pos = rem/divisor
			temp_list[-1].append(data_set[index][pos])
			rem %= divisor
	combi_list.extend(temp_list)
	
for i in combi_list:
	csvWriter.writerow(i)
	print i
			
op_file.close()

#End of program