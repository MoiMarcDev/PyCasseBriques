import csv
import os

import pygame

import AppConfig

"""Caractéristiques et liste des éléments pouvant être positionnés sur la grille de jeu"""

class ElementItem:
    def __init__(self, dict_data:dict):
        """Initalizer
        Args:
            dict_data (dict): Contient, sous forme de dictionnaire, une ligne du fichier CSV (les clefs du dictionnaire étant les items de la ligne d'entête du fichier)
        """
        self._dict_data = dict_data
        self.identifiant:str = dict_data["Identifiant"]
        self.durete:int = int(dict_data["Durete"])
        self.images:list[str] = ( dict_data["Image"], dict_data["Image_impact_1"], dict_data["Image_impact_2"] )
        self.surfaces:list[pygame.surface.Surface] = [
            pygame.image.load( os.path.join( AppConfig.dossier_img, x ) ) for x in self.images if x is not None and x.strip() != ""
        ]
        self.largeur:int = self.surfaces[0].get_width()
        self.hauteur:int = self.surfaces[0].get_height()
        #.convert_alpha()
        
    def __repr__(self)->str:
        return f"{type(self)} → identifiant={self.identifiant}; durete={self.durete}; largeur={self.largeur}; hauteur={self.hauteur}; images={self.images}; surfaces={id(self.surfaces)}"
        
class ElementList:
    def __init__(self, nom_fichier_csv:str):
        """Initializer
        Args:
            nom_fichier_csv (str): Nom complet (avec chemin) di fichier CSV des éléments ; le fichier doit être strcutré comme décrit dans la ligne d'entête 
            Cette ligne d'entête doit être 1) présente et 2) égale à : "Identifiant;Durete;Largeur;Image;Image_impact_1;Image_impact_2"
            Les informations étant de type: chaine;entier;entier;chaine(nom du fichier sans chemain);chaine;chaine
        """
        self._nom_fichier_csv:str = nom_fichier_csv
        
        self._elements:list[ElementItem] = []
        with open(self._nom_fichier_csv, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                self._elements.append(ElementItem(row))
        
    def __iter__(self):
        """Fournir un itérateur"""
        for x in self._elements:
            yield x

    def get_element(self, identifiant:str) -> ElementItem:
        """Retourne un item à partir de son idendifiant
        Args:
            identifiant (str): nom (identifiant) à rechercher
        Raises:
            KeyError: si idnetifiant non trouvé
        Returns:
            ElementItem: l'élément correspondant à l'identifiant recherché
        """
        for x in self._elements:
            if x.identifiant == identifiant:
                return x
            
        raise KeyError # Non trouvé
    
    def get_surface(self, identifiant:str, durete_actuelle:int|None=None) -> pygame.surface.Surface:
        """Retourne la surface pour un élément, en fonction de son identifiant et de sa duretée actuelle (si précisée)
        Args:
            identifiant (str): nom (identifiant) à rechercher
            durete_actuelle (int | None, optional): duretée actuelle. Defaults to None.
        Returns:
            pygame.surface.Surface: la surface correspondante
        """
        elt:ElementItem = self.get_element(identifiant)
        if elt.durete in [0,1]: return elt.surfaces[0]
        index:int = 0 if durete_actuelle is None else elt.durete - durete_actuelle
        return elt.surfaces[index]
    
#############################

if __name__ == "__main__":
    import AppConfig
    el = ElementList(AppConfig._fichier_csv_element)
    for e in el:
        print(e)
    print("-"*10, el.get_element("BRIQUE_ROUGE"))
    