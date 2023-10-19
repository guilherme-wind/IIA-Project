from MedoTotal import *
from searchPlus import *

def depth_first_tree_search_all_count(problem, optimal=False, verbose=False):
    def search(problem, frontier, optimal, verbose):
        resultado = Node(state=None, path_cost=infinity)
        max_mem = 0
        visitados = 0
        finais = 0
        frontier.append(Node(problem.initial))
        while frontier:
            node = frontier.pop()
            max_mem = max(max_mem, len(frontier))
            if optimal and node.path_cost >= resultado.path_cost:
                continue
            if (verbose):
                print('-'*21, "\n")
                print(problem.display(node.state))
            visitados += 1
            if problem.goal_test(node.state):
                if verbose:
                    print("GGGGooooooallllll --------- com o custo:", node.path_cost)
                finais += 1
                if node.path_cost < resultado.path_cost:
                    if (verbose):
                        print("Di best goal até agora")
                    resultado = node
            else:
                if verbose:
                    print("Custo:", node.path_cost)
                children = list(node.expand(problem))
                if children:
                    children.reverse()
                if optimal:
                    children = list(filter(lambda c: c.path_cost < resultado.path_cost, children))
                frontier.extend(children)
            # print("CHILDREN =", len(children))
            # print("MEMÓRIA MAX=", max_mem)
        return (resultado, max_mem, visitados, finais)

    resultado, max_mem, visitados, finais = search(problem, Stack(), optimal, verbose)

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
print('*'*20)
resultado,max_mem,visitados,finais = depth_first_tree_search_all_count(gx,True,True)

if resultado:
    print("Solução Prof-total (árvore) com custo", str(resultado.path_cost)+":")
    print(resultado.solution())
else:
    print('\nSem Solução')
print('Visitados=',visitados)
print('Dimensão máxima da memória',max_mem)
print('Estados finais:',finais)