
# Imports
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import re
import pandas as pd
#from cachecontrol import CacheControl

url_recherche = "https://www.veocinemas.fr/grand-lumiere/films-a-l-affiche/"


# Fonctions

# sess = requests.session()
# cached_sess = CacheControl(sess)
#
# login_data = {"login":"xxxx","password":"xxxx"}
# cached_sess.post("url d'un site necessitant connexion",login_data)
#
# # capture de la requete http
#
# html = cached_sess.get("url_recherche")

#proxies

proxies = {
  "http": "http://atlas.proxy.edf.fr:3131",
  "https": "https://atlas.proxy.edf.fr:3131"
}


html = requests.get(url_recherche, proxies = proxies)

soup = BeautifulSoup(html.text, 'html.parser', parse_only=SoupStrainer(id="maincontent-large"))

film={}
liste_films = []

def has_duration(classe):
    return re.compile("duration").search(classe) and not classe


for fiches in soup.find_all("div","fichefilm-mini-block fichefilm-mini-block-pair"): #on parcoure les fiches de film coté gauche de la page
    film["Titre"] = str(fiches.h4.contents[0]) #Le le titre du film est la première valeur de la liste du contenu de la balise h4
    film["EnSalle"] = str(fiches.p.span.strong.contents[0]) #on accede à la date de disponibilité du film en salle

    if (fiches.p.find("strong", "hi duration") !=None): #certains films n'ont pas de duree et on ne peut pas faire .contents sur un NoneType
        film["Duree"] = str(fiches.p.find("strong", "hi duration").contents[0])
    else:
        film["Duree"] = None

    lien = requests.get(fiches.a['href'], proxies = proxies) #on recupere l'adresse du lien qui mene à la fiche etendue du film
    souplette = BeautifulSoup(lien.text, 'html.parser', parse_only=SoupStrainer(id="maincontent-large")) #on cree u obj BS pour cette nouvelle page


    liste_films.append(dict(film)) #on stocke chaque dictionnaire créé (1par film) dans une liste

for fiches in soup.find_all("div", "fichefilm-mini-block fichefilm-mini-block-impair"): #idem pour les fiches coté droit
    film["Titre"] = str(fiches.h4.contents[0])
    film["EnSalle"] = str(fiches.p.span.strong.contents[0])

    if (fiches.p.find("strong", "hi duration") != None):
        film["Duree"] = str(fiches.p.find("strong", "hi duration").contents[0])
    else:
        film["Duree"] = None
    liste_films.append(dict(film))

df_films = pd.DataFrame(liste_films) #création d'un dataframe

