# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 14:46:26 2023

@author: user
"""


'''GraphsTrees.py'''



class Graph:
    def __init__(self):
        self._graph = {}
        self._vertexNo = 0
    def add_vertex(self, v):
        if v in self._graph:
            print('The vertex Already Exsits!')
        else:
            self._graph[v] = []
            self._vertexNo += 1
    def add_edges(self, v1, v2, w=0):
        if v1 not in self._graph:
            print(f'{v1} does not exist in the graph!')
        elif v2 not in self._graph:
            print(f'{v2} does not exist in the graph!')
        else:
            self._graph[v1].append([v2, w])
            self._graph[v2].append([v1, w])
            
    def __len__(self):
        return len(self._graph)
    def __getitem__(self, v):
        return self._graph[v]
    def show_graph(self):
        return(self._graph)
            
graph = Graph()

graph.add_vertex('Arad')
graph.add_vertex('Zerind')
graph.add_vertex('Timisoara')
graph.add_vertex('Sibiu')
graph.add_vertex('Fagaras')
graph.add_vertex('Rimnicu')
graph.add_vertex('Oradea')
graph.add_vertex('Lugoj')
graph.add_vertex('Mehadia')
graph.add_vertex('Dobreta')
graph.add_vertex('Pitesti')
graph.add_vertex('Craiova')
graph.add_vertex('Bucharest')

graph.add_edges('Arad', 'Zerind', 75)   
graph.add_edges('Arad', 'Timisoara', 118)
graph.add_edges('Arad', 'Sibiu', 140)   
graph.add_edges('Sibiu', 'Fagaras', 99)
graph.add_edges('Sibiu', 'Rimnicu', 80)   
graph.add_edges('Sibiu', 'Oradea', 151)
graph.add_edges('Timisoara', 'Lugoj', 111)
graph.add_edges('Lugoj', 'Mehadia', 70)
graph.add_edges('Mehadia', 'Dobreta', 75)
graph.add_edges('Dobreta', 'Craiova', 120)
graph.add_edges('Rimnicu', 'Pitesti', 97)
graph.add_edges('Craiova', 'Rimnicu', 146)
graph.add_edges('Fagaras', 'Bucharest', 211)
graph.add_edges('Craiova', 'Pitesti', 138)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    