from MedoTotal import * 
from GrafoAbstracto import *

def ida_star_graph_search_count(problem,f,verbose=False):
    def depth_limited_search(problem, limit=5):
        def recursive_dls(node, problem, limit):
            if problem.goal_test(node.state):
                return node
            elif limit == 0:
                return 'cutoff'
            else:
                cutoff_occurred = False
                for child in node.expand(problem):
                    result = recursive_dls(child, problem, limit - 1)
                    if result == 'cutoff':
                        cutoff_occurred = True
                    elif result is not None:
                        return result
                return 'cutoff' if cutoff_occurred else None

        # Body of depth_limited_search:
        return recursive_dls(Node(problem.initial), problem, limit)
    
    initial_node = Node()
