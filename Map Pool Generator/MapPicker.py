from random import randrange
#random generator

class MapPicker:

    def __init__(self):

        self.DT	= [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]							#Double Time map pool
        self.HR = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]					#No Mod map pool
        self.HD = [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91]					#Hidden map pool
        self.NM	= [92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 17, 118, 119, 120, 121]	#Hard Rock map pool
        self.TB = [122, 123, 124, 125, 126, 127, 128, 129, 130, 131]	#Tiebreaker map pool
		
	self.DTmaps = []
	self.NMmaps = []
	self.HDmaps = []
	self.HRmaps = []
	self.TBmap = None
        self.maps = []
        self.set_maps()
                

    def create_list(self):
        #creates a list of maps
        self.searchfile = open("List of Maps.txt", "r")
        for line in self.searchfile:
            self.maps.append(line.rstrip("\n"))
        self.searchfile.close()
		
		
    def random_search(self, pool):
        # pops the 3 map #s from the pool
        self.map1 = pool.pop(randrange(0, len(pool)))
        self.map2 = pool.pop(randrange(0, len(pool)))
        self.map3 = pool.pop(randrange(0, len(pool)))
        
        return [self.maps[self.map1 - 1], self.maps[self.map2 - 1], self.maps[self.map3 - 1]]

    def run_randomizer(self):
        self.set_DT()
        self.set_NM()
        self.set_HD()
        self.set_HR()
        self.set_TB()
            
    def get_maps(self): return self.maps
    def set_maps(self): self.create_list()
    def get_DT(self): return self.DTmaps
    def set_DT(self): self.DTmaps = self.random_search(self.DT)
    def get_NM(self): return self.NMmaps
    def set_NM(self): self.NMmaps = self.random_search(self.NM)
    def get_HD(self): return self.HDmaps
    def set_HD(self): self.HDmaps = self.random_search(self.HD)
    def get_HR(self): return self.HRmaps
    def set_HR(self): self.HRmaps = self.random_search(self.HR)
    def get_TB(self): return self.TBmap
    def set_TB(self): self.TBmap = self.maps[self.TB.pop(randrange(0, len(self.TB)))]
		
    def print_maps(self):

        print("No Mod: \nMap 1: {}\nMap 2: {}\nMap 3: {}".format(self.NMmaps[0], self.NMmaps[1], self.NMmaps[2]))
        print("Double Time:\nMap 1: {}\nMap 2: {}\nMap 3: {}".format(self.DTmaps[0], self.DTmaps[1], self.DTmaps[2]))
        print("Hidden:\nMap 1: {}\nMap 2: {}\nMap 3: {}".format(self.HDmaps[0], self.HDmaps[1], self.HDmaps[2]))
        print("Hard Rock:\nMap 1: {}\nMap 2: {}\nMap 3: {}".format(self.HRmaps[0], self.HRmaps[1], self.HRmaps[2]))
        print("And tiebreaker is: {}".format(self.TBmap))
