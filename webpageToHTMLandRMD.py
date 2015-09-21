"""
Parse la page web du site de Leroy Merlin afin d'ajouter des filtres (epaisseur, prix/m2, matériau)sur le choix de contre plaque
url -> json -> table (html & rmd)
Auteur: MathGon CCbyNC

UPGRAGE:
Exporter directement une page html? Uploader sur un serveur? Executer sur un serveur?
"""

import urllib
from BeautifulSoup import BeautifulSoup

def listProd():
    """ A partir du site internet de Leroy Merlin, retourne une liste de contreplaque avec carac au format json """
    listProd = []
    url = "http://www.leroymerlin.fr/v3/search/search.do?pageTemplate=Recherche&resultOffset=0&resultLimit=100&resultListShape=SEARCHENGINE_PRODUCT_LIST_PLAIN&facet=PRODUCT&keyword=contre+plaqu%C3%A9&sort=TRI_PAR_PRIX_CROISSANT_ID&intuitiontodo=newSearchAllSite"
    data = urllib.urlopen(url).read()
    soup = BeautifulSoup(data)
    soup = soup.prettify()
    lines = soup.split("\n")
    for line in lines:
        chaine_a_chercher = "prd-infos"
        #token = chaine_a_chercher in line[i]
        print line
        if chaine_a_chercher in line:        
            print line
            #listProd.append(line[i]) 
            #return listProd
            #while token == True:
            #	lien = line[i-2].split("\"")[1]
            #Retourner un format json
            
listProd()

def miseTableauHTML(listProd):
    """ Retourne une table html a partir d'une liste de produit en json """
    for prod in listProd:
        print prod

def miseTableauRMD(listProd):
    """ Retourne une table rmd a partir d'une liste de produit en json """
    for prod in listProd:
        print prod

def

def uploadServeur(file):
    """
    Upload la page html vers le serveur XXX
    """
    serveur = "youpi"#uploader  
  
    
                 
#miseTableauHTML(listProd())
