from MedoTotal import * 
from GrafoAbstracto import *

def ida_star_graph_search_count(problem,f,verbose=False):
    def graph_search_count(problem, frontier, threshold, f):
        frontier.append(Node(problem.initial))
        visited = 1
        explored = set()
        new_threshold = infinity
        while frontier:
            node = frontier.pop()
            if verbose:
                print("\n" + str(node.state))
                print("Cost:", node.path_cost, "f=", f(node))
            if f(node) > threshold:
                new_threshold = min(new_threshold, f(node))
                if verbose:
                    print("Out of cutoff -- minimum out:", f(node))
            elif problem.goal_test(node.state):
                if f(node) <= threshold:
                    if verbose:
                        print("Goal found within cutoff!")
                    return (node, visited, new_threshold)
                elif verbose:
                    print("Out of cutoff -- minimum out:", f(node))
            explored.add(node.state)
            children = node.expand(problem)
            if children and f(node) <= threshold:
                children.reverse()
                for child in children:
                    if child.state not in explored and child not in frontier:
                        frontier.append(child)
                        visited += 1
        return (None, visited, new_threshold)

    threshold = f(Node(problem.initial))
    total_visitados = 0
    while True:
        if verbose:
            print("------Cutoff at", threshold)
        return_node, visitados, new_treshhold = graph_search_count(problem, Stack(), threshold, f)
        total_visitados += visitados
        threshold = new_treshhold
        if return_node is not None and problem.goal_test(return_node.state):
            return return_node, total_visitados
        elif return_node is None and new_treshhold == infinity:
            return None, total_visitados
        if verbose:
            print("\n")





parametros="T=23\nM=7\nP=8"
linha1= "= = = = = = = = = =\n"
linha2= "= @ . . . . * . . =\n"
linha3= "= . = = = = . = . =\n"
linha4= "= . = F * = . . . =\n"
linha5= "= = = = . = . = . =\n"
linha6= "= * = . . . . . . =\n"
linha7= "= . = = = = . = = =\n"
linha8= "= * . . . . . = . =\n"
linha9= "= * . . . . . . . =\n"
linha10="= = = = = = = = = =\n"
grelha=linha1+linha2+linha3+linha4+linha5+linha6+linha7+linha8+linha9+linha10
mundoStandardx=parametros + "\n" + grelha
gx=MedoTotal(mundoStandardx)
print('---------------- IDA* ----------------')
f=lambda n: n.path_cost + gx.minimal_h(n)
res_IDAstar,visitados=ida_star_graph_search_count(gx,f)
if res_IDAstar:
    print("\nSolução:",res_IDAstar.solution(),'com custo',res_IDAstar.path_cost)
else:
    print('\nSem Solução')
print('Visitados:',visitados)

# ---------------- IDA* ----------------

# Solução: ['S', 'N', 'E', 'E', 'E', 'E', 'E', 'S', 'S', 'S', 'S', 'W', 'W', 'N', 'N', 'S', 'S', 'E', 'E', 'E', 'E', 'N', 'N'] com custo 28
# Visitados: 2342