#### Imports et définition des variables globales
"""Des fonctions itérative et récursive qui retournent la liste des tuples"""
import sys
sys.setrecursionlimit(2000)

#### Fonctions secondaires


def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne
    de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder
    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
        
    """
    # votre code ici

    listetuple=[]
    i=0
    while i<len(s):
        g=i
        o=0
        while g<len(s) and s[i]==s[g]:
            o+=1
            g+=1
        listetuple.append((s[i],o))
        i += o
    return listetuple


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de
    caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)"""

    # votre code ici

    # cas de base
    if s=="":
        return []
    # recherche nombre de caractères identiques au premier
    caractere= s[0]
    s=s[1:]
    compteur=1
    while s!="" and caractere == s[0]:
        compteur+=1
        s= s[1:]

    #appel recursif
    return [(caractere,compteur)]+artcode_r(s)

#### Fonction principale


def main():
    """On teste les fonctions"""
    print(artcode_i("MMMMaaacXolloMM"))
    print(artcode_r("MMMMaaacXolloMM"))

if __name__ == "__main__":
    main()
