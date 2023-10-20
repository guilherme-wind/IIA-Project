from MedoTotal import * 
from GrafoAbstracto import *

def ida_star_graph_search_count(problem,f,verbose=False):
    def graph_search_count(problem, frontier, threshold, f):
        expandidos = 0
        frontier.append(Node(problem.initial))
        explored = set()
        new_threshold = infinity
        while frontier:
            node = frontier.pop()
            expandidos+=1
            if problem.goal_test(node.state):
                return (node, expandidos, new_threshold)
            explored.add(node.state)            
            children = node.expand(problem)
            if children:
                children.reverse()
            for child in children:
                if f(child) > threshold and child.state not in explored:
                    new_threshold = min(new_threshold, f(child))
                    expandidos += 1
                    explored.add(child.state)
                elif problem.goal_test(child.state) and f(child) <= threshold and child.state not in explored:
                    return (child, expandidos, threshold)
                elif child.state not in explored and child not in frontier and f(child) < threshold:
                    frontier.append(child)
        return (None, expandidos, new_threshold)

    threshold = f(Node(problem.initial))
    total_expandidos = 0
    while True:
        return_node, expandidos, new_treshhold = graph_search_count(problem, Stack(), threshold, f)
        total_expandidos += expandidos
        threshold = new_treshhold
        if return_node is not None and problem.goal_test(return_node.state):
            return return_node, total_expandidos




s = ProblemaGrafo()
print('---------------- IDA* ----------------')
f=lambda n: n.path_cost + s.h1(n)
res_IDAstar,visitados=ida_star_graph_search_count(s,f)
if res_IDAstar:
    print("\nSolução:",res_IDAstar.solution(),'com custo',res_IDAstar.path_cost)
else:
    print('\nSem Solução')
print('Visitados:',visitados)