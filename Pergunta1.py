from MedoTotal import *
from searchPlus import *


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


class DistancePoints(Problem):
        directions = {"N":(0, -1), "W":(-1, 0), "E":(1,  0),"S":(0, +1)}  # ortogonais

        def __init__(self, p1, p2, obstacles, fantasma):
            self.initial = p1
            self.goal = p2
            self.obstacles = obstacles
            self.fantasma = fantasma

        def actions(self, state):
            x, y = state
            return [act for act in self.directions.keys() 
                if (x+self.directions[act][0],y+self.directions[act][1]) not in (self.obstacles | {self.fantasma})]

        def goal_test(self, state):
            if isinstance(self.goal, list):
                return state in self.goal
            else:
                return state == self.goal

        def h(self, state):
            x, y = state.state
            return abs(x - self.goal[0]) + abs(y - self.goal[1])
        
        def path_cost(self,c,state1,action,state2):
            x1, y1 = state1
            x2, y2 = state2
            return c + abs(x2 - x1) + abs(y2 - y1)
        
        def result(self, state, action): 
            x, y = state
            return (x+self.directions[action][0],y+self.directions[action][1])


class MedoTotalTurbo(MedoTotal):
    """Encontrar um caminho numa grelha 2D com obstáculos. Os obstáculos são células (x, y)."""
    
        
    def __init__(self, texto_input=mundoStandard):
        super().__init__(texto_input)
    

    def distancia_entre_pontos(self, p1, p2):
        distancia = DistancePoints(p1, p2, self.obstacles, self.fantasma)

        # Call the astar_search() function to get the shortest path between the two points.
        path = astar_search(distancia)
        # The cost of the path is the distance between the two points.
        return path.path_cost


    # situações de falha antecipada
    #
    def falha_antecipada(self,state):
        if state.tempo <= state.medo:
            return False
        if state.pastilhas == set(): # se não há mais pastilhas e eram necessárias
            return True
        minDist = min(list(map(lambda x: self.distancia_entre_pontos(state.pacman,x),state.pastilhas)))
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





parametros="T=4\nM=2\nP=10"
linha1= "= = = = = =\n"
linha2= "= @ F * . =\n"
linha3= "= . = . . =\n"
linha4= "= . . . . =\n"
linha5= "= . = = . =\n"
linha6= "= = = = = =\n"
grelha=linha1+linha2+linha3+linha4+linha5+linha6
mundoStandardx=parametros + "\n" + grelha
gx=MedoTotalTurbo(mundoStandardx)
print(gx.actions(gx.initial))