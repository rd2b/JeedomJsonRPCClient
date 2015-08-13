#!/usr/bin/env python

""" testapi.py : Description """

__author__ = "Remi Debay"
__date__ = "2015/07/24"


import urllib2
import json

"""
Exemple d'utilisation:

from JeedomJsonRPCClient import handler

api = handler.Handler("192.168.XXX.XXX", "CCCCCCCCCCCCCCC")
print api.ping()
print api.method("object::all")
print api.method("object::full")
"""

class handler:
    parameters = {
          "jsonrpc" : "2.0",
          "method" : "ping",
          "params" : {},
          "id" : "0" }

    headers = { 'Content-Type': 'application/json' }

    def __init__(self, ip, apikey):
        self.ip = ip
        self.parameters["params"]["apikey"] = apikey


    def ping(self):
        self.parameters["method"] = "ping"
        return self.send()

    def send(self):
        data = json.dumps(self.parameters)
        url = "http://%s/core/api/jeeApi.php?request=%s"% ( self.ip, data )
        req = urllib2.Request(url, data, self.headers)
        response = urllib2.urlopen(req)
        fulljson = response.read()
        myjson = json.loads(fulljson)
        return  myjson["result"]

    def method(self, method):
        self.parameters["method"] = method
        return self.send()

    def getstate(self, logicalid):
        """
        Exemple:
        from APIHandler import handler

        api = handler.handler("192.168.0.XXX", "i9fjkfvjkdhvdfjkXXXX")
        print api.getstate("sunrise")
        print api.getstate("firmwareOnline")
        """
        myjson = self.method("object::full")
        for room in myjson:
            for equipement in room["eqLogics"]:
                for cmd in equipement["cmds"]:
                    if cmd["logicalId"] == logicalid:
                        return cmd["state"]

