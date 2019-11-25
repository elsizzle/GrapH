#!/usr/bin/python3 

import sys
import argparse
import requests
import networkx as nx
import matplotlib.pyplot as plt

from helper import *

g = nx.DiGraph()

def main() : 
 
   global g 

   parser = argparse.ArgumentParser()
   parser.add_argument("-s", "--start", help="Account to start graph at.", dest='start')
   parser.add_argument("-d", "--depth", help="Depth to recurse.", type=int, dest='depth')
   args = parser.parse_args()

   g.add_node(args.start)
   recurse(args.start, args.depth)

   nx.draw_networkx(g, nodecolor='w', edge_color='b')
   plt.show()

def recurse (cuser, cdepth) : 
 
   global g
   following = userFollowing(cuser)
   followers = userFollowers(cuser)

   print(cuser, cdepth, following, followers)

   for i in following : 
      g.add_node(i)
      g.add_edge(cuser, i)

   for i in followers : 
      g.add_node(i)
      g.add_edge(i, cuser)

   print(cdepth)
   print(cdepth-1)

   if cdepth > 0 : 
      for i in following : 
         recurse(i, cdepth-1)
      for i in followers : 
         recurse(i, cdepth-1) 

if __name__ == "__main__" : 
   main()
