from random import *
from Outils_projet_2 import *
from dico import *
from data_nv2 import *


#////////////////////////////////////////////////////////////////////////////

#fonction qui interagissent avec le dico
# ds le main
#fonction qui font ce que l'énoncé demande



def fct_qui_cherche_ds_le_dico_les_notes_d_un_eleve_par_matière(eleve):
    eleve = str(eleve)
    return dico_globale["dico_eleve_a_matiere_a_note"][eleve]

def fct_qui_cherche_ds_le_dico_la_moyenne_d_un_eleve(eleve):
    eleve = str(eleve)

    for i in range(nombre_de_matière):
        matiere = liste_matiere[i]
        ensemble_de_note_d_une_matiere = dico_globale["dico_eleve_a_matiere_a_note"][eleve][matiere]
        print(ensemble_de_note_d_une_matiere)
        ensemble_de_note_de_tout_les_matieres += ensemble_de_note_d_une_matiere

    return moyenne(ensemble_de_note_de_tout_les_matieres)


def fct_qui_cherche_ds_le_dico_la_liste_eleve_ayant_moyenne_generale_comprise_entre_n1_n2(n1, n2):
    if fct_qui_verifie_que_l_utilisateur_entre_une_moyenne_comprise_entre_0_et_20 == False :
        return False

    else:

        for i in range(nombre_eleves):
            eleve = list_eleve[i]

            if n1 < fct_qui_cherche_ds_le_dico_la_moyenne_d_un_eleve(eleve) < n2:
                list_eleve.append(eleve)


def fct_qui_cherche_ds_le_dico_l_info():

    fct_qui_cherche_ds_le_dico_l_nb_eleve_ayant_moyenne_generale_sup_ou_inf_a_n(n)
    fct_qui_cherche_ds_le_dico_la_liste_eleve_ayant_moyenne_generale_sup_ou_inf_a_n(n)

    fct_qui_cherche_ds_le_dico_l_nb_eleve_ayant_moyenne_matiere_sup_ou_inf_a_n(n,matiere)
    fct_qui_cherche_ds_le_dico_la_liste_eleve_ayant_moyenne_matiere_sup_ou_inf_a_n(n, matiere)

    fct_qui_cherche_ds_le_dico_l_nb_eleve_ayant_moyenne_generale_comprise_entre_n1_n2(n1,n2)
    fct_qui_cherche_ds_le_dico_la_liste_eleve_ayant_moyenne_generale_comprise_entre_n1_n2(n1,n2)

    fct_qui_cherche_ds_le_dico_la_moyenne_d_un_eleve(eleve)
    fct_qui_cherche_ds_le_dico_les_notes_d_un_eleve_par_matière(eleve)

def fct_qui_traite_la_reponse_pour_savoir_ce_l_utilisateur_veut_plus_precisemment(reponse):
    global question_plus_precise1
    if reponse == mot_clee_correpondant_au_texte1:
        question_plus_precise1 = texte_pour_demander_m_et_ainsi_avoire_la_liste_ou_le_nombre_eleve_ayant_moyennes_supérieures_à_m_sur_20

    if reponse == mot_clee_correpondant_au_texte2:
        question_plus_precise1 = texte_pour_demander_n_et_ainsi_avoir_le_nombre_ou_la_liste_eleve_ayant_une_moyenne_dans_une_matiere_supérieure_à_n_sur_20

    if reponse == mot_clee_correpondant_au_texte3:
        question_plus_precise1 = texte_pour_demander_deux_notes_pour_avoir_le_nombre_ou_liste_eleve_ayant_une_moyenne_entre_n1_sur_20_et_n2_sur_20

    if reponse == mot_clee_correpondant_au_texte4:
        question_plus_precise1 = texte_pour_demander_nom_eleve_auquelle_on_cherche_info


    reponse = input(question_plus_precise1)


    while verif_nom_ou_prenom_exist(reponse) == False:
            reponse = input(texte_pour_re_demander_nom_ou_prenom_eleve_auquelle_on_cherche_sa_moyenne)


    if reponse in liste_noms:
        reponse = str(reponse)
        reponse = dico_globale["dico_liste_nom_a_prenom"][reponse]
    cas = 4

    return (reponse)

def fct_qui_demande_a_l_utilisateur_ce_qu_il_veut():
    reponse = input(texte_qui_demande_a_l_utilisateur_ce_qu_il_veut)



    while fct_qui_verifie_que_l_utilisateur_ne_rentre_pas_n_importe_quoi_au_premier_input(reponse) == False:

        reponse = input(texte_qui_re_demande_a_l_utilisateur_ce_qu_il_veut)
        fct_qui_verifie_que_l_utilisateur_ne_rentre_pas_n_importe_quoi_au_premier_input(reponse)


    reponse = input(fct_qui_traite_la_reponse_pour_savoir_ce_l_utilisateur_veut_plus_precisemment(reponse))

    return(reponse)

def main():

    fct_qui_demande_a_l_utilisateur_ce_qu_il_veut()
    fct_qui_cherche_ds_le_dico_l_info()
    fct_qui_traite_l_info()
    fct_qui_donne_ce_que_l_utilisateur_a_demander()


#////////////////////////////////////////////////////////////////////////////

print(texte_d_accueil)

main()

print(texte_sortie_programme)