import sys
import math

g = open("relationships.txt", 'w')
f = open("output.txt", 'r')

line = f.readline()
vects = [];
while (len(line) != 0):
	current = [];
	current += [line];
	for i in range(3):
		ele = f.readline();
		current += [ele]
	if abs(float(current[1])) <= 10:
		vects += [current]
	line = f.readline()

#1216
g.write("{\"relationships\": [\n")
for i in range(len(vects)):
	for j in range(i+1, len(vects)):
		summ = 0.0;
		for k in range(1,4):
			summ += (float(vects[i][k]) - float(vects[j][k])) * (float(vects[i][k]) - float(vects[j][k]));
		summ = math.sqrt(summ);
		g.write("{\"distance\": \"" + str(summ) + "\", ")
		g.write("\"id1\": \"" + vects[i][0] + "\", ")
		g.write("\"id2\": \"" + vects[j][0] + "\"}, ")


g.write("]}")
g.close()