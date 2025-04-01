from .node import Node


def expand(problem, node):
    s = node.state
    generated_nodes = set()

    for action in problem.actions(s):
        print(action)
        s_prime = problem.result(s, action)
        cost = node.path_cost + problem.action_cost(s, action, s_prime)
        depth = node.depth + 1
        generated_nodes.add(Node(s_prime, parent=node, action=action, path_cost=cost, depth=depth))

    return generated_nodes


'''
def EXPAND(problem, node) return node
    s <- node.STATE
    for action in problem.ACTIONS(s)
        s' <- problem.RESULT(s, action)
        cost <- node.PATH-COST + problem.ACTION-COST(s, action, s')
        return NODE(STATE=s', PARENT=node, ACTION=action, PATH-COST=cost)
'''
