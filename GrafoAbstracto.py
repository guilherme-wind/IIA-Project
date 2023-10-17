from searchPlus import *

class ProblemaGrafo(Problem) :
    grafoDuplo=grafo = {'I':{'A':3,'B':3},
             'A':{'C':1,'D':6},
             'B':{'E':1,'F2':9},
             'C':{'D':4,'I':10},
             'D':{'B':3,'F1':6},
             'F1':{'C':2},
             'E':{'F2':5},
             'F2':{'B':8}}

    hDuplo = {'A':5,'B':5,'C':3,'D':7,'E':4,'F1':0,'F2':0, 'I':10 }


    def __init__(self,initial = 'I', goal = ['F1','F2'],grafo=grafoDuplo,h=hDuplo) :
        super().__init__(initial,goal)
        self.grafo=grafo
        self.h=h
        
    def actions(self,estado) :
        sucessores = self.grafo[estado].keys()  # métodos keys() devolve a lista das chaves do dicionário
        accoes = list(map(lambda x : "ir de {} para {}".format(estado,x),sucessores))
        return accoes

    def result(self, estado, accao) :
        """Assume-se que uma acção é da forma 'ir de X para Y'
        """
        return accao.split()[-1]
    
    def path_cost(self, c, state1, action, state2):
        return c + self.grafo[state1][state2]
    
    def display(self,state):
        return state

    def h1(self,no) : 
        """Uma heurística é uma função de um estado.
        Nesta implementação, é uma função do estado associado ao nó
        (objecto da classe Node) fornecido como argumento.
        """
        
        return self.h[no.state]