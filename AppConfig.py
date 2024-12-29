""" Constantes / paramètres / variables à utiliser "globalement" """
import os

from Element import ElementList

dossier_racine:str = os.path.dirname(__file__)
dossier_niveau:str = os.path.join(dossier_racine, "niveau")
dossier_img:str = os.path.join(dossier_racine, "img")
dossier_csv:str = os.path.join(dossier_racine, "csv")

_fichier_csv_element = os.path.join(dossier_csv, "element.csv")
elements:ElementList = ElementList(_fichier_csv_element)
