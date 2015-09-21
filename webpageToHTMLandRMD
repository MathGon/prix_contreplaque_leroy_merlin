"""
Parse la page web du site de Leroy Merlin afin d'ajouter des filtres sur le choix de contre plaque
url -> json -> table (html & rmd)

UPGRAGE:
Exporter directement une page html?
"""

import urllib
from BeautifulSoup import BeautifulSoup

def listProd(): 
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
    for prod in listProd:
        print prod

def miseTableauRMD(listProd):        
    for prod in listProd:
        print prod

def uploadServeur(file):
    serveur = "youpi"#uploader  
  
    
                 
#miseTableauHTML(listProd())
