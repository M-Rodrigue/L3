
############################# CORRECTION ###############################
#Question A
def palindrome(mot:str)->bool:
    if(mot==mot[::-1]):
        return True
    else:
        return False
#Question B
def compter(ph1,ph2):
    cpt=0
    for i in range(0,len(ph2)-len(ph1)):
        if ph2[i:len(ph1)+i]==ph1:
            cpt=cpt+1
    return cpt
#Question C
def voyelles(phrase):
    l='aeiouyAEIOUY'
    cpt=0
    for i in phrase:
        if (i in l):
            cpt=cpt+1
    return cpt
#question D
def minuscules(phrase):
    l=[]
    for i in phrase:
        if (65<=ord(i)<=90):
            l.append(chr(ord(i)+32))
        else:
            l.append(i)
    print(l)
    resu=""
    for i in l:
        resu=resu+i
#    resu="".join(l)
    return resu
#Question E
def anagramme(str1,str2):
    if(len(str1)==len(str2)):
        string1=minuscules(str1)
        string2=minuscules(str2)
        if (sorted(string1)==sorted(string2)):
            return True
        else:
            return False
    else:
        return False

def nombre_ident(phr1,phr2):
    cpt=0
    for i in phr1:
        if i in phr2:
            cpt=cpt+1
    return cpt

def progPrincipal():
#    m=input("Entrez un mot\n")
#   m=m.lower()
#    var=palindrome(m)
#    if(var == True):
#        print(m, " est un palindrome")
#    else:
#        print(m, " n'est pas un palindrome")
    phr2="Bonjour tout le monde"
    phr1="on"
    print(compter(phr1,phr2))
    print("nombre de voyelles :",voyelles(phr2))
    phr3="Bonjour Tout Le Monde"
    print(minuscules(phr3))
    if(anagramme("phrAse","eSraPh")):
        print("c'est un anagramme")
    else:
        print("ce n'est pas un anagramme")
    phrase1="abcdef"
    phrase2="aabfghi"
    print("le nombre de lettres communs aux deux phrases est : ",nombre_ident(phrase1,phrase2))
progPrincipal()