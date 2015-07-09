#Victor Stolle MapTocsv.py
import csv

class CSVGenerator:

    def __init__(self, mapmaker, DT, HR, HD, NM, TB):
        self.DT = DT
        self.HR = HR
        self.HD = HD
        self.NM = NM
        self.TB = TB
        self.mapmaker = mapmaker


    def write(self):
        #csv write 
