from utils import *

class Node:

    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state.  Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node.  Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """[Figure 3.10]"""
        next = problem.result(self.state, action)
        return Node(next, self, action,
                    problem.path_cost(self.path_cost, self.state,
                                      action, next))

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    # We want for a queue of nodes in breadth_first_search or
    # astar_search to have no duplicated states, so we treat nodes
    # with the same state as equal. [Problem: this may not be what you
    # want in other contexts.]

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)

class Problem:

    """The abstract class for a formal problem.  You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value.  Hill-climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError

class Graph:

    """A graph connects nodes (verticies) by edges (links).  Each edge can also
    have a length associated with it.  The constructor call is something like:
        g = Graph({'A': {'B': 1, 'C': 2})
    this makes a graph with 3 nodes, A, B, and C, with an edge of length 1 from
    A to B,  and an edge of length 2 from A to C.  You can also do:
        g = Graph({'A': {'B': 1, 'C': 2}, directed=False)
    This makes an undirected graph, so inverse links are also added. The graph
    stays undirected; if you add more links with g.connect('B', 'C', 3), then
    inverse link is also added.  You can use g.nodes() to get a list of nodes,
    g.get('A') to get a dict of links out of A, and g.get('A', 'B') to get the
    length of the link from A to B.  'Lengths' can actually be any object at
    all, and nodes can be any hashable object."""

    def __init__(self, dict=None, directed=True):
        self.dict = dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        """Make a digraph into an undirected graph by adding symmetric edges."""
        for a in list(self.dict.keys()):
            for (b, dist) in self.dict[a].items():
                self.connect1(b, a, dist)

    def connect(self, A, B, distance=1):
        """Add a link from A and B of given distance, and also add the inverse
        link if the graph is undirected."""
        self.connect1(A, B, distance)
        if not self.directed:
            self.connect1(B, A, distance)

    def connect1(self, A, B, distance):
        """Add a link from A to B of given distance, in one direction only."""
        self.dict.setdefault(A, {})[B] = distance

    def get(self, a, b=None):
        """Return a link distance or a dict of {node: distance} entries.
        .get(a,b) returns the distance or None;
        .get(a) returns a dict of {node: distance} entries, possibly {}."""
        links = self.dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    def nodes(self):
        """Return a list of nodes in the graph."""
        return list(self.dict.keys())

def UndirectedGraph(dict=None):
    """Build a Graph where every edge (including future ones) goes both ways."""
    return Graph(dict=dict, directed=False)

class GraphProblem(Problem):

    """The problem of searching a graph from one node to another."""

    def __init__(self, initial, goal, graph):
        Problem.__init__(self, initial, goal)
        self.graph = graph

    def actions(self, A):
        """The actions at a graph node are just its neighbors."""
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        """The result of going to a neighbor is just that neighbor."""
        return action

    def path_cost(self, cost_so_far, A, action, B):
        return cost_so_far + (self.graph.get(A, B) or infinity)

    def find_min_edge(self):
        """Find minimum value of edges."""
        m = infinity
        for d in self.graph.dict.values():
            local_min = min(d.values())
            m = min(m, local_min)

        return m

    def h(self, node):
        """h function is straight-line distance from a node's state to goal."""
        locs = getattr(self.graph, 'locations', None)
        if locs:
            if type(node) is str:
                return int(distance(locs[node], locs[self.goal]))

            return int(distance(locs[node.state], locs[self.goal]))
        else:
            return infinity

class NewGraphProblem(GraphProblem):

    "The problem of searching a graph from one node to another."

    def __init__(self, initial, goal, graph):
        Problem.__init__(self, initial, goal)
        self.graph = graph

    def actions(self, A):
        "The actions at a graph node are operators such as Left, Right, Suck, etc."
        return list(self.graph.get(A).keys())

    def result(self, state, action):  # state is the name of a graph node,which really does not describe the state
        (new_state, distance) = self.graph.get(state)[action]
        return new_state

    def path_cost(self, cost_so_far, A, action, B):
        (new_state, distance) = self.graph.get(A)[action]
        return int(cost_so_far + (distance or infinity))

    # def h(self, node):
    #     percts  = getattr(self.graph, 'percepts', None)
    #     if percts:
    #         perc = percts[node.state]
    #         if perc[0]== perc[1]==perc[2]== 0:
    #             return int(0)
    #         sum1 = perc[0]+perc[1]+perc[2]
    #         Loc = perc[3]
    #         if sum1 == 3 and Loc >= 4:
    #             return int(2*sum1 + 2*sum1-1+4*(sum1-1)+4)
    #         if sum1 == 3 and Loc < 4:
    #             return int(2*sum1-1+4*(sum1-1)+4)
    #         if sum1 == 2 and Loc >= 4:
    #             return int(2*sum1 + 2*sum1-1+4)
    #         if sum1 ==2 and  Loc <4:
    #             return int(2*sum1-1+4)
    #         if sum1 == 1 and Loc >= 4:
    #             return 2+1
    #         if sum1 == 1 and Loc  <4:
    #             return int(1)
    #     else:
    #         return infinity


    def h(self, node):
        percts  = getattr(self.graph, 'percepts', None)
        if percts:
            perc = percts[node.state]
            if perc[0]== perc[1]==perc[2]== 0:
                return int(0)
            sum1 = perc[0]+perc[1]+perc[2]
            Loc = perc[3]
            if sum1 == 3 and Loc >= 4:
                return int(sum1 + sum1-1+2*(sum1-1))
            if sum1 == 3 and Loc < 4:
                return int(sum1-1)
            if sum1 == 2 and Loc >= 4:
                return int(2*sum1)
            if sum1 ==2 and  Loc <4:
                return int(sum1+2)
            if sum1 == 1 and Loc >= 4:
                return 2
            if sum1 == 1 and Loc  <4:
                return int(1)
        else:
            return infinity


def best_first_graph_search(problem, f):
    iterations = 0
    f = memoize(f, 'f')
    node = Node(problem.initial)
    iterations += 1
    if problem.goal_test(node.state):
        iterations += 1
        return(iterations, node)

    frontier = PriorityQueue(min, f)
    frontier.append(node)
    iterations += 1
    explored = set()
    while frontier:
        node = frontier.pop()
        iterations += 1
        if problem.goal_test(node.state):
            iterations += 1
            return(iterations, node)
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
                iterations += 1
            elif child in frontier:
                incumbent = frontier[child]
                if f(child) < f(incumbent):
                    del frontier[incumbent]
                    frontier.append(child)
                    iterations += 1
        iterations += 1
    return None

def astar_search(problem, h=None):
    h = memoize(h or problem.h, 'h')
    iterations, node = best_first_graph_search(problem, lambda n: n.path_cost + h(n))
    return(iterations, node)
