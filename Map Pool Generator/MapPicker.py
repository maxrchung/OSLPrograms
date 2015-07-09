#Victor Stolle MapPicker.py
from random import randrange
from csvToMap import MapMaker

#random generator
class MapPicker:

    def __init__(self):

        self.mapmaker = MapMaker()
        '''
        Mapmaker object: defaultdict(list)
        DTmap[num ( 0 -> self.param )] = [[Artist, Title, Difficulty, Link, Mod, Length, Star, Song No.], html]
        '''        
        self.DT = [i for i in range(0, len(self.mapmaker.getDTmaps().items()))]#Double Time map pool
        self.HR = [i for i in range(0, len(self.mapmaker.getHRmaps().items()))]#No Mod map pool
        self.HD = [i for i in range(0, len(self.mapmaker.getHDmaps().items()))]#Hidden map pool
        self.NM = [i for i in range(0, len(self.mapmaker.getNMmaps().items()))]#Hard Rock map pool
        self.TB = [i for i in range(0, len(self.mapmaker.getTBmaps().items()))]#Tiebreaker map pool
        
        self.DTmaps = []
        self.NMmaps = []
        self.HDmaps = []
        self.HRmaps = []
        self.TBmap = None

        self.map1 = 0
        self.map2 = 0
        self.map3 = 0


        self.run_randomizer()
        
    def random_search(self, pool):
        # pops the 3 map #s from the pool
        self.map1 = pool.pop(randrange(0, len(pool)))
        self.map2 = pool.pop(randrange(0, len(pool)))
        self.map3 = pool.pop(randrange(0, len(pool)))

    def run_randomizer(self):
        self.set_DT()
        self.set_NM()
        self.set_HD()
        self.set_HR()
        self.set_TB()
            
    def get_maps(self): return self.mapmaker
    def get_DT(self): return self.DTmaps
    def set_DT(self):
        self.random_search(self.DT)
        self.DTmaps = [self.mapmaker.getDTmaps()[str(self.map1)], self.mapmaker.getDTmaps()[str(self.map2)], self.mapmaker.getDTmaps()[str(self.map3)]]
    def get_NM(self): return self.NMmaps
    def set_NM(self):
        self.random_search(self.NM)
        self.NMmaps = [self.mapmaker.getNMmaps()[str(self.map1)], self.mapmaker.getNMmaps()[str(self.map2)], self.mapmaker.getNMmaps()[str(self.map3)]]
    def get_HD(self): return self.HDmaps
    def set_HD(self):
        self.random_search(self.HD)
        self.HDmaps = [self.mapmaker.getHDmaps()[str(self.map1)], self.mapmaker.getHDmaps()[str(self.map2)], self.mapmaker.getHDmaps()[str(self.map3)]]
    def get_HR(self): return self.HRmaps
    def set_HR(self):
        self.random_search(self.HR)
        self.HRmaps = [self.mapmaker.getHRmaps()[str(self.map1)], self.mapmaker.getHRmaps()[str(self.map2)], self.mapmaker.getHRmaps()[str(self.map3)]]
    def get_TB(self): return self.TBmap
    def set_TB(self):
        self.TBmap = self.mapmaker.getTBmaps()[str(randrange(0, len(self.TB)))]
        
    def print_maps(self):

        print("No Mod: \nMap 1: {}\nMap 2: {}\nMap 3: {}\n".format(self.NMmaps[0][0][1], self.NMmaps[1][0][1], self.NMmaps[2][0][1]))
        print("Double Time:\nMap 1: {}\nMap 2: {}\nMap 3: {}\n".format(self.DTmaps[0][0][1], self.DTmaps[1][0][1], self.DTmaps[2][0][1]))
        print("Hidden:\nMap 1: {}\nMap 2: {}\nMap 3: {}\n".format(self.HDmaps[0][0][1], self.HDmaps[1][0][1], self.HDmaps[2][0][1]))
        print("Hard Rock:\nMap 1: {}\nMap 2: {}\nMap 3: {}\n".format(self.HRmaps[0][0][1], self.HRmaps[1][0][1], self.HRmaps[2][0][1]))
        print("And tiebreaker is: {}".format(self.TBmap[0][1]))

