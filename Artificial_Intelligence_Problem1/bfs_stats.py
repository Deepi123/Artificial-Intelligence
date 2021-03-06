#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
vanilla breadth first search
- relies on  Puzzle8.py module
"""

import Puzzle8
from Puzzle8 import*

 #### ++++++++++++++++++++++++++++++++++++++++++++++++++++
 #### breadth_first_search_stats

def breadth_first_search_stats():
    #print('Stats')
    print('Total Nodes expanded:' ,nodes_expanded)
    print('Total Nodes generated:' ,nodes_generated)
    print('Maximum queue length:' ,max_queue_length)
    print('Length of solution Path:' ,length_solution_path)


 #### ++++++++++++++++++++++++++++++++++++++++++++++++++++
 #### breadth first search


nodes_expanded=0;
nodes_generated=0;
max_queue_length=0;
max_queue_length_before_deletion=0;

def breadth_first_search(problem):
    global nodes_expanded
    global nodes_generated
    global max_queue_length
    #global max_queue_length_before_deletion
    global length_solution_path

    queue =deque([])
    root=TreeNode(problem,problem.initial_state)
    queue.append(root)
    while len(queue)>0:
        #Make sure maximum length of queue is captured
        if max_queue_length<len(queue):
            max_queue_length=len(queue)

        next=queue.popleft()
        if next.goalp():
            del(queue)
            return next.path()
        else:
            new_nodes=next.generate_new_tree_nodes()
            nodes_expanded+=1 #increment counter once you expand the node
            for new_node in new_nodes:
                queue.append(new_node)
                nodes_generated+=1 #increment counter for every new node generated
    print('No solution')
    return NULL


problem=Puzzle8_Problem(Example1)
output=  breadth_first_search(problem)
print('Solution Example 1:')
print_path(output)
length_solution_path=len(output)
breadth_first_search_stats()

# wait = input("PRESS ENTER TO CONTINUE.")

# problem=Puzzle8_Problem(Example2)
# output=  breadth_first_search(problem)
# print('Solution Example 2:')
# print_path(output)
# length_solution_path=len(output)
# breadth_first_search_stats()

#wait = input("PRESS ENTER TO CONTINUE.")

# problem=Puzzle8_Problem(Example3)
# output=  breadth_first_search(problem)
# print('Solution Example 3:')
# print_path(output)
# length_solution_path=len(output)
# breadth_first_search_stats()

# wait = input("PRESS ENTER TO CONTINUE.")

# problem=Puzzle8_Problem(Example4)
# output=  breadth_first_search(problem)
# print('Solution Example 4:')
# print_path(output)
# length_solution_path=len(output)
# breadth_first_search_stats()

# Solution to Example 5 may take too long to calculate using vanilla bfs
# problem=Puzzle8_Problem(Example5)
# output=  breadth_first_search(problem)
# print('Solution Example 5:')
# print_path(output)
