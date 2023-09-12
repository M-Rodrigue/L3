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