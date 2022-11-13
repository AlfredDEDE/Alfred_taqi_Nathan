from data import *


def est_bon_prenom (a):
    return a in liste_prenoms

def pas_bon_prenom (a):
    return not (liste_prenoms (a))

def est_bon_nom (a):
    return a in liste_noms

def pas_bon_nom (a):
    return not (liste_noms (a))


##

'''def verif_nom_ou_prenom_exist (a) :
    if a in liste_prenoms :
        print(est_bon_prenom(a))
    if a in liste_nom :
        print(est_bon_nom(a))
    else :
        print("Le prenom/nom se trouve pas dans la base de donnes")'''

def verif_nom_ou_prenom_exist (a) :
    if pas_bon_prenom == False :
        return (est_un_bon_prenom())
    if pas_bon_nom == False :
        return (est_un_bon_nom())
    else :
        print(id_pas_valide)
