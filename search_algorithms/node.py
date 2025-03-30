class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        '''
        self.state <- state to which node corresponds,
                                            tuple (block, board_layout)
        self.parent <- node in the tree that generates this node
        self.action <- action that was applied to the parent's node to
                                            generate this node
        self.path_cost <- total cost of the path from the initial state
                                            to this node
        '''
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __lt__(self, other):
        return self.path_cost < other.path_cost
