from bs4 import BeautifulSoup
import HTMLParser

csv = open("input.csv", 'r')

matches = {}

for line in csv:
    parts = line.split(',')
    matchNumber = parts[1].split(' ')
    matches[matchNumber[0]] = parts[2:]
    
table = open("table.html", "r")
soup = BeautifulSoup(table)

table = soup.find("table")
rows = table.find_all("tr")
for row in rows:
    cols = row.find_all('td')
    index = cols[0].contents[0].strip()
    try:
        match = matches[index]

        matchHistory = ""
        links = match[1].split(' ')
        for link in links:
            matchHistory = matchHistory + "<a href='" + link + "'><img src='http://osuuci.com/tournaments/osl/arrow.png' /></a>"

            cols[4].string.replaceWith(match[0])
            cols[5].string.replaceWith(matchHistory)
    except:
        pass


    
output = open("output.html", "w")
html = str(soup)


h = HTMLParser.HTMLParser()
html = h.unescape(html)

output.write(html)
output.close()

print "Complete"
