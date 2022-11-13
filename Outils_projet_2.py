from data import *

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

def est_bon_prenom (a):
    return a in liste_prenoms

def pas_bon_prenom (a):
    return not (liste_prenoms (a))

def est_bon_nom (a):
    return a in liste_noms

def pas_bon_nom (a):
    return not (liste_noms (a))

def moyenne (notes,coef):
    somme = 0.0
    for i in range (len(notes)):
        somme = somme + notes [i] * coef [i]
        moyenne = somme / sum(float(coef))
        reponse = moyenne
    return reponse

notes = list(input('Notes?'))
coef = list(input('coef?'))

print (str(moyenne))

def creer_une_note():
    marks.append(randint(0, 20))
    return marks

def determiner_le_nombre_de_note():
    length = randint(3, 8)
    return length

def creer_des_notes():
    for i in range(determiner_le_nombre_de_note()):
        creer_une_note()
    return marks
