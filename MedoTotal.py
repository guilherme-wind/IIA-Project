
from collections import namedtuple
from searchPlus import *
import timeit    # Para tirar


EstadoMedo = namedtuple('EstadoMedo', 'pacman, pastilhas, tempo, medo, visitadas')


class EstadoMedoTotal(EstadoMedo):
    """ A classe para representar a informação que muda com as acções.
    um estado é sempre considerado menor do que qualquer outro. """
    def __lt__(self,x):
        return True
    
    def __eq__(self,outro):
        return self.pacman==outro.pacman and self.pastilhas == outro.pastilhas and \
                self.visitadas == outro.visitadas and self.medo == outro.medo and self.tempo == outro.tempo
    
    def __hash__(self):
        return hash(str(self.pacman)+str(self.pastilhas)+str(self.tempo)+str(self.medo)+str(self.visitadas))


parametros="T=26\nM=6\nP=10"
linha1= "= = = = = = = = = =\n"
linha2= "= @ . * . . * . . =\n"
linha3= "= . = = = = = = . =\n"
linha4= "= . = F . . . . . =\n"
linha5= "= . = . . . . . . =\n"
linha6= "= . = . . . . . . =\n"
linha7= "= . = . . . . . . =\n"
linha8= "= * . . . . . . . =\n"
linha9= "= . . . . . . . . =\n"
linha10="= = = = = = = = = =\n"
grelha=linha1+linha2+linha3+linha4+linha5+linha6+linha7+linha8+linha9+linha10
mundoStandard=parametros + "\n" + grelha

# Distância de Manhatan entre 2 pontos
#
def manhatan(p,q):
    (x1,y1) = p
    (x2,y2) = q
    return abs(x1-x2) + abs(y1-y2)


# A subclasse de Problem: MedoTotal
#
class MedoTotal(Problem):
    """Encontrar um caminho numa grelha 2D com obstáculos. Os obstáculos são células (x, y)."""

    def conv_txt_estado(self,txt):
    
        def processa_linha(dados,y,linha):
            x=0
            for c in linha:
                if c=='*':
                    dados['pastilhas'].add((x,y))
                elif c=='=':
                    dados['obstaculos'].add((x,y))
                elif c=='@':
                    dados['pacman']=(x,y)
                elif c=='F':
                    dados['fantasma']=(x,y)
                if c!= " ":
                    x+=1
        
        linhas=txt.split('\n')
        T=int(linhas[0][2:])
        M=int(linhas[1][2:])
        P=int(linhas[2][2:])
        dim=(len(linhas[3])+1)//2
        
        dados={'dim':dim, 'T':T, 'M':M, 'P':P, 'obstaculos':set(), 'pastilhas':set()}
        y=0
        for l in linhas[3:]:
            processa_linha(dados,y,l)
            y+=1
        return dados
    
        
    def __init__(self, texto_input=mundoStandard):
        diccio=self.conv_txt_estado(texto_input)
        self.initial=EstadoMedoTotal(diccio['pacman'], diccio['pastilhas'], diccio['T'], diccio['M'],{diccio['pacman']:1})
        self.goal=diccio['T'] 
        self.fantasma = diccio['fantasma']
        self.poder = diccio['P']
        self.obstacles=diccio['obstaculos']
        self.dim=diccio['dim']


    directions = {"N":(0, -1), "W":(-1, 0), "E":(1,  0),"S":(0, +1)}  # ortogonais
    
                  
    def result(self, state, action): 
        "Tanto as acções como os estados são representados por pares (x,y)."
        pacman,pastilhas,tempo,medo,visitadas=state
        (x,y) = pacman
        (dx,dy) = self.directions[action]
        npos = (x+dx,y+dy)
        if npos == self.fantasma:
            medo=0
        elif npos in pastilhas:
            pastilhas = pastilhas - {npos}
            medo = self.poder
        else:
            medo -= 1
        tempo -=1
        copia_visitadas = visitadas.copy()
        freq=copia_visitadas.get(npos,0)
        copia_visitadas[npos]=freq+1
        return(EstadoMedoTotal(npos, pastilhas, tempo, medo, copia_visitadas))
    
    

    # situações de falha antecipada
    #
    def falha_antecipada(self,state):
        if state.tempo <= state.medo:
            return False
        if state.pastilhas == set(): # se não há mais pastilhas e eram necessárias
            return True
        minDist = min(list(map(lambda x: manhatan(state.pacman,x),state.pastilhas)))
        if minDist > state.medo: # se não há tempo (manhatan) para chegar à próxima super-pastilha
            return True
        if (state.medo + self.poder * len(state.pastilhas)) < state.tempo:
            # se o poder de todas as pastilhas mais o medo são insuficientes.
            return True
        return False
    
    def actions(self, state):
        """Podes mover-te para uma célula em qualquer das direcções para uma casa 
           que não seja obstáculo nem fantasma."""
        x, y = state.pacman
        return [act for act in self.directions.keys() 
                if (x+self.directions[act][0],y+self.directions[act][1]) not in (self.obstacles | {self.fantasma}) and 
                not self.falha_antecipada(self.result(state,act))]

    
    def path_cost(self,c,state,action,new):
        return c + new.visitadas[new.pacman]
    
    def goal_test(self,state):
        return state.tempo==0

    def display(self, state):
        """ print the state please"""
        output="Tempo: "+ str(state.tempo) + "\n"
        output+="Medo: "+ str(state.medo)  + "\n"
        for j in range(self.dim):
            for i in range(self.dim):
                if state.pacman ==(i,j):
                    ch = '@'
                elif self.fantasma==(i,j):
                    ch = "F"
                elif (i,j) in self.obstacles:
                    ch = "="
                elif (i,j) in state.pastilhas:
                    ch = '*'
                else:
                    ch = "."
                output += ch + " "
            output += "\n"
        return output  

    def executa(p,estado,accoes,verbose=False):
        """Executa uma sequência de acções a partir do estado devolvendo o triplo formado pelo estado, 
        pelo custo acumulado e pelo booleano que indica se o objectivo foi ou não atingido. Se o objectivo for atingido
        antes da sequência ser atingida, devolve-se o estado e o custo corrente.
        Há o modo verboso e o não verboso, por defeito."""
        custo = 0
        for a in accoes:
            seg = p.result(estado,a)
            custo = p.path_cost(custo,estado,a,seg)
            estado = seg
            objectivo=p.goal_test(estado)
            if verbose:
                p.display(estado)
                print('Custo Total:',custo)
                print('Atingido o objectivo?', objectivo)
            if objectivo:
                break
        return (estado,custo,objectivo)
    
    def minimal_h(self,node):
        return node.state.tempo