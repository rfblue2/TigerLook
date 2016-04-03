import sys
import math

g = open("relationships.txt", 'w')
f = open("output.txt", 'r')

line = f.readline()
vects = [];
while (len(line) != 0):
	current = [];
	current += [line];
	for i in range(5):
		ele = f.readline();
		current += [ele]
	vects += [current]


g.write("{\"relationships\": [\n")
for i in range(len(vects)):
	for j in range(i+1, len(vects)):
		summ = 0.0;
		for k in range(1,6):
			sum += (vects[i][k] - vects[j][k]) * (vects[i][k] - vects[j][k]);
		summ = math.sqrt(summ);
		g.write("{\"distance\": \"" + str(summ) + "\", ")
		g.write("\"id1\": \"" + vects[i] + "\", ")
		g.write("\"id2\": \"" + vects[i] + "\"}, ")


g.write("]}")
g.close()