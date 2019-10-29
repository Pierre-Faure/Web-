
# Imports
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
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

for fiches in soup.find_all("div","fichefilm-mini-block fichefilm-mini-block-pair"):
    film["Titre"] = str(fiches.h4.contents[0])
    liste_films.append(dict(film))

for fiches in soup.find_all("div", "fichefilm-mini-block fichefilm-mini-block-impair"):
    film["Titre"] = str(fiches.h4.contents[0])
    liste_films.append(dict(film))

