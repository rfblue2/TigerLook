import sys
import math

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


f = open("output.txt", 'r')

line = f.readline()
vects = [];
tracker = 0
print("parsing")
while (len(line) > 0):
    current = [];
    current += [line];
    counter = 0

    for i in range(3):
        ele = f.readline()
        # print(ele)
        if not is_number(ele):
            break
        current += [ele]
        counter += 1
        # print("BOB")

        
    if (counter == 3):
        # print(current[0])
        if abs(float(current[1])) <= 10:
            vects += [current]
        line = f.readline()
    tracker += 1


#1216
print("starting")
new_counter = 1
nums = 0
g = open("relationships"+str(new_counter)+".txt", 'w')
g.write("[\n")
for i in range(len(vects)):
    print(str(i))
    for j in range(i+1, len(vects)):
        summ = 0.0;
        for k in range(1,4):
            summ += (float(vects[i][k]) - float(vects[j][k])) * (float(vects[i][k]) - float(vects[j][k]));
        summ = math.sqrt(summ);
        if nums == 999999 or (j == len(vects) - 1 and i == len(vects) - 2):
            g.write("{\"distance\": \"" + str(summ) + "\",\"id1\":\"" + vects[i][0][:-1] + "\",\"id2\":\"" + vects[j][0][:-1] + "\"}")
        else:
            g.write("{\"distance\": \"" + str(summ) + "\",\"id1\":\"" + vects[i][0][:-1] + "\",\"id2\":\"" + vects[j][0][:-1] + "\"},")
        nums += 1

        if (nums >= 1000000):
            g.write("]")
            g.close()
            nums = 0
            new_counter += 1
            g = open("relationships"+str(new_counter)+".txt", 'w')
            g.write("[\n")


g.write("]")
g.close()