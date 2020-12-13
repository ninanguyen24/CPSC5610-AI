# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 12:46:15 2019

@author: hanks
"""

"""
Nina Nguyen
CPSC 5610 - AI
February 23, 2019
Assignment 2 (Problem 1)
"""

##  This method is called from Boards.py -- the two inputs are
##    -- initial cell assignments, a list of length N where N is 
##       the problem size (number of rows = number of columns = number
##       of streams = length of each stream).  For example, for a game
##       of size three,  this assigns the value i to the cells on 
##       the diagonal:   [[1,0,0], [0,2,0], [0,0,3]]   -- the value
##       of 0 means the initial value for that cell should be unassigned
##
##    -- streams:  a list of length N, each element is a stream, which 
##       is a list of N coordinates.  For example for N=3:
##          [[(1,1), (2,2), (1,3)], [(1,2), (2,3), (3,3)], [(2,1), (3,1), (3,2)]]
##       Notice that every legal coordinate appears in a stream exactly
##       once, and that the streams are "contiguous" in the sense that 
##       every coordinate is connected to another coordinate either by
##       a row, a column or a diagonal
##
##  Indexing convention:  (row, col) where (1,1) is at the upper left, 
##    (1,2) is one to the right, (2,1) is one down, and (N,N) is at the 
##    upper left
##
##  The return value is exactly the return value from the Python constraints library method
##   getSolutions -- a list of solutions;  each solution is a dictionary 
##   with a key being a coordinate and the value being a value assigned
##   to the cell with that coordinate

from constraint import *

def solveProblem(inits, streams):
    initialValues = inits #
    size = len(inits)+1
    problem = Problem() 
    
    #create each (row,col) on the board and add to variable
    for i in range(1, size):
        for j in range(1,size):
            problem.addVariable((i,j),range(1,size))
    
    #Add constraint for Initial Values
    addInitialValueConstraints(problem,initialValues)
    
    var = 1        
    for i in range(1, size):
        #Create each row to add to constraint
        rowInd = [(var,col) for col in range(1,size)]
        #Add the row to the constraint
        problem.addConstraint(AllDifferentConstraint(), rowInd)
        #Create each column to add to constraint 
        colInd = [(row, var) for row in range(1,size)]
        #Add the column to the constraint
        problem.addConstraint(AllDifferentConstraint(), colInd)
        var += 1
    
    #Add each stream to the constraint
    for i in range(size-1):
        problem.addConstraint(AllDifferentConstraint(),streams[i])
        
    
    return problem.getSolutions()

def addInitialValueConstraints(problem,initialValues):
    size = len(initialValues)
    for i in range(0,size):
        for j in range(0,size):
            if initialValues[i][j] !=0:
                addEqualsConstraint(problem,(j+1,i+1), initialValues[i][j])

def addEqualsConstraint(problem, coord, value):
    problem.addConstraint(lambda c:c == value,[coord])
