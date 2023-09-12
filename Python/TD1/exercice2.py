# Exercice 2 - Les boucles
# Nous souhaitons réaliser un programme d’un jeu simple, ce jeu permet à un utilisateur de deviner un nombre aléatoire choisi par le programme.
import random
nombreMax = int(input("Veuillez donner un nombre limite :"))
nombreDeBase = random.randint(1,nombreMax)
print("Vous devez deviner le nombre aléatoire entre 1 et " + str(nombreMax))

i = 0
nombreUtilisateur = 0
while int(nombreUtilisateur) != nombreDeBase:
  i += 1
  nombreUtilisateur = int(input("Donner un nombre : "))
  if(int(nombreUtilisateur) < nombreDeBase):
    print("Plus !")
  elif(int(nombreUtilisateur) > nombreDeBase):
    print("Moins !")

print("Vous avez trouvé le nombre en " + str(i) + " tentatives")