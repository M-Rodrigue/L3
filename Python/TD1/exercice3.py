# Exercice 3 - Les dictionnaires
points_lettres = {"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,"G":2,"H":4,"I":1,"J":8,"K":10,"L":1,"M":2,"N":1,"O":1,"P":3,"Q":8,"R":1,"S":1,"T":1,"U":1,"V":4,"W":10,"X":10,"Y":10,"Z":10}

# Question 1 & 2
def comptePoints(motUtilisateur):
  motUtilisateur = motUtilisateur.upper()
  total_points = 0

  for lettre in motUtilisateur:
    if lettre in points_lettres:
      total_points += points_lettres[lettre]

  return total_points

def question1_2():
  motUtilisateur = input("Donnez-moi un mot : ")
  points = comptePoints(motUtilisateur)
  print("Le total des points pour le mot est : ",points)

# Question 3
def nbr_Consonnes(motUtilisateur):
  motUtilisateur = motUtilisateur.upper()
  voyelles = ["A", "E", "I", "O", "U", "Y"]
  consonnes = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

  total_voyelles = 0
  total_consonnes = 0
  points_voyelles = 0
  points_consonnes = 0

  for lettre in motUtilisateur:
    if lettre in voyelles:
      total_voyelles += 1
      points_voyelles += points_lettres.get(lettre, 0)
    elif lettre in consonnes:
      total_consonnes += 1
      points_consonnes += points_lettres.get(lettre, 0)

  return total_voyelles, total_consonnes, points_voyelles, points_consonnes

def question3():
  motUtilisateur = input("Donnez-moi un mot : ")
  total_voyelles, total_consonnes, points_voyelles, points_consonnes = nbr_Consonnes(motUtilisateur)
  print("Le nombre de voyelles est de ",total_voyelles," et le nombre de consonnes est de ",total_consonnes)

# Question 4 & 5
def question4_5():
  motUtilisateur = input("Donnez-moi un mot : ")
  points = comptePoints(motUtilisateur)
  total_voyelles, total_consonnes, points_voyelles, points_consonnes = nbr_Consonnes(motUtilisateur)
  print("Le total des points pour le mot est ",points," pour les voyelles ",points_voyelles," et pour les consonnes ",points_consonnes)
  print("Le nombre de voyelles est de ",total_voyelles," et le nombre de consonnes est de ",total_consonnes)

# Appel de la fonction question1_2 pour tester la question 1 et 2
# question1_2()

# Appel de la fonction question3 pour tester la question 3
# question3()

# Appel de la fonction question4_5 pour tester la question 4 et 5
# question4_5()