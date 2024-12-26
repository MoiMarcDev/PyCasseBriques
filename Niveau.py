"""
Niveau (plateau de jeu)
"""
import os
import AppConfig

class Niveau:
    def __init__(self,numero:int):
        self._numero = numero
        self._fichier = os.path.join( AppConfig.dossier_niveau,"niveau_"+str(numero)+".csv")
