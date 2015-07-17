'''
Created on Jul 3, 2015

@author: Justin
'''

s = """Ryan Gooseling
Zukarido
Ignite
PainSinger
Alexefer
jaskier2
Bass
YunoWhoItIs
Zafkiel
Kaifin
Shinyblade
BBastia
Ecliptus
Amagi
DeucesWiId
Kocari
shivo
Keanu
Andrew
captin1
Xexxar
ScrYpt
Xbox
Karuta-
bananamilk
- Nakano Azusa-
IOException
Natalia
kennyyam
Ultraplex1337
Keepu
Vapor
Cl8n
KevEz
Dunois
jackisgone
plaatinum
Ex6TenZ
Aaerok
BradXYZ
[Neetwork]
Kazuki
Aoiyuuki-
kymotsujason
leluffy
kutora
Kuki
payau
WynnWolf
tyronetoblerone
TheOnlyLeon
iSlapWhale
saltstick
KogureKun
Rhylent
funnytrees"""
s = s.split("\n")
print s

#Above makes a list of entrants
temp = []

for a in s:
    link = "https://osu.ppy.sh/u/" + a.replace(" ", "%20")
    temp.append((a, '<a href="{}">{}</a>'.format(link, a)))

print temp
        
f = open("input.html", 'r')
txt = f.read()
f.close()

def special_iter(itera):
    for item in itera:
        for i in item:
            yield i

for name in temp:
    print name
    txt = txt.replace(name[0], name[1])


print txt
f = open("output.html", 'w')
f.write(txt)
f.close()
