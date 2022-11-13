from data import *

def est_bon_prenom (a):
    return a in liste_prenoms

def est_bon_nom (a):
    return a in liste_noms

def verif_nom_ou_prenom_exist(a):

    if est_bon_prenom (a) == True :
        return (est_bon_prenom(a))
    if est_bon_nom(a)== True :
        return (est_bon_nom(a))
    else :
        return False

def creer_une_note():
    notes.append(randint(0, 20))
    return notes

def determiner_le_nombre_de_note():
    length = randint(3, 8)
    return length

def creer_des_notes():
    for i in range(determiner_le_nombre_de_note()):
        creer_une_note()
    return notes

def moyenne (notes):
    somme = 0.0
    for i in range (len(notes)):
        somme = somme + notes [i] * coef [i]
        moyenne = somme / sum(float(coef))
        reponse = moyenne
    return reponse

