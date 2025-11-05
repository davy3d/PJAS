import datetime
import csv
import os

class NewCsv:
    
    def __init__(self):
        pass
    
    def newcsv(self, filename):
        self.time = datetime.datetime.now()
        self.filetime = self.time.strftime('%Y_%m_%d')
        newfilename = f'wether_data_{self.filetime}.csv'
        
        if self.filetime not in filename:
            if os.path.exists(newfilename):
                with open(newfilename, 'a') as csvfile:
                    csvfileWriter = csv.DictWriter(csvfile, ['Time', 'Number of drops per frame', 'rain on ground'])
                return newfilename
        
            else:
                with open(newfilename, 'w') as csvfile:
                    csvfileWriter = csv.DictWriter(csvfile, ['Time', 'Number of drops per frame', 'rain on ground'])
                    csvfileWriter.writeheader()
                return newfilename
        else:
            return filename