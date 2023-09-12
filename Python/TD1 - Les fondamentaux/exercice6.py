############################# CORRECTION ###############################
#question A
l=[12,3,5,78,23,11,17,67,54,90,1,14,8,34]
l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
l3=[1,2,3,1,3,4,5,3,6,5,7,9,2,8,9]

#question A
def moyenne(liste):
    nbr=0
    for i in liste:
        nbr=nbr+i
    nbr=nbr/len(liste)
    return(nbr)

#Question B
def additionListe(liste1:list,liste2:list)->list:
    resuListe:list
    resuListe=[]
    for i in range(0,len(liste1)):
        resuListe.append(liste1[i]+liste2[i])
    return resuListe

#Question C
def listeSansDoublon(liste):
    listeResu=[]
    for i in liste:
        if i not in listeResu:
            listeResu.append(i)
    return listeResu

#Question D
def communsListe(liste1,liste2):
    listeResu=[]
    for i in liste1:
        if i in liste2:
            listeResu.append(i)
    listeResu=listeSansDoublon(listeResu) # si sans doublons
    return listeResu

#Question E
def elementsDistincts(liste1,liste2):
    listeResu=[]
    for i in liste1:
        if i not in liste2:
                listeResu.append(i)
    for i in liste2:
        if i not in liste1:
                listeResu.append(i)
    listeResu=listeSansDoublon(listeResu)
    return listeResu


#print(moyenne(l))
#liste=additionListe(l,l1)
#print(liste)
#print(listeSansDoublon(l3))
#print(communsListe(l1,l3))
print(elementsDistincts(l1,l3))
#print(l, "    ",l1)