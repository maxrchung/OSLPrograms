file = open("output.html", 'r')
text = file.read()
text.replace("&gt;", ">")
text.replace("&lt;", "<")
print(text)

