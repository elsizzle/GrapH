#!/usr/bin/python3

import sys
import requests
import networkx as nx 
import matplotlib.pyplot as plt

from helper import * 

start = sys.argv[1]
#depth = sys.argv[2]

g = nx.DiGraph()
g.add_node(start)

for i in userFollowing(start) : 
   g.add_node(i)
   g.add_edge(start, i)

for i in userFollowers(start) : 
   g.add_node(i)
   g.add_edge(i, start)

nx.draw_networkx(g, pos=nx.circular_layout(g), nodecolor='w', edge_color='b')
plt.show()

