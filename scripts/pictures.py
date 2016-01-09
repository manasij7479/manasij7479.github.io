import os

gallery_dir = "data/pictures/galleries"
header_file = open("data/pictures/header.txt", "r")
footer_file = open("data/pictures/footer.txt", "r")
output_file = open("../pictures.html", "w")

output_file.write(header_file.read())

gallery_string = ""
dir_list = []
for dir in [x for x in os.listdir(gallery_dir)]:
	# print (dir)
	gallery_string += "<div class=\"container\">\n"
	gallery_string += "<div class=\"header clearfix\">\n"
	gallery_string += "<h4 class=\"text-muted\">" + dir + "</h3></div>\n"
	gallery_string += "<div class=\"" + dir + "\">\n"
	for pic in [x for x in os.listdir(gallery_dir + "/" + dir)]:
		# print ("\t" + pic)
		gallery_string += "<img src=\" " + "scripts/data/pictures/galleries/" + dir +"/"+ pic+ " \">\n"
	gallery_string += "</div><hr></div>\n"
	dir_list.append (dir)

gallery_string += "<script>\n"
gallery_string += "Galleria.loadTheme('external/galleria/themes/classic/galleria.classic.min.js');\n"
for dir in dir_list:
	gallery_string += "Galleria.run('." + dir+ "');\n"
gallery_string += "</script>\n"

output_file.write (gallery_string)
output_file.write (footer_file.read())
