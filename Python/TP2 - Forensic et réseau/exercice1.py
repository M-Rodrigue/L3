# Importation des bibliothèques
import os, re, shutil, socket, ipaddress

# Fonction pour rechercher les documents JPG et TXT
def recherche():
  pattern = r'\w+\.(jpg|txt)' # Filtre tous les fichiers en jpg et txt avec 'r' pour raw string
  chemin = input("Entrer le chemin à parcourir : ")
  regex = re.compile(pattern)
  listeRecherche = []

  # Boucle pour chercher tous les documents et leurs chemins
  for chemin, _, fichiers in os.walk(chemin):
    for fichier in fichiers:
      if regex.match(fichier):
        listeRecherche.append(os.path.join(chemin, fichier))

  # Boucle pour afficher tous les résultats
  print("Fichiers trouvées : ")
  for resultat in listeRecherche:
    print("- " + resultat)

  return listeRecherche

# Fonction pour trier les images dans un dossier
def trieImages(listeRecherche):

  # Création dossier Photos s'il n'existe pas
  if not os.path.exists("Photos"):
    os.makedirs("Photos")

  # Filtre les JPG
  for fichier in listeRecherche:
    if fichier[-3:] == "jpg":
      shutil.move(fichier, "/Users/mrodrigue/Desktop/Projets/L3/Python/TP2 - Forensic et réseau/Photos")

# Fonction pour trouver des adresses IP dans un fichier txt
def trieTextes(listeRecherche):

  # Filtre les TXT pour trouver les IP
  for fichier in listeRecherche:
    if fichier[-3:] == "txt":
      with open(fichier, 'r') as texte:
        contenu = texte.read()
        pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
        listeIP = re.findall(pattern, contenu)

  # Affiche les adresses IP et l'IP locale
  localeIP = socket.gethostbyname(socket.gethostname())
  print("\nAdresse IP locale : " + localeIP)
  if listeIP:
    print("Adresses IP trouvées : ")
    for ip in listeIP:
      print("- " + ip)
  else:
    print("Aucune adresse IP trouvée")

  return listeIP

# Fonction pour trier les adresses IP
def trieIP(listeIP):
  localeIP = ipaddress.IPv4Network(socket.gethostbyname(socket.gethostname()), strict = False)

  # Filtre les IP LAN
  if listeIP:
    print("\nAdresse IP LAN :")
    for ip in listeIP:
      lanIP = ipaddress.IPv4Network(ip, strict = False)
      if localeIP.network_address.exploded[:3] == lanIP.network_address.exploded[:3]:
        print(f"- {lanIP}")
  else:
    print("\nAucune adresse IP trouvée")

def main():
  listeRecherche = recherche()
  trieImages(listeRecherche)
  listeIP = trieTextes(listeRecherche)
  trieIP(listeIP)

  # Affiche fichiers sans les extensions
  print("\nFichiers trouvés sans les extensions :")
  for fichier in listeRecherche:
    print("- " + fichier[:-4])


main()