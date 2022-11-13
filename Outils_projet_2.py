def est_bon_prenom (a):
    return a in liste_prenoms

def pas_bon_prenom (a):
    return not (liste_prenoms (a))

def est_bon_nom (a):
    return a in liste_noms

def pas_bon_nom (a):
    return not (liste_noms (a))

def est_un_bon_prenom (a):
    return a in liste_prenoms
##

def is_not_a_valid_f_name (a):
    return not (liste_prenoms (a))

def is_a_valid_name (a):
    return a in liste_noms

def is_not_a_valid_f_name (a):
    return not (liste_noms (a))
##

def Prenoms (a) :
    if a in liste_prenoms :
        print(est_bon_prenom(a))
    if a in liste_nom :
        print(est_bon_nom)
    else :
        print("Le nom se trouve pas dans la base de donnes")

str(input("Le nom ou prenom"))
