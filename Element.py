import csv

"""Caractéristiques et liste des éléments pouvant être positionnés sur la grille de jeu"""

class ElementItem:
    def __init__(self, dict_data):
        self._dict_data = dict_data
        self.identifiant = dict_data["Identifiant"]
        self.durete = dict_data["Durete"]
        self.largeur = dict_data["Largeur"]
        self.images = ( dict_data["Image"], dict_data["Image_impact_1"], dict_data["Image_impact_2"] )
        
    def __repr__(self):
        return f"{type(self)} → identifiant={self.identifiant}; durete={self.durete}; largeur={self.largeur}; images={self.images}"
        
class ElementList:
    def __init__(self, nom_fichier_csv):
        self._nom_fichier_csv = nom_fichier_csv
        
        self._elements = []
        with open(self._nom_fichier_csv, 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                self._elements.append(ElementItem(row))
        
    def __iter__(self):
        """Fournir un itérateur"""
        for x in self._elements:
            yield x

#############################

if __name__ == "__main__":
    import AppConfig
    el = ElementList(AppConfig.fichier_csv_element)
    for e in el:
        print(e)
