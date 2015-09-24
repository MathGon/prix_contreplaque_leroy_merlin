"""
Parse la page web du site de Leroy Merlin afin d'ajouter des filtres (epaisseur, prix/m2, materiau) sur le choix de contre plaque

url -> json -> table (html & rmd)
Auteur: MathGon CCbyNC

UPGRAGE:
Exporter directement une page html? Uploader sur un serveur? Executer sur un serveur?
"""

from BeautifulSoup import BeautifulSoup
import urllib
import json

def listProd():
    """ A partir du site internet de Leroy Merlin, retourne une liste de contreplaque avec carac au format json """
    listProduits = []
    url = "http://www.leroymerlin.fr/v3/search/search.do?pageTemplate=Recherche&resultOffset=0&resultLimit=100&resultListShape=SEARCHENGINE_PRODUCT_LIST_PLAIN&facet=PRODUCT&keyword=contre+plaqu%C3%A9&sort=TRI_PAR_PRIX_CROISSANT_ID&intuitiontodo=newSearchAllSite"
    data = urllib.urlopen(url).read()
    soup = BeautifulSoup(data)
    soup = soup.prettify()
    lines = soup.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        chaine_a_chercher = "prd-infos"
        if chaine_a_chercher in line:  
            produit = {}
            prodTot = lines[i+4]
            description = prodTot.split(",")[0]
            descriptionList = description.split(" ")
            typ = descriptionList[7]
            if len(descriptionList)>9:
                materiau = " ".join(descriptionList[9:])
            dimension = prodTot.split(",")[1]
            dimension = dimension.replace(" ", "")
            dimension = dimension.replace("L", "")
            dimension = dimension.replace("l", "")
            dimension = dimension.replace(".", "")
            longueur = float(dimension.split("x")[0])
            largeur = float(dimension.split("x")[1])
            epaisseur = prodTot.split(",")[2].replace("epais. ", "")
            epaisseur = epaisseur.replace("mm", "")
            surface = (largeur * longueur) / 1000
        if "price-wrapper" in line:
            prix = float(lines[i+6].replace("&euro;", ""))
            prixSurface = round(prix /surface, 2)
            produit["typ"] = typ
            produit["materiau"] = materiau
            produit["longueur"] = longueur
            produit["largeur"] = largeur
            produit["surface"] = surface
            produit["epaisseur"] = epaisseur
            produit["prix"] = prix
            produit["prixSurface"] = prixSurface
            listProduits.append(produit)
    return(listProduits)
        
print listProd()

def miseTableauHTML(listProd):
    """ Retourne une table html a partir d'une liste de produit en json """
    """
    for prod in listProd:
        print prod
    """
#miseTableauHTML(listProd())

def miseTableauRMD(listProd):
    """ Retourne une table rmd a partir d'une liste de produit en json """
    for prod in listProd:
        print prod

def uploadServeur(file):
    """
    Upload la page html vers le serveur XXX
    """
    serveur = "youpi"#uploader  
  
    
                 
#miseTableauHTML(listProd())
