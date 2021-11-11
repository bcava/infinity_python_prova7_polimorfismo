class Atletas:
    def __init__(self, nome, idade, score, cat):
        self._nome = nome
        self._idade = idade
        self._score = score
        self._cat = cat


    @property
    def nome(self):
        return self._nome
    nome.setter
    def nome (self, nome):
        self.nome = nome


    @property
    def idade(self):
        return self._idade
    idade.setter
    def idade (self, idade):
        self.idade = idade


    @property
    def score(self):
        return self._score
    score.setter
    def score (self, score):
        self.score = score


    @property
    def cat(self):
        return self._cat
    cat.setter
    def cat (self, cat):
        self.cat = cat



