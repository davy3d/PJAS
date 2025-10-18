import datetime
import csv

class NewCsv:
    
    def __init__(self):
        pass
    
    def newcsv(self, filename):
        self.time = datetime.datetime.now()
        self.filetime = self.time.strftime('%Y_%m_%d')
        newfilename = f'wether_data_{self.filetime}'
        
        if self.filetime not in filename:
            with open(newfilename, 'x') as csvfile:
                csvfileWriter = csv.DictWriter(csvfile, ['Time', 'Number of drops per frame'])
                csvfileWriter.writeheader()
            return newfilename
        else:
            return filename