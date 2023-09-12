# Exercice 1 - Les conditions
# Une entreprise de nutrition souhaite automatiser le calcul de la dépense journalière en fonction des caractéristiques des clients.
def informationsClient():
  sexe = int(input("Vous êtes un homme (1) ou une femme (2) : "))
  poids = float(input("Votre poids (kg) : "))
  taille = float(input("Votre taille (cm) : "))
  age = int(input("Votre âge : "))
  print("Votre niveau d'activité entre 1 et 2 :")
  print("- Sédentaire = 1")
  print("- Très faible activité = 1.2")
  print("- Activité légère = 1.4")
  print("- Activité modérée = 1.6")
  print("- Haute activité = 1.8")
  print("- Activité extrême = 2")
  activite = float(input())
  objectif = int(input("Voulez-vous maigrir (1) ou grossir (2) : "))
  return sexe, poids, taille, age, activite, objectif

def calculBRM(sexe, poids, taille, age, activite):
  if(sexe == 1):
    BRM = float((66+(13.7*poids)+(5*taille)-(6.8*age))*activite)
  elif(sexe == 2):
    BRM = float((655+(9.6*poids)+(1.7*taille)-(4.7*age))*activite)
  else:
    print("Erreur sur le sexe")
    BRM = None
  return BRM

def calculObjectif(objectif, BRM):
  if(objectif == 1):
    objectif = BRM*0.9
  elif(objectif == 2):
    objectif = BRM*1.1
  else:
    print("Erreur sur l'objectif")
    objectif = None
  return objectif

def main():
  sexe, poids, taille, age, activite, objectif = informationsClient()
  BRM = calculBRM(sexe, poids, taille, age, activite)
  if BRM is not None:
    objectif = calculObjectif(objectif, BRM)
    if objectif is not None:
      print("Votre besoin calorique quotidien est :", BRM, "kcal")
      print("Votre objectif calorique quotidien est :", objectif, "kcal")

main()

############################# CORRECTION ###############################
def demandeUtilisateurs():
	age=int(input("Quel est votre age?\n"))
	poids=int(input("Quel est votre poids?\n"))
	taille=int(input("Quel est votre taille (en cm)?\n"))
	sexe=input("Quel est votre sexe ? (F ou H)\n")
	print("Quel est votre niveau d'activité ?\n")
	print("Sédentaire : 1\n")
	print("Trés faible activité :1.2\n")
	print("Activité légére : 1.4\n")
	print("Activité modérée : 1.6\n")
	print("Haute activité : 1.8\n")
	print("Activité extréme : 2\n")
	activite=float(input())
	attente=input("Voulez maigrif (m) ou grossir (g)?\n")
	return age,poids,taille,sexe,activite,attente

def calcul_BRM(age, poids,taille,sexe):
		if(sexe=="H"):
			BRM=66+(13.7 * poids) + (5 * taille)-(6.8 * age)
			return BRM
		elif(sexe=="F"):
			BRM=655+(9.6 * poids) + (1.7 * taille)-(4.7 * age)
			return BRM
		else:
			print("Vous n'avez pas entré F ou H\n")

def calcul_final(BRM,activite,attente):
	BRMa=BRM*activite
	if(attente=="m"):
		BRMf=BRMa*0.9
		return BRMf
	elif(attente=="g"):
		BRMf=BRMa*1.1
		return BRMf
	else:
		print("vous vous etes trompé entre m et g\n")

def progPrincipal():
	age,poids,taille,sexe,activite,attente=demandeUtilisateurs()
	BRM=calcul_BRM(age,poids,taille,sexe)
	print("Votre BRM est de : ",BRM, " Calories par jours")
	BRMf=calcul_final(BRM,activite,attente)
	print("Votre nombre de calories par jour doit être de ",BRMf)

progPrincipal()