############################# CORRECTION ###############################
import os,re

pattern = '\w+\.py'
l=[]
#chemin=input("Entrez le chemin à parcourir")
chemin="/Users/franckebel/Documents/formations/IUT/Licence_CDAISI/python/"
regex=re.compile(pattern)
for chemin,repertoires,fichiers in os.walk(chemin):
    for fichier in fichiers:
        l1=regex.findall(fichier)
        if l1:
            l.append(l1)
for fich in l:
    print(fich[0], end=" |  ")