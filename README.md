# python-JeedomJsonRPCClient
Python client for Jeedom's JsonRPC : https://www.jeedom.fr/wiki/index.php?title=API_JSONRPC_2.0


Here is how to connect to your Jeedom's API, and request some data:
```
from APIHandler import handler                                                  

api = handler.handler("192.168.0.XXX", "MYAPIKEYDDDDDDDD")                  
#print api.ping()                                                               
#print api.method("object::all")                                                

import pprint, json                                                             
fulljson = api.method("object::full")                                           

myjson = json.loads(fulljson)                                                   
#print(json.dumps(myjson, indent=4, sort_keys=True) )                           

for room in myjson["result"]:
    print room["name"]
    for equipement in room["eqLogics"]:                                         
        print ("%s->%s"%(room["name"], equipement["name"]))                     
        for cmd in equipement["cmds"]:                                          
            if cmd.has_key("state"):                                            
                print ("%s->%s %s : %s"%(room["name"], equipement["name"], cmd["logicalId"],  cmd["state"]))
                                                                                
fulljson = api.method("eqLogic::all")                                           
myjson = json.loads(fulljson)                                                   
for equipement in myjson["result"]:                                             
    print ("%s"%( equipement["name"]))                                          
```
