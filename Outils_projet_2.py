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

def notes_de_tous_les_eleves_ds_une_matiere ():
    for i in range(nombre_eleves):
        creer_des_notes()
        liste_note_dans_une_matiere.append(moyenne(notes))

    return(liste_note_dans_une_matiere)

def moyenne_eleves_gen_ds_une_matiere():
    for i in range(nombre_eleves):
        creer_des_notes()
        liste_note_dans_une_matiere.append(moyenne(notes))

    moyenne_eleves_gen_ds_une_matiere = moyenne (liste_note_dans_une_matiere)
    return ( moyenne_eleves_gen_ds_une_matiere)

def notes_tous_les_eleves():
    for i in range(nombre_eleves):
        creer_des_notes()
        liste_note_dans_une_matiere.append(moyenne(notes))

    return(liste_note_dans_une_matiere)

#La liste et/ou le nombre d'eleves ayant une moyenne en Maths supérieure à n/20

def savoir_notes_eleves_sup_n (n):

    for i in range (nombre_eleves) :
        if moyenne_gen >= n:
            moyenne_sup_n.append()
    return moyenne_sup_n 

def savoir_notes_eleves_inf_n (n):
    moyenne_inf_n = []
    for i in range (nombre_eleves) :
        if moyenne_gen <= n:
            moyenne_inf_n.append()
    return moyenne_inf_n

def savoir_nbr_eleves_sup_n (savoir_notes_eleves_sup_n):
    len(savoir_notes_eleves_sup_n())

def savoir_nbr_eleves_inf_n (savoir_notes_eleves_inf_n) :
    len(savoir_notes_eleves_inf_n())



#La liste et/ou le nombre d'eleves ayant n moyennes supérieures à m/20

/
/
/
/
/

#La liste et/ou le nombre d'eleves ayant une moyenne générale compris entre n1/20 et n2/20

def moyenne_gen_entre_n_et_m (n,m):
    Intervalle_note = interval([n, m])
    for i in eleves:
        if moyenne_generqle_eleve in Intervalle_note :
            eleves_notes_gen.append()
    return eleves_notes_gen
