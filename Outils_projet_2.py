from data_nv2 import *

#fonction qui verifie ce que entre l'utilisateur du - au + précis :


def est_une_bonne_reponse_pr_lepremier_input(a):
    return a in ensemble_des_mots_clees

def fct_qui_verifie_que_l_utilisateur_ne_rentre_pas_n_importe_quoi_au_premier_input(reponse):
    if est_une_bonne_reponse_pr_lepremier_input(reponse) == True:
        return est_une_bonne_reponse_pr_lepremier_input(reponse)
    else :
        return False

#fonction qui verifie ce que entre l'utilisateur du - au + précis :

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





#focntion pour creer des notes aléatoire dans le dico

def creer_une_note():
    notes.append(randint(0, 20))
    return notes

def creer_des_notes(nombre_de_note_a_creer):
    for i in range(nombre_de_note_a_creer):
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

def notes_tous_les_eleves_dans_une_matière():
    for i in range(nombre_eleves):
        creer_des_notes()
        liste_note_dans_une_matiere.append(moyenne(notes))

    return(liste_note_dans_une_matiere)

def toutes_les_notes_d_un_eleve():
    for i in range(len()):
        liste_note_dans_une_matiere.append(notes)


def moyenne_generale_d_un_eleve(notes):
    moyenne(notes)





# La liste et/ou le nombre d'eleves ayant une moyenne en Maths supérieure à n/20

def savoir_notes_eleves_sup_n(n):
    for i in range(nombre_eleves):
        if moyenne_gen >= n:
            moyenne_sup_n.append()
    return moyenne_sup_n


def savoir_notes_eleves_inf_n(n):
    moyenne_inf_n = []
    for i in range(nombre_eleves):
        if moyenne_gen <= n:
            moyenne_inf_n.append()
    return moyenne_inf_n



def savoir_nbr_eleves_sup_n(savoir_notes_eleves_sup_n):
    len(savoir_notes_eleves_sup_n())
    return savoir_nbr_eleves_sup_n


def savoir_nbr_eleves_inf_n(savoir_notes_eleves_inf_n):
    len(savoir_notes_eleves_inf_n())
    return savoir_nbr_eleves_inf_n


# La liste et/ou le nombre d'eleves ayant n moyennes supérieures à m/20

def nbr_moyenne_eleves_sup_n(m):
    for i in range(nombre_eleves):
        if note_gen_eleve >= m:
            eleves_notes_gen_sup_m.append()
        return eleves_notes_gen_sup_m


def savoir_moyenne_gen_eleves_sup_n(eleves_notes_gen_sup_m):
    len(eleves_notes_gen_sup_m)
    return savoir_moyenne_gen_eleves_sup_n


# La liste et/ou le nombre d'eleves ayant une moyenne générale compris entre n1/20 et n2/20

def moyenne_gen_d_eleve_entre_n_et_m(n, m):

    for i in (nombre_eleves):
        if moyenne_generale_eleve in Intervalle_entre_deux_notes:
            eleves_notes_gen.append()
    return eleves_notes_gen


def savoir_nombre_moyenne_gen_eleves_entre_n_et_m(moyenne_gen_entre_n_et_m):
    len(moyenne_gen_entre_n_et_m)
    return savoir_nombre_moyenne_gen_eleves_entre_n_et_m



#Fontion recommmencer --- > nouvelle fct par Taqi 

def replay ():
    play = "yes"
    while play in rejoue_commande:
        main ()
        play = input (texte_pour_rejouer)


'''def fct_pr_recommmencer:
    restart = str(input("Recommencer ? Oui ou Non"))
    if restart in commande_pour_quitter:
        break
    elif restart not in commande_pour_quitter:
        pass''' 

#Fct intervalle

def intervalle(mini,maxi):
    intervalle_n_et_m = [ mini , maxi ]

    if mini>maxi:
        return "erreur , la note minimimum est plus grande que la note maximum"
        exit()
    else:
        return intervalle_n_et_m
