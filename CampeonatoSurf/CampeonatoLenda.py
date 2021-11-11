from Campeonato import Campeonato
from Atletas import Atletas
from Sponsor import Sponsor



def verificaCat(cat):
    if cat=="Lenda":
        return True
    return False
    




class Lenda:
    def __init__(self, nomeCamp, local, premio, sponsor, atletas):
        super().__init__(nomeCamp, local, premio, sponsor, verificaCat(atletas))
    
    
    
    def pontos(self):
        return self._score + 100