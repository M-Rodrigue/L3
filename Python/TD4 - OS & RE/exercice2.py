############################# CORRECTION ###############################
import os,time

l=[]
chemin="/Users/franckebel/Documents/formations/oteria/challenges"
for chemin,repertoires,fichiers in os.walk(chemin):
    for fichier in fichiers:
        chem_fich=chemin+"/"+fichier
        #print(chem_fich)
        fd = os.open(chem_fich, os.O_RDWR)
        info = os.fstat(fd)
        #print(f"le fichier {fichier} Total size, in bytes: {info.st_size}")
        F=info.st_size
        #time.sleep(0.5)
        if (int(F)>= 8192):
            l.append( fichier)
        os.close( fd)
print("il y a ",len(l)," fichiers superieures a 8192 , les voici :")
for i in l:
	print(i,end= " | ")