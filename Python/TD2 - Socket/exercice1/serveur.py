# Exercice 1 - Client-serveur jeu trouve
# Ecrire un jeu qui permet à un client de deviner un nombre aléatoire choisi par le serveur. Le client indique le nombre maximum au serveur. Le serveur demande un nombre au client et répond ‘plus’ ou ‘moins’. La connexion est terminée lorsque le nombre est trouvé.
import socket
import random

def serveur():
  host = ""
  port = 1217
  s = socket.socket()
  s.bind((host, port))
  s.listen()
  s_client, adresse = s.accept()
  print("Client " + str(adresse) + " s'est connecté")
  s_client.send(("Client " + str(adresse) + " s'est connecté\r\n").encode()) #1
  return s, s_client

def juste_prix(s, s_client):
  s_client.send(b"Veuillez donner un nombre limite\r\n") #2
  nombreMax = s_client.recv(128).decode() #2
  nombreDeBase = random.randint(1, int(nombreMax))
  s_client.send(("Vous devez deviner le nombre aléatoire entre 1 et " + str(nombreMax) + "\r\n").encode())

  i = 0
  nombreUtilisateur = 0
  while int(nombreUtilisateur) != nombreDeBase:
    i += 1
    s_client.send(b"Donner un nombre : \r\n")
    nombreUtilisateur = int(input(s_client.recv(128).decode()))
    if(int(nombreUtilisateur) < nombreDeBase):
      s_client.send(b"Plus !\r\n")
    elif(int(nombreUtilisateur) > nombreDeBase):
      s_client.send(b"Moins !\r\n")

  s_client.send(("Vous avez trouvé le nombre en " + str(i) + " tentatives\r\n").encode())
  s_client.close()
  s.close()

def main():
  s, s_client = serveur()
  juste_prix(s, s_client)

main()
