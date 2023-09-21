import random
# On importe des composants de la bibliothèque scapy
# IP : forger des paquets IP
# TCP : forger les segments TCP
# sr1 : fonction qui permet d'émettre le paquet forgé
from scapy.all import IP, sr1, TCP

# La fonction doScan() prend en paramètres :
# myhost : IP de l'hôte à scanner
# ttl : Délai de garde port scanné
def doScan (myhost,ttl):
  # 22 = port SSH = Secure SHell (protocole de prise en main à distance de machines essentiellement linux)
  # 80 = HTTP = HyperText Transfert Protocol (protocole de communication entre navigateurs et serveurs web)
  # 443 = HTTPS = HTTPSecure (protocole de communication entre navigateurs et serveurs web mais chiffrés)
  # 25 = SMTP = Simple Mail Transfer Protocol (protocole de transfert de mails, relais de spams potentiels)
  # 3389 = RDP = Remote Desktop Protocol (protocole de prise en main à distance de machines windows)
  ports = [22,80,443,25,3389]

  # for dst_port in range(1,65535) pour scanner tous les ports possibles
  for dst_port in ports:
    #src_port sert à fixer un port pour le client. Le port est tiré aléatoirement entre 1025 et 65535.
    # Les ports de 1 à 1024 sont des ports privilégiés uniquement accessibles aux processus s'executant
    # avec les privilèges d'admin
    src_port = random.randint(1025,65535)
    # 65535 = 2^16-1 (parce que TCP donne 16 bits par ports, et -1 parce que le port 0 ne compte pas)

    # On ne traite que la première réponse avec sr1()
    # Envoie SYN avec un port source aléatoire > 1024 et on stocke la première réponse dans resp
    # le port source fait une demande de connexion au port destinataire par le protocole TCP
    # on indique que si au bout de "ttl" temps il n'y a pas de réponse, on passe à l'itération suivante de la boucle
    # verbose = 0 -> on ne produit pas d'affichage de ce qui est entrain de se passer dans la machine
    resp = sr1(
      IP(dst=myhost)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=ttl,
      verbose=0,
    )

    # On rentre dans le traitement de la réponse

    # 1) Si pas de réponse à la fin du délais
    if resp is None:
      # on affiche l'IP destination : le port destination et pas de réponse
      print(myhost + " : " + str(dst_port) + " pas de réponse.")

    # 2) On recoit quelque chose
    # ici, un paquet comprenant une couche TCP
    elif(resp.haslayer(TCP)):
      # 2a) On reçoit un SYN/ACK => il y a un processus en écoute sur le port dst_port
      # 0x12 = 0x02 (SYN) + 0x10 (ACK)-> SYN/ACK = réponse du processus lié au dst_port pour acquitter le SYN qu'on lui a envoyé
      if(resp.getlayer(TCP).flags == 0x12):
      # Une fois le port ouvert trouvé, on envoie un RST pour mettre fin à la connexion.
        send_rst = sr1(
          IP(dst=myhost)/TCP(sport=src_port,dport=dst_port,flags='R'),
          timeout=1,
          verbose=0,
        )
        print(myhost + " : " + str(dst_port) + " est ouvert.")

        # 2b) On a reçu un RST/ACK, le port est donc fermé
      elif (resp.getlayer(TCP).flags == 0x14):
        print(myhost + " : " + str(dst_port) + " est fermé.")

def main():
  # on définit ttl à 1 seconde de délais
  ttl = 1
  for myhost in listeIP:
    doScan(myhost, ttl)

main()