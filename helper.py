#!/usr/bin/python3 

import requests

def userFollowing (uname) :
   fr = []
   r = requests.get("https://api.github.com/users/" + uname + "/following")
   fd = r.json()
   for i in fd :
      fr.append(i["login"])
   return(fr)

def userFollowers (uname) :
   fr = []
   r = requests.get("https://api.github.com/users/" + uname + "/followers")
   fd = r.json()
   for i in fd :
      fr.append(i["login"])
   return(fr)

