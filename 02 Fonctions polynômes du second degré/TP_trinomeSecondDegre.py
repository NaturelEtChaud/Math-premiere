# on importe dans la bibliotheque math la fonction sqrt
# SQuare RooT, soit en francais, racine carree

from math import sqrt


# tp1 ##########################################################################
def discriminant(a,b,c):
    calcul = b**2 - 4*a*c
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
    return nb


# tp3 c'est une amelioration du tp2 ############################################
def racines(a,b,c):
    delta = discriminant(a,b,c)
    if delta>0:
        racine1 = (-b-sqrt(delta))/(2*a)
        racine2 = (-b+sqrt(delta))/(2*a)
        reponse = (2,racine1,racine2)
    # elif est la contraction de "else if"   
    elif (delta==0):
        racine = (-b)/(2*a)
        reponse = (1,racine)
    else:
        reponse = (0)
    return reponse
