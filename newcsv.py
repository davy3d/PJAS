import datetime

class NewCsv:
    
    def __init__(self):
        pass
    
    def newcsv(self, filename):
        self.time = datetime.datetime.now()
        self.timeday = self.time.strftime('%d')
        self.timedif = self.time - datetime.timedelta(seconds=1)
        self.timedif = self.timedif.strftime('%d')
        self.filetime = self.time.strftime('%Y_%m_%d')
        
        if self.timedif != self.time and self.filetime not in filename:
            return open(f'wether_data_{self.filetime}', 'x')
        else:
            return None