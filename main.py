from random import *
from Outils_projet_2 import *
from dico import *
from data_nv2 import *


#////////////////////////////////////////////////////////////////////////////



def fct_qui_cherche_ds_le_dico_les_notes_d_un_eleve_par_matiere(eleve):
    eleve = str(eleve)
    return dico_globale["dico_eleve_a_matiere_a_note"][eleve]



def fct_qui_cherche_ds_le_dico_la_moyenne_d_un_eleve(eleve):

    global ensemble_de_note_de_tout_les_matieres
    eleve = str(eleve)

    for i in range(nombre_de_matière):
        matiere = liste_matiere[i]
        ensemble_de_note_d_une_matiere = dico_globale["dico_eleve_a_matiere_a_note"][eleve][matiere]
        ensemble_de_note_de_tout_les_matieres += ensemble_de_note_d_une_matiere

    return moyenne(ensemble_de_note_de_tout_les_matieres)



def fct_qui_cherche_ds_le_dico_la_liste_eleve_ayant_moyenne_generale_sup_a_n(n1):
    n1 = int(n1)
    for i in range(nombre_eleves):
        eleve = liste_prenoms[i]

        if n1 < fct_qui_cherche_ds_le_dico_la_moyenne_d_un_eleve(eleve):
            list_eleve_cree.append(eleve)
    return list_eleve_cree

def fct_qui_cherche_ds_le_dico_le_nombre_eleve_ayant_moyenne_generale_sup_a_n(n1):
    return len(fct_qui_cherche_ds_le_dico_la_liste_eleve_ayant_moyenne_generale_sup_a_n(n1))



def fct_qui_cherche_ds_le_dico_la_liste_eleve_ayant_moyenne_generale_comprise_entre_n1_n2(n1, n2):
    global list_eleve_cree
    n1 = int(n1)
    n2 = int(n2)

    for i in range(nombre_eleves):
            eleve = liste_prenoms[i]

            if n1 < fct_qui_cherche_ds_le_dico_la_moyenne_d_un_eleve(eleve) < n2:
                list_eleve_cree.append(eleve)
    return list_eleve_cree

def fct_qui_cherche_ds_le_dico_le_nombre_eleve_ayant_moyenne_generale_comprise_entre_n1_n2(n1, n2) :
    return len(fct_qui_cherche_ds_le_dico_la_liste_eleve_ayant_moyenne_generale_comprise_entre_n1_n2(n1, n2))



def fct_qui_cherche_ds_le_dico_la_moyenne_d_un_eleve_dans_une_matière(eleve, matiere):

    moyenne_a_calculer = dico_globale["dico_eleve_a_matiere_a_note"][eleve][matiere]
    moyenne_calculer_pr_une_matiere = moyenne(moyenne_a_calculer)

    return moyenne_calculer_pr_une_matiere


def fct_qui_cherche_ds_le_dico_la_liste_eleve_ayant_moyenne_matiere_sup_a_n(n1, matiere):
    n1 = int(n1)

    for i in range(nombre_eleves):
        eleve = liste_prenoms[i]
        

        if n1 < fct_qui_cherche_ds_le_dico_la_moyenne_d_un_eleve_dans_une_matière(eleve,matiere):
            list_eleve_cree.append(eleve)
    return list_eleve_cree


def fct_qui_cherche_ds_le_dico_l_nb_eleve_ayant_moyenne_matiere_sup_a_n(n1, matiere):
    return len(fct_qui_cherche_ds_le_dico_la_liste_eleve_ayant_moyenne_matiere_sup_a_n(n1, matiere))





def fct_qui_cherche_ds_le_dico_l_info(cas,facteur1_principale,facteur2_secondaire_qd_deux_variables,facteur3_pr_precision):

    if cas == 1 :
        if facteur3_pr_precision == "liste" :
            resulat = fct_qui_cherche_ds_le_dico_la_liste_eleve_ayant_moyenne_matiere_sup_a_n(facteur1_principale,facteur2_secondaire_qd_deux_variables)

        if facteur3_pr_precision == "nombre":
            resulat = fct_qui_cherche_ds_le_dico_l_nb_eleve_ayant_moyenne_matiere_sup_a_n(facteur1_principale, facteur2_secondaire_qd_deux_variables)

    if cas == 2:
        if facteur3_pr_precision == "liste":
            resulat = fct_qui_cherche_ds_le_dico_la_liste_eleve_ayant_moyenne_generale_sup_a_n(facteur1_principale)
        if facteur3_pr_precision == "nombre":
            resulat = fct_qui_cherche_ds_le_dico_le_nombre_eleve_ayant_moyenne_generale_sup_a_n(facteur1_principale)

    if cas == 3:
        if facteur3_pr_precision == "liste":
            resulat =fct_qui_cherche_ds_le_dico_la_liste_eleve_ayant_moyenne_generale_comprise_entre_n1_n2(facteur1_principale,facteur2_secondaire_qd_deux_variables)
        if facteur3_pr_precision == "nombre":
            resulat =fct_qui_cherche_ds_le_dico_le_nombre_eleve_ayant_moyenne_generale_comprise_entre_n1_n2(facteur1_principale,facteur2_secondaire_qd_deux_variables)

    if cas == 4:
        if facteur3_pr_precision == "moyenne":
            resulat = fct_qui_cherche_ds_le_dico_la_moyenne_d_un_eleve(facteur1_principale)
        if facteur3_pr_precision == "note":
            resulat = fct_qui_cherche_ds_le_dico_les_notes_d_un_eleve_par_matiere(facteur1_principale)
    return resulat

def fct_qui_traite_la_reponse_pour_savoir_ce_l_utilisateur_veut_plus_precisemment(reponse):
    global question_plus_precise1
    global facteur1_principale
    global facteur3_pr_precision
    global facteur2_secondaire_qd_deux_variables
    global nom_eleve

    if reponse == mot_clee_correpondant_au_texte1:
        question_plus_precise1 = texte_pour_demander_n_et_ainsi_avoir_le_nombre_ou_la_liste_eleve_ayant_une_moyenne_dans_une_matiere_supérieure_à_n_sur_20
        cas = 1

    if reponse == mot_clee_correpondant_au_texte2:
        question_plus_precise1 = texte_pour_demander_m_et_ainsi_avoire_la_liste_ou_le_nombre_eleve_ayant_moyennes_supérieures_à_m_sur_20
        cas = 2

    if reponse == mot_clee_correpondant_au_texte3:
        question_plus_precise1 = texte_pour_demander_première_notes_pour_avoir_le_nombre_ou_liste_eleve_ayant_une_moyenne_entre_n1_sur_20_et_n2_sur_20
        cas = 3

    if reponse == mot_clee_correpondant_au_texte4:
        question_plus_precise1 = texte_pour_demander_nom_eleve_auquelle_on_cherche_info
        cas = 4

    reponse = input(question_plus_precise1)

    if cas == 4 :
        while verif_nom_ou_prenom_exist(reponse) == False:
                reponse = input(texte_pour_re_demander_nom_eleve_auquelle_on_cherche_info_dans_toutes_les_matiere_prenom)

        if reponse in liste_noms:
            reponse = str(reponse)
            reponse = dico_globale["dico_liste_nom_a_prenom"][reponse]

        nom_eleve = reponse
        facteur1_principale = nom_eleve
        reponse = input(texte_pr_demander_plus_precisement_moyenne_ou_note)

        while fct_qui_verifife_que_l_utilisateur_entre_soit_moyenne_soit_note(reponse) == False:
            reponse = input(texte_pr_redemander_plus_precisement_moyenne_ou_note)

        moyenne_ou_note = reponse
        facteur3_pr_precision = moyenne_ou_note

    else:

        while fct_qui_verifie_que_l_utilisateur_entre_une_moyenne_comprise_entre_0_et_20(reponse) == False:
            reponse = input(text_pour_redemander_une_note)

        note = reponse
        facteur1_principale = note

        reponse = input(texte_pr_demander_plus_precisement_liste_ou_nombre)
        while fct_qui_verifife_que_l_utilisateur_entre_soit_liste_soit_nombre(reponse) == False:
            reponse = input(texte_pr_redemander_plus_precisement_liste_ou_nombre)

        liste_ou_nombre = reponse
        facteur3_pr_precision = liste_ou_nombre

        if cas == 1:
            reponse = input(texte_pour_demander_la_matiere_et_ainsi_avoir_le_nombre_ou_la_liste_eleve_ayant_une_moyenne_dans_une_matiere_supérieure_à_n_sur_20)
            while fct_qui_verifie_que_l_utilisateur_entre_une_matiere(reponse) == False:
                reponse = input(texte_pour_demander_la_matiere_et_ainsi_avoir_le_nombre_ou_la_liste_eleve_ayant_une_moyenne_dans_une_matiere_supérieure_à_n_sur_20)
            facteur2_secondaire_qd_deux_variables = reponse

        if cas == 3:
            reponse = input(texte_pour_demander_deuxieme_notes_pour_avoir_le_nombre_ou_liste_eleve_ayant_une_moyenne_entre_n1_sur_20_et_n2_sur_20)

            while fct_qui_verifie_que_l_utilisateur_entre_une_moyenne_comprise_entre_0_et_20(reponse) == False:
                reponse = input(text_pour_redemander_une_note)
            facteur2_secondaire_qd_deux_variables = reponse

    return (cas,facteur1_principale,facteur2_secondaire_qd_deux_variables,facteur3_pr_precision)

def fct_qui_demande_a_l_utilisateur_ce_qu_il_veut():
    reponse = input(texte_qui_demande_a_l_utilisateur_ce_qu_il_veut)

    if reponse == "q":
        exit()

    while fct_qui_verifie_que_l_utilisateur_ne_rentre_pas_n_importe_quoi_au_premier_input(reponse) == False:

        reponse = input(texte_qui_re_demande_a_l_utilisateur_ce_qu_il_veut)
        
        if reponse == "q":
            exit()
        
        fct_qui_verifie_que_l_utilisateur_ne_rentre_pas_n_importe_quoi_au_premier_input(reponse)
        
        reponse = fct_qui_traite_la_reponse_pour_savoir_ce_l_utilisateur_veut_plus_precisemment(reponse)

        if reponse == "q":
            exit()

    return(reponse)


def fct_qui_donne_ce_que_l_utilisateur_a_demander(resultat):
    print("Voici ce que vous avez demander : \n")
    print(resultat)




def main():

        reponse_sous_forme_de_4_critere = fct_qui_demande_a_l_utilisateur_ce_qu_il_veut()
        resultat = fct_qui_cherche_ds_le_dico_l_info(reponse_sous_forme_de_4_critere[0],reponse_sous_forme_de_4_critere[1],reponse_sous_forme_de_4_critere[2], \
                                            reponse_sous_forme_de_4_critere[3])
        fct_qui_donne_ce_que_l_utilisateur_a_demander(resultat)

#////////////////////////////////////////////////////////////////////////////

print(texte_d_accueil)

print()

main()

print(texte_sortie_programme)
