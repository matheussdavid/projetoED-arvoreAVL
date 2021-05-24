class Musica:
    def __init__(self, nome, album, ano, idMusica):
        self.nome = nome
        self.album = album
        self.ano = int(ano)
        self.idMusica = int(idMusica)
        self.esq = None
        self.dir = None

    def __str__(self):
        return f'Nome: {self.nome}, Album:{self.album}, ano:{self.ano}, idMusica:{self.idMusica},'