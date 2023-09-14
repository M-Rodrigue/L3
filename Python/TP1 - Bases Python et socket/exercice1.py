# Exercice 1 - Les bases
# On suppose qu’un enseignant a réalisé une évaluation. Le secrétariat lui a transmis une liste dont chaque élément est un dictionnaire comportant deux clés : "nom" et "prénom".

# Cette fonction permet de saisir les notes pour chaque étudiant dans la liste 'd'.
def saisieNotes(d):
  for eleve in d:
    # Demande à l'utilisateur de saisir la note pour un étudiant spécifique.
    note = int(input(f"Entrez la note pour {eleve['prenom']} {eleve['nom']} : "))
    # Stocke la note dans le dictionnaire de l'étudiant sous la clé 'note'.
    eleve['note'] = note
  print("\r")  # Ligne vide pour la clarté de l'affichage.
  return d

# Cette fonction trouve l'étudiant ayant obtenu la meilleure note.
def meilleur(l1):
  meilleur_eleve = None
  meilleur_note = -1

  for eleve in l1:
    note = eleve.get('note', 0)
    if note > meilleur_note:
      meilleur_note = note
      meilleur_eleve = eleve

  # Retourne le nom, prénom et la meilleure note de l'étudiant.
  return meilleur_eleve['nom'], meilleur_eleve['prenom'], meilleur_note

# Fonction principale qui exécute le programme.
def progPrincipal():
  d = [
    {"nom":"EBEL","prenom":"Franck"},
    {"nom":"SPRIET","prenom":"Hugues"},
    {"nom":"BUREL","prenom":"Romain"},
    {"nom":"DE MONTALIVET","prenom":"Paul"}
  ]

  # Appelle la fonction saisieNotes pour saisir les notes pour chaque étudiant.
  l1 = saisieNotes(d)
  print(l1, "\r\n")

  # Appelle la fonction meilleur pour trouver l'étudiant avec la meilleure note.
  resu = meilleur(l1)
  print("La meilleure note est : ", resu[2], " et appartient à ", resu[0], resu[1])

# Exécute la fonction principale.
progPrincipal()
