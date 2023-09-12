# Exercice 4 - Gestion des dates/jours de l’année

Jours=[‘Lundi’,’Mardi’,’Mercredi’,’Jeudi’,’vendredi’,’Samedi’,’Dimanche’]
Mois=
[‘Janvier’,’Fevrier’,’Mars’,’Avril’,’Mai’,’Juin’,’Juillet’,’Aout’,’Spetembre’,’Octobre’,’Novembre’,
’Decembre’]
Nbr_j=[31,28,31,30,31,30,31,31,30,31,30,31]

############################# CORRECTION ###############################
def jourAnnee(j,m,n):
    l=[]
    j=j[4:]+j[:4] # je commence la liste par vendredi
#    print(j)
#creation d'une liste avec les dates et mois
    i=0
    while i < len(m):
            for day in range(1,n[i]+1):
                l.append([day,m[i]])
            i=i+1
#    print(l)
    long=len(l)
#creation d'une liste avec  tous les jours de l'année
    longe=long//len(j) # 365/7 = 52
    l2=[]
    for i in range(0,longe):
        for var in j:
            l2.append(var)
    l2.append(j[(long%len(j)-1)])
#    print(l2)

#fusion des deux listes
    for i in range(0,len(l)):
        l[i].append(l2[i])
    print(l)
    return l

def determinationJour(j,m,l):
    for a,b,c in l:
        if(a==j and b==m):
            return c
        else:
            False

def progPrincipal():
    Jours=["Lundi","Mardi","Mercredi","Jeudi","vendredi","Samedi","Dimanche"]
    Mois= ["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Aout","Septembre","Octobre","Novembre","Decembre"]
    Nbr_j=[31,28,31,30,31,30,31,31,30,31,30,31]
    liste=jourAnnee(Jours,Mois,Nbr_j)
    jour=int(input("veuillez entrer une date\n"))
    mois=input("Veuillez entrer un mois\n")
    mois=mois.capitalize()
    j=determinationJour(jour,mois,liste)
    print("le ",jour," ",mois," est un ",j)

if(__name__=="__main__"):
    progPrincipal()