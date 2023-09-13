# Exercice 1 - Client-serveur jeu trouve
# Ecrire un jeu qui permet à un client de deviner un nombre aléatoire choisi par le serveur. Le client indique le nombre maximum au serveur. Le serveur demande un nombre au client et répond ‘plus’ ou ‘moins’. La connexion est terminée lorsque le nombre est trouvé.
import socket

def connexion():
  host = "127.0.0.1"
  port = 1217
  s = socket.socket()
  s.connect((host, port))
  data = s.recv(128) #1
  print(data.decode())
  return s

def client(s):
  nombreMax = int(input("Veuillez donner un nombre limite pour commencer (quitter le programme : 0) : "))
  s.send(str(nombreMax).encode()) #2

  if(nombreMax != 0):
    while True:
      data = s.recv(128) #3
      print(data.decode())

      nombre = int(input("Donner un nombre : "))
      s.send(str(nombre).encode()) #4

      data = s.recv(128) #5
      print(data.decode())

      if nombre == 0:
        break

def main():
  s = connexion()
  client(s)
  s.close()

main()

# ############################# CORRECTION ###############################
# import socket, time

# host="127.0.0.1"
# port = 1338
# s=socket.socket()
# s.connect((host,port))
# data=s.recv(1024)
# print(data.decode())
# nbr0=input()
# s.send(nbr0.encode("utf8"))
# reponse="test"
# point=0
# while ( True ):
#     if (reponse!="fini"):
#         nbr=int(input("entrez un nombre\n"))
#         s.send(str(nbr).encode("utf8"))
#         reponse=s.recv(10)
#         reponse=reponse.decode("utf8")
#         print(reponse)
#         point=point+1
#     else:
#         print("c'est fini")
#         print("vous avez gagné en ",point," coups")
#         break
# s.close()