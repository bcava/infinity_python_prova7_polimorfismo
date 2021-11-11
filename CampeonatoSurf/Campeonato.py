
def verificaCat(cat):
    pass






class Campeonato:
    def __init__(self, nomeCamp, local, premio, sponsor, atletas):
        self._nomeCamp = nomeCamp
        self._local = local
        self._premio = premio
        self._sponsor = sponsor
        self._atletas = verificaCat(atletas)
    
    
    @property
    def nomeCamp(self):
        return self._nomeCamp
    nomeCamp.setter
    def nomeCamp (self, nomeCamp):
        self.nomeCamp=nomeCamp
    
    
    @property
    def local(self):
        return self._local
    local.setter
    def local (self, local):
        self.local=local   


    @property
    def premio(self):
        return self._premio
    premio.setter
    def premio (self, premio):
        self.premio=premio
    
    @property
    def sponsor(self):
        return self._sponsor
    sponsor.setter
    def sponsor (self, sponsor):
        self.sponsor=sponsor   

    @property
    def atletas(self):
        return self._atletas
    atletas.setter
    def atletas (self, atletas):
        self.atletas=atletas   






    def pontos(self):
        pass







