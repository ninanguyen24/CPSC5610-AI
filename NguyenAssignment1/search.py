# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    #SuccessorNode = [(startState,[Direction],cost int)]

    
    fringeStack = util.Stack()
    visited = [] #sets will throw you off
    SuccessorNode = (problem.getStartState(),[],0)
    fringeStack.push(SuccessorNode)
    
    while not fringeStack.isEmpty():
        node = fringeStack.pop() #LIFO
        state = node[0]
        direction = node[1]
        cost = node[2]
        
        if problem.isGoalState(state):
            return direction
        
        if state not in visited:
            visited.append(state)
        
            for successor in problem.getSuccessors(state):
                childNode = successor[0]
                childDirection = direction + [successor[1]] #Add the moves to Direction list
                childCost = cost + successor[2] #Add up the total costs
                
                fringeStack.push((childNode,childDirection,childCost))
    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    fringeQ = util.Queue()
    #visited = set()
    visited = []
    SuccessorNode = (problem.getStartState(),[],0)
    fringeQ.push(SuccessorNode)
    
    while not fringeQ.isEmpty():
        node = fringeQ.pop() #FIFO
        state = node[0]
        direction = node[1]
        cost = node[2]
        
        if problem.isGoalState(state):
            return direction
        
        if state not in visited:
            visited.append(state)
        
            for successor in problem.getSuccessors(state):
                childNode = successor[0]
                childDirection = direction + [successor[1]] #Add the moves to Direction list
                childCost = cost + successor[2] #Add up the total costs
                
                fringeQ.push((childNode,childDirection,childCost))
        
    
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first.
    
    By changing the cost function, we can encourage Pacman to find different paths.
    For example, we can charge more for dangerous steps in ghost-ridden areas or 
    less for steps in food-rich areas, and a rational Pacman agent should adjust
    its behavior in response.

    Implement the uniform-cost graph search algorithm in the uniformCostSearch
    function in search.py. We encourage you to look through util.py for some
    data structures that may be useful in your implementation. You should now
    observe successful behavior in all three of the following layouts, where
    the agents below are all UCS agents that differ only in the cost function
    they use (the agents and cost functions are written for you):

    python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
    python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
    python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
    """
    
    "*** YOUR CODE HERE ***"
    priorityQ = util.PriorityQueue()
    visited = []
    SuccessorNode = (problem.getStartState(),[],0)
    priorityQ.push(SuccessorNode,0)
    
    
    while not priorityQ.isEmpty():
        node = priorityQ.pop()
        state = node[0]
        direction = node[1]
        cost = node[2]
        
        if problem.isGoalState(state):
            return direction
        
        if state not in visited:
            visited.append(state)
        
            for successor in problem.getSuccessors(state):
                childNode = successor[0]
                childDirection = direction + [successor[1]] #Add the moves to Direction list
                childCost = cost + successor[2] #Add up the total costs
                
                priorityQ.push((childNode,childDirection,childCost),childCost)
    
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first.
    
    python pacman.py -l tinyMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
    python pacman.py -l mediumMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
    python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
    """
    "*** YOUR CODE HERE ***"
    priorityQ = util.PriorityQueue()
    visited = []
    SuccessorNode = (problem.getStartState(),[],0)
    
    #heuristic takes a state and problem as parameter. Like above.
    parentHeu = heuristic(problem.getStartState(), problem) #from searchAgent.py
    totalCost = 0 + parentHeu
    priorityQ.push(SuccessorNode,totalCost)
    
    
    while not priorityQ.isEmpty():
        node = priorityQ.pop()
        state = node[0]
        direction = node[1]
        cost = node[2]

        if problem.isGoalState(state):
            return direction
        
        if state not in visited:
            visited.append(state)
            
            for successor in problem.getSuccessors(state):
                childNode = successor[0]
                childDirection = direction + [successor[1]] #Add the moves to Direction list
                childCost = cost + successor[2] #add up the total costs
                
                """Note to future self:DON't MAKE THE ATTRIBUTE ABOVE NAMED "heuristic" and then
                called the function heuristic below. You spent 2 hours debugging the 
                "INT OBJECT IS NOT CALLABLE" ERROR
                """
                childHeuristic = heuristic(childNode, problem) 
                childTotal = childCost + childHeuristic
                
                priorityQ.push((childNode, childDirection, childCost), childTotal)
    
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
