from collections import deque
from .node import Node
from .expand import expand
from pprint import pprint


def breadth_first_search(problem):
    node = Node(problem.initial)
    if problem.is_goal(node.state):
        return node

    frontier = deque([node])
    reached = {problem.initial[0]: node}

    print("_______________INITIAL_________________")
    print(problem.initial[0])
    pprint(problem.initial[1])

    while frontier:
        node = frontier.popleft()
        for child in expand(problem, node):
            s = child.state
            if problem.is_goal(s):
                return child

            if s[0] not in reached.keys():
                reached[s[0]] = child
                frontier.append(child)

    return None


'''
def breadth_first_search(problem) return solution node or failure
    node <- NODE(problem.INITIAL)
    if problem.IS_GOAL(node.state) return node
    frontier <- FIFO queue, with node as an element
    reached <- {problem.INITIAL}
    while frontier:
        node <- POP(frontier)
        for child in EXPAND(problem, node)
            s <- child.STATE
            if problem.IS_GOAL(s) return child
            if s not in reached
                add s to reached
                add child to frontier
'''
