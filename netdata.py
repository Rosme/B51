# -*- coding: ISO-8859-1 -*-
'''
Classe englobante pour le transfert de donnees sur le reseau
Par Jean-Sebastien Fauteux
netdata.py
'''


class ListClientInfo():
    def __init__(self):
        self.list = list()

class MsgQueue():
    def __init__(self):
        self.msg = []

class ClientInfo():
    def __init__(self, id, nom, race):
        self.nom = nom
        self.id = id
        self.race = race

class StartGameMsg():
    def __init__(self):
        self.msg = "StartGame";

class ClientDisconnect():
    #id du joueur
    def __init__(self, listId):
        self.listId = listId

class ClientTickInfo():
    #Id du joueur, frame, list des events
    def __init__(self, id, tick, events):
        self.id = id
        self.tick = tick
        self.events = events

class ClientTickData():
    #Id du joueur, list des events
    def __init__(self, id, events):
        self.id = id
        self.events = events;
'''
class ClientListTick():
    def __init__(self, list):
        self.list = list

class TotalTickInfo():
    #Frame, ClientTickData
    def __init__(self, tick, listEvents):
        self.tick = tick
        self.listEvents = listEvents

class NoConnect():
    def __init__(self):
        self.msg = "Aucune connection disponible"
'''
class ClientId():
    #ID du joueur
    def __init__(self, id):
        self.id = id

class ClientTireInfo():
    def __init__(self,finX,finY):
        self.finX = finX
        self.finY = finY

class LeverModifier():
    def __init__(self, matX, matY, nomMap):
        self.x = matX
        self.y = matY
        self.nomMap = nomMap

class SwitchModifier():
    def __init__(self, matX, matY, nomMap):
        self.x = matX
        self.y = matY
        self.nomMap = nomMap

class Seed():
    def __init__(self,seed):
        self.seed=seed