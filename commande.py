# -*- coding: ISO-8859-1 -*-

def parseCommande(commande):
	if commande == "/quit":
		return True, "client-deconnection", []
	elif commande == "/shutdown":
		return True, "fermer-serveur", []
	else:
		return False, commande, []