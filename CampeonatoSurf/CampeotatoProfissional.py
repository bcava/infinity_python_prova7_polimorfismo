from Campeonato import Campeonato
from Atletas import Atletas
from Sponsor import Sponsor


def verificaCat(cat):
    if cat=="Lenda" or cat=="Profissional":
        return True
    return False
    



class Profissional:
    def __init__(self, nomeCamp, local, premio, sponsor, atletas):
        super().__init__(nomeCamp, local, premio, sponsor, verificaCat(atletas))

    
    
    
    def pontos(self):
        return Atletas.score + 50
    
