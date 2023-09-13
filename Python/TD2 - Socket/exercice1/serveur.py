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
  s_client.send(("Client " + str(adresse) + " s'est connecté").encode()) #1
  return s, s_client

def juste_prix(s, s_client):
  nombreMax = s_client.recv(128).decode() #2


  if(nombreMax != 0):
    nombreDeBase = random.randint(1, int(nombreMax))
    print("Le nombre à trouver est : " + str(nombreDeBase))

    s_client.send(("Vous devez deviner le nombre aléatoire entre 1 et " + str(nombreMax)).encode()) #3

    i = 0
    nombreUtilisateur = 0
    while int(nombreUtilisateur) != nombreDeBase:
      i += 1

      nombreUtilisateur = s_client.recv(128).decode() #4

      if(int(nombreUtilisateur) < nombreDeBase):
        s_client.send("Plus !".encode()) #5
      elif(int(nombreUtilisateur) > nombreDeBase):
        s_client.send("Moins !".encode()) #5

    s_client.send(("Vous avez trouvé le nombre en " + str(i) + " tentatives").encode()) #5

def main():
  print("Serveur en cours")
  s, s_client = serveur()
  juste_prix(s, s_client)
  s_client.close()
  s.close()

main()


# ############################# CORRECTION ###############################
# import socket, time, random

# host=""
# port=1337
# s=socket.socket()
# s.bind((host,port))
# s.listen(1)
# client,address=s.accept()
# client.send("\n\n===================\n\nbienvenue dans ce jeu\nVeuillez donner un nombre maximum pour le tirage aleatoire\nBonne chance\n===================\n\n".encode("utf8"))
# n=client.recv(8)
# nbr=int(n)
# print ("le nombre maximum est : ",nbr)
# alea=random.randint(1,nbr)
# print ("le tirage donne : ",alea)
# nbr_c=client.recv(10)
# nbr_c=int(nbr_c)
# print("le nombre recu est : ", nbr_c)
# while ( int(nbr_c) != alea ):
#     if ( int(nbr_c) < alea):
#         client.send("plus".encode("utf8"))
#     else:
#         client.send("moins".encode("utf8"))
#     nbr_c = client.recv(10)
#     nbr_c=nbr_c.decode("utf8")
#     print("le nombre recu est : ",nbr_c)
# client.send("fini".encode("utf8"))
# time.sleep(1)
# client.send("vous avez trouve\n".encode("utf8"))
# client.close()
# s.close()