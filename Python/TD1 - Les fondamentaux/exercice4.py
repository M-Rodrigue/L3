# Exercice 4 - Gestion des dates/jours de l'année
jours = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']
mois = ['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Aout','Septembre','Octobre','Novembre','Decembre']
nombres_jours = [31,28,31,30,31,30,31,31,30,31,30,31]

def jourAnnee(jours, mois, nombres_jours):
    l = []


############################# CORRECTION CHATGPT ###############################
def determinationJour(jour, mois):
  mois_jours = (("Janvier", 31), ("Février", 28), ("Mars", 31), ("Avril", 30),("Mai", 31), ("Juin", 30), ("Juillet", 31), ("Août", 31),("Septembre", 30), ("Octobre", 31), ("Novembre", 30), ("Décembre", 31))
  jours_semaine = ("Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche")

  try:
    mois_index = [m[0] for m in mois_jours].index(mois)
    jours_du_mois = mois_jours[mois_index][1]
    total_jours = sum([m[1] for m in mois_jours])
    jour_de_la_semaine = (jour - 1 + total_jours) % 7
    return jours_semaine[jour_de_la_semaine]
  except ValueError:
    return "Date invalide"

if __name__ == "__main__":
  jour = int(input("Veuillez entrer un jour (ex. 15) : "))
  mois = input("Veuillez entrer un mois (ex. Janvier) : ")

  jour_semaine = determinationJour(jour, mois.capitalize())
  print(f"Le {jour} {mois} est un {jour_semaine}")

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