#!/usr/bin/python3 

import requests
from private import token as apikey

url  = 'https://api.github.com'
head = {'Authorization': 'token {}'.format(apikey)}

#response = requests.get(url + '/users/tomsom', headers=head)

def userFollowing (uname) :
   fr = []
   r = requests.get(url + "/users/" + uname + "/following", headers=head)
   fd = r.json()
   for i in fd :
      fr.append(i["login"])
   return(fr)

def userFollowers (uname) :
   fr = []
   r = requests.get(url + "/users/" + uname + "/followers", headers=head)
   fd = r.json()
   for i in fd :
      fr.append(i["login"])
   return(fr)
