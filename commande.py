# -*- coding: ISO-8859-1 -*-
'''
Méthode pour vérifier si le client à demandé un action au serveur
Par Jean-Sebastien Fauteux
commande.py
'''

def parseCommande(commande):
	commande = commande.split("\r")[0]
	if commande == "/quit":
		return True, "client-deconnection", []
	elif commande == "/shutdown":
		return True, "fermer-serveur", []
	else:
		return False, commande, []