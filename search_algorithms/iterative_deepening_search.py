from collections import deque
from .expand import expand
from .node import Node


def depth_limited_search(problem, l):
    node = Node(problem.initial)
    frontier = deque([node])
    reached = {problem.initial[0]: node}
    result = None

    while frontier:
        node = frontier.pop()
        if problem.is_goal(node.state):
            return node

        if node.depth >= l:
            if node.depth > l:
                result = "cutoff"
            continue

        if node.state[0] not in reached.keys() or node.depth < reached[node.state[0]].depth:
            reached[node.state[0]] = node
            for child in expand(problem, node):
                s = child.state
                frontier.append(child)

    print(frontier)
    return None if result == "cutoff" and not frontier else result


def iterative_deepening_search(problem):
    depth = 0
    while True:
        print("Current depth:", depth)
        result = depth_limited_search(problem, depth)
        if result == "cutoff":
            depth += 1
        else:
            return result


'''
def iterative_deepening_search(problem) returns node or failure
    for depth = 0 to infinity
        result <- DEPTH-LIMITED-SEARCH(problem, depth)
        if result != cutoff
            return result


def depth_limited_search(problem, l) returns node or failure or cutoff
    frontier <- LIFO queue (stack) with NODE(problem.INITIAL) as element
    result <- failure

    while frontier
        node <- POP(frontier)
        if problem.IS-GOAL(node.STATE)
            return node
        if DEPTH(node) > l
            result <- cutoff
        else if not IS-CYCLE(node)
            for child in EXPAND(problem, node)
                add child to frontier
    return result
'''
