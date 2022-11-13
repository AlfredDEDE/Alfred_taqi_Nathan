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
        somme = somme + notes [i] 
        moyenne = somme / len(notes)
        reponse = moyenne
    return reponse

'''def moyenne_eleves_gen (nom):
    for i in range 21 :
        creer_des_notes()
        moyenne(notes)'''
#

def savoir_notes_eleves_sup_n (n):
    moyenne_sup_n = []
    for i in range 21 :
        if moyenne_gen >= n:
            moyenne_sup_n.append()
    return moyenne_sup_n 

def savoir_notes_eleves_inf_n (n):
    moyenne_inf_n = []
    for i in range 21 :
        if moyenne_gen <= n:
            moyenne_inf_n.append()
    return moyenne_inf_n

def savoir_nbr_eleves_sup_n (savoir_notes_eleves_sup_n):
    len(savoir_notes_eleves_sup_n())
def savoir_nbr_eleves_inf_n (savoir_notes_eleves_inf_n) :
    len(savoir_notes_eleves_inf_n())
        

