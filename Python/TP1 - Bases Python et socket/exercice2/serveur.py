# Exercice 2 - Socket
# Nous voulons créer un client serveur qui jouent au chifoumi.
import socket
import random

def serveur():
  host = ""
  port = 2001
  s_serveur = socket.socket()
  s_serveur.bind((host, port))
  s_serveur.listen()
  s_client, adresse = s_serveur.accept()
  print("Client " + str(adresse) + " s'est connecté\r\n")
  s_client.send(("Client " + str(adresse) + " s'est connecté\r\n").encode()) #1-Q
  return s_serveur, s_client

def chifoumi(s_client):
  l = ["pierre", "feuille", "ciseaux"]
  points_serveur = 0
  points_client = 0

  for i in range(5):
    choix_serveur = random.choice(l)
    choix_client = s_client.recv(128).decode() #2-R
    print(f"Choix du serveur : {choix_serveur}\r\nChoix du client : {choix_client}")
    s_client.send(("Choix du serveur : " + choix_serveur + "\r\nChoix du client : " + choix_client + "\r\n").encode()) #3-Q

    if(choix_serveur == choix_client):
      print("Nul\r\n")
    elif(choix_serveur == "pierre" and choix_client == "ciseaux"):
      print("Serveur gagne\r\n")
      points_serveur += 1
    elif(choix_serveur == "feuille" and choix_client == "pierre"):
      print("Serveur gagne\r\n")
      points_serveur += 1
    elif(choix_serveur == "ciseaux" and choix_client == "feuille"):
      print("Serveur gagne\r\n")
      points_serveur += 1
    else:
      print("Client gagne\r\n")
      points_client += 1
  print(f"Points serveur : {points_serveur}\r\nPoints client : {points_client}")

def main():
  print("Serveur en marche")
  s_serveur, s_client = serveur()
  chifoumi(s_client)
  s_client.close()
  s_serveur.close()

main()
