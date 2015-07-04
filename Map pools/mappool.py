# Output file
output = open("mappool.html", "w")

# Header HTML
output.write("<table>\n<tr>\n<td>Mod</td>\n<td>Title</td>\n<td>Artist</td>\n<td>Difficulty</td>\n<td>Length</td>\n<td>Stars</td>\n</tr>\n")

# Reads in a mappool
with open("swiss.csv", "r") as openfileobject:
    for line in openfileobject:
        # Splits information from Swiss maps and presents as HTML
        split = line.split(",")
        output.write("<tr>\n<td>\n" + split[4] + '</td>\n<td>\n<a href="' + split[3] + '">' + split[1] + "</a>\n</td>\n<td>\n" + split[0] + "</td>\n<td>" + split[2] + "</td>\n<td>" + split[5] + "</td>\n<td>" + split[6] + "</td>\n</tr>\n")

output.write("</table>\n")
output.close()
