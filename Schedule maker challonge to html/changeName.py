inputFile = open("editing.html", 'r')
data = inputFile.read()

data = data.replace('shintomo">Shintomo', 'lalipo">lalipo')

outputFile = open("lalipo.html", 'w')

outputFile.write(data)
