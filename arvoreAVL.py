from musica import Musica

class Arvore:
    def __init__(self):
        self.raiz = None
        self.altura = -1
        self.balanco = 0

    def att_altura(self, recursivo = True):
        if self.raiz:
            if recursivo:
                if self.raiz.esq:
                    self.raiz.esq.att_altura()
                if self.raiz.dir:
                    self.raiz.dir.att_altura()
            self.altura = 1 + max(self.raiz.esq.altura, self.raiz.dir.altura)
        else:
            self.altura = -1

    def att_balanco(self, recursivo = True):
        if self.raiz:
            if recursivo:
                if self.raiz.esq:
                    self.raiz.esq.att_balanco()
                if self.raiz.dir:
                    self.raiz.dir.att_balanco()
            self.balanco = self.raiz.esq.altura - self.raiz.dir.altura
        else:
            self.balanco = 0
            
    def inserir(self, dados):
        n = Musica(dados.nome, dados.album, dados.ano, dados.idMusica)
        if self.raiz == None:
            self.raiz = n
            self.raiz.esq = Arvore()
            self.raiz.dir = Arvore()
        elif dados.idMusica < self.raiz.idMusica:
            self.raiz.esq.inserir(dados)
        elif dados.idMusica > self.raiz.idMusica:
            self.raiz.dir.inserir(dados)
        elif dados.idMusica == self.raiz.idMusica:
            return False
        self.balancear()
        return True

    def balancear(self):
        self.att_altura(recursivo = False)
        self.att_balanco(False)
        while self.balanco < -1 or self.balanco > 1:
            if self.balanco > 1:
                if self.raiz.esq.balanco < 0:
                    self.raiz.esq.rotacionar_esq()
                    self.att_altura()
                    self.att_balanco()
                self.rotacionar_dir()
                self.att_altura()
                self.att_balanco()
            if self.balanco < -1:
                if self.raiz.dir.balanco > 0:
                    self.raiz.dir.rotacionar_dir()
                    self.att_altura()
                    self.att_balanco()
                self.rotacionar_esq()
                self.att_altura()
                self.att_balanco()

    def rotacionar_dir(self):
        nova_raiz = self.raiz.esq.raiz
        nova_raiz_esq = nova_raiz.dir.raiz
        raiz_anterior = self.raiz

        self.raiz = nova_raiz
        raiz_anterior.esq.raiz = nova_raiz_esq
        nova_raiz.dir.raiz = raiz_anterior

    def rotacionar_esq(self):
        nova_raiz = self.raiz.dir.raiz
        nova_raiz_esq = nova_raiz.esq.raiz
        raiz_anterior = self.raiz

        self.raiz = nova_raiz
        raiz_anterior.dir.raiz = nova_raiz_esq
        nova_raiz.esq.raiz = raiz_anterior
        
        
lista = []    
def encontra_ano(valor, value = None):
    if value == None:
        return None
            
    if value.raiz.ano == valor:
        lista.append(value.raiz.nome)
        if value.raiz.esq.raiz != None:
            encontra_ano(valor, value.raiz.esq)
        if value.raiz.dir.raiz != None:
            encontra_ano(valor, value.raiz.dir)
    else:
        if value.raiz.esq.raiz != None:
            encontra_ano(valor, value.raiz.esq)
        if value.raiz.dir.raiz != None:
            encontra_ano(valor, value.raiz.dir)
    
    return lista   

musicasOrd = []
def ordenarMusicas(raiz = None):
    if raiz == None:
        return None

    musicasOrd.append(raiz.raiz.nome)        
    if raiz.raiz.esq.raiz != None:
        ordenarMusicas(raiz.raiz.esq)
    if raiz.raiz.dir.raiz != None:
        ordenarMusicas(raiz.raiz.dir)
        
    listafinal = sorted(musicasOrd)
    return listafinal   
    
def encontraMusica(raiz, valor):
    if raiz == None:
        return None 
    elif valor > raiz.raiz.idMusica:
        return encontraMusica(raiz.raiz.dir, valor)
    elif valor < raiz.raiz.idMusica:
        return encontraMusica(raiz.raiz.esq, valor)
    else:
        return raiz.raiz

def imprimirArvore(arvore, level=0):
    if arvore.raiz != None:
        imprimirArvore(arvore.raiz.esq, level + 1)
        print(' ' * 4 * level + '->', arvore.raiz.idMusica)
        imprimirArvore(arvore.raiz.dir, level + 1)     
