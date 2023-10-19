from MedoTotal import *
from searchPlus import *

def depth_first_tree_search_all_count(problem, optimal=False, verbose=False):
    
    def search(problem, frontier, optimal, verbose):
        
        max_mem = 0
        visitados = 0
        finais = 0
        frontier.append(Node(problem.initial))

        if problem.goal_test(problem.initial):
            resultado = Node(problem.initial)
        else:
            resultado = Node(state=None, path_cost=infinity)
        
        while frontier:
            node = frontier.pop()
            visitados += 1
            if (verbose):
                print('-'*21, "\n")
                print(problem.display(node.state))
                print("Custo:", node.path_cost)
            children = list(node.expand(problem))

            for c in list(children):
                if optimal and c.path_cost >= resultado.path_cost:
                    children.remove(c)
                elif problem.goal_test(c.state):
                    visitados += 1
                    if verbose:
                        print('-'*21, "\n")
                        print(problem.display(c.state))
                        print("GGGGooooooallllll --------- com o custo:", c.path_cost)
                    finais += 1
                    if c.path_cost < resultado.path_cost:
                        if (verbose):
                            print("Di best goal até agora")
                        resultado = c
                    children.remove(c)

            if children:
                children.reverse()
            frontier.extend(children)
            max_mem = max(max_mem, len(frontier))

        return (resultado, max_mem, visitados, finais)

    resultado, max_mem, visitados, finais = search(problem, Stack(), optimal, verbose)
    if resultado.path_cost == infinity:
        resultado = None
    return resultado, max_mem, visitados, finais






	
parametros="T=6\nM=4\nP=10"
linha1= "= = = = = =\n"
linha2= "= . @ F * =\n"
linha3= "= . . . . =\n"
linha4= "= . = . . =\n"
linha5= "= . = . . =\n"
linha6= "= = = = = =\n"
grelha=linha1+linha2+linha3+linha4+linha5+linha6
mundoStandardx=parametros + "\n" + grelha
gx=MedoTotal(mundoStandardx)

resultado,max_mem,visitados,finais = depth_first_tree_search_all_count(gx,False,True)
print('*'*20)
if resultado:
    print("Solução Prof-total (árvore) com custo " + str(resultado.path_cost)+":")
    print(resultado.solution())
else:
    print('\nSem Solução')
print('Visitados=',visitados)
print('Dimensão máxima da memória',max_mem)
print('Estados finais:',finais)