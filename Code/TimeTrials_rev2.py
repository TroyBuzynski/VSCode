from datetime import datetime



class Event:
    def __init__( self):
        self.riders = []
    
    def get_riders(self):
        return self.riders
    
    def add_rider(self,rider):
        self.riders.append(rider)

class Rider:
    def __init__(self, name, start_time = "00.00.00" , end_time = "00.00.00" ):
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        
    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name = name
    
    def get_start_time(self):
        return self.start_time
    
    def set_start_time(self,start_time):
        self.start_time = start_time
    
    def get_end_time(self):
        return self.start_time
    
    def set_end_time(self,end_time):
        self.end_time = end_time
        




e =Event()
riders = ["Max", "Troy", "Phil"]
for rider in riders:
    e.add_rider(Rider(rider))

      



#for rider in e.get_riders():
 #   print(rider.get_name())
print(e.get_riders())
