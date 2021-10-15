# on importe dans la bibliotheque math la fonction sqrt
# SQuare RooT, soit en francais, racine carree

from math import sqrt


# tp1 ##########################################################################
def discriminant(a,b,c):
    calcul = b**2 - 4*a*c
    print("Le discriminant vaut ",calcul)
    # on renvoie aussi le resultat
    return calcul

# tp2 ##########################################################################
def nb_racines(a,b,c):
    delta = discriminant(a,b,c)
    if delta>0:
        nb=2
    # elif est la contraction de "else if"   
    elif (delta==0):
        nb=1
    else:
        nb=0
    print("Il y a ",nb," racine(s)")
    return nb


# tp3 c'est une amelioration du tp2 ############################################
def racines(a,b,c):
    delta = discriminant(a,b,c)
    if delta>0:
        nb=2
        racine1 = (-b-sqrt(delta))/(2*a)
        racine2 = (-b+sqrt(delta))/(2*a)
        print("Il y a deux racines ",racine1," et ",racine2)
    # elif est la contraction de "else if"   
    elif (delta==0):
        nb=1
        racine1 = (-b)/(2*a)
        racine2 = 0
        print("Il y a une racine double ",racine1)
    else:
        nb,racine1, racine2 = 0,0,0
        print("Il n'y a aucune racine")
    return(nb,racine1,racine2)
        
 
        
# tp4 ##########################################################################
def f_canonique(a,b,c):
    alpha = -b / (2*a)
    beta = -(b**2 - 4*a*c)/(4*a)
    print("alpha =",alpha," et beta =",beta)
    return (alpha,beta)
