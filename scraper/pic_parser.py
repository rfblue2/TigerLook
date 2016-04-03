import sys


g = open("name_pics.txt", 'w')


colleges=["butler", "forbes", "mathey" ,"rockefeller", "whitman", "wilson"]
g.write("{\"students\": [\n")
for c in colleges:
	for j in range(1,60):
		f = open("res_pages/"+c+"/"+c+str(j)+".html", 'r')
		body = f.read()

		index = 0

		for i in range(16):
			index = body.find("<div class=\"photo\">", index, len(body)) + len("<div class=\"photo\"><img alt=\"") - 1
			name_start = body.find("\"", index, len(body))
			name_end = body.find("\"", name_start+1, len(body))
			pic_start = body.find("src=\"", index, len(body)) + 4
			pic_end = body.find("\"", pic_start+1, len(body))
			if (len(body[name_start+1:name_end]) > 1):
				#{"name": "Matthew Li", "img": "images/matthew.png"},
				g.write("{\"name\": \"" + body[name_start+1:name_end] + "\", ")
				g.write("\"img\": \"" + "http://www.princeton.edu" + body[pic_start+1:pic_end] + "\"},\n")

g.write("]}")
g.close()