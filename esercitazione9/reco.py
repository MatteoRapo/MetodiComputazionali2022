class Hit:
    def __init__(self, modulo,sensore,timestamp):
        self.modulo=modulo
        self.sensore=sensore
        self.timestamp=timestamp

    def __lt__(self,other):
        return self.timestamp < other.timestamp
    def __gt__(self,other):
        return self.timestamp > other.timestamp
    def __sub__(self,other):
        return self.timestamp - other.timestamp
    
class Event:
    def __init__(self,num,timestamp1,timestamp2,durata,arrayhit):
        self.numero=num
        self.timestampinit=timestamp1
        self.timestampfin=timestamp2
        self.durata=durata
        self.insieme_degli_eventi=arrayhit
    def __str__(self):
        print("Questo evento contiene "+ str(self.numero)+ " eventi, il timestamp del primo hit è "+str( self.timestampinit) +", il timestamp del secondo event è "+str( self.timestampfin) +", la durata è "+str( self.durata) +".")
        return  
        
