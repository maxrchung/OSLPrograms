'''
Created on Jul 3, 2015

@author: Justin
'''

s = """OSL1     Sat 8:00 PM     WynnWolf     tyronetoblerone     N/A     N/A     osuuci dot com
OSL2     Sat 8:00 PM     DeucesWiId     leluffy     N/A     N/A     Shintomo
OSL3     Sat 8:00 PM     eeezzzeee     mintypeach     N/A     N/A     mauler68
OSL4     Sat 8:00 PM     Vapor     YunoWhoItIs     N/A     N/A     lalipo
OSL5     Sat 8:30 PM     payau     - Nakano Azusa-     N/A     N/A     osuuci dot com
OSL6     Sat 8:30 PM     jackisgone     plaatinum     N/A     N/A     Shintomo
OSL7     Sat 8:30 PM     Fridolin     shivo     N/A     N/A     mauler68
OSL8     Sat 8:30 PM     KogureKun     BBastia     N/A     N/A     lalipo
OSL9     Sat 9:00 PM     Natalia     Kyoko     N/A     N/A     osuuci dot com
OSL10     Sat 9:00 PM     Bass     bananamilk     N/A     N/A     Shintomo
OSL11     Sat 9:00 PM     Kazuki     Alexefer     N/A     N/A     mauler68
OSL12     Sat 9:00 PM     Ryan Gooseling     Keanu     N/A     N/A     lalipo
OSL13     Sat 9:30 PM     IOException     Amagi     N/A     N/A     osuuci dot com
OSL14     Sat 9:30 PM     Kocari     kennyyam     N/A     N/A     Shintomo
OSL15     Sat 9:30 PM     PainSinger     Andrew     N/A     N/A     mauler68
OSL16     Sat 9:30 PM     Ecliptus     Demitoo     N/A     N/A     lalipo
OSL17     Sun 8:00 PM     Poofie     Slvin     N/A     N/A     osuuci dot com
OSL18     Sun 8:00 PM     iSlapWhale     HijiCG     N/A     N/A     Shintomo
OSL19     Sun 8:00 PM     Aaerok     BradXYZ     N/A     N/A     mauler68
OSL20     Sun 8:00 PM     saltstick     Endyron     N/A     N/A     lalipo
OSL21     Sun 8:30 PM     Xexxar     Karuta-     N/A     N/A     osuuci dot com
OSL22     Sun 8:30 PM     YoshiIsAwsum     ScrYpt     N/A     N/A     Shintomo
OSL23     Sun 8:30 PM     Aoiyuuki-     kymotsujason     N/A     N/A     mauler68
OSL24     Sun 8:30 PM     Cl8n     Raddy     N/A     N/A     lalipo
OSL25     Sun 9:00 PM     Kuki     Zafkiel     N/A     N/A     osuuci dot com
OSL26     Sun 9:00 PM     Ignite     captin1     N/A     N/A     Shintomo
OSL27     Sun 9:00 PM     KevEz     Dunois     N/A     N/A     mauler68
OSL28     Sun 9:00 PM     [Neetwork]     Keepu     N/A     N/A     lalipo
OSL29     Sun 9:30 PM     Zukarido     Xbox     N/A     N/A     osuuci dot com
OSL30     Sun 9:30 PM     TheOnlyLeon     Ultraplex1337     N/A     N/A     Shintomo
OSL31     Sun 9:30 PM     Ex6TenZ     Kaifin     N/A     N/A     mauler68
OSL32     Sun 9:30 PM     Renkee     kutora     N/A     N/A     lalipo"""
s = s.split("\n")
s = [tuple(a.split("     ")[2:4]) for a in s]

#Above makes a list of entrants
temp = []

for a in s:
    for b in a:
        link = "https://osu.ppy.sh/u/" + b.replace(" ", "%20")
        temp.append('<a href="{}">{}</a>'.format(link, b))
'''<a href="https://osu.ppy.sh/u/1472763">osuuci dot com</a>'''
f = open("temp.txt", 'r')
txt = f.read()
f.close()

def special_iter(itera):
    for item in itera:
        for i in item:
            yield i

for name, link in zip(special_iter(s),temp):
    print(name, link)
    assert name in txt
    txt = txt.replace(name,link)

f = open("temp.html", 'w')
f.write(txt)
f.close()
