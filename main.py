from random import *
from Outils_projet_2 import *
from dico import *
from data_nv2 import *


#////////////////////////////////////////////////////////////////////////////

#fonction qui interagissent avec le dico
# ds le main
#fonction qui font ce que l'énoncé demande


def fct_qui_cherche_ds_le_dico_l_info():
    x= 1



def fct_qui_traite_la_reponse_pour_savoir_ce_l_utilisateur_veut_plus_precisemment(reponse):

    if reponse == mot_clee_correpondant_au_texte1:
        question_plus_precise1 = 1

    if reponse == mot_clee_correpondant_au_texte2 :
        question_plus_precise1 = 2

    if reponse == mot_clee_correpondant_au_texte3 :
        question_plus_precise1 = 3

    if reponse == mot_clee_correpondant_au_texte4 :
        question_plus_precise1 = 4
        reponse = input(texte_pour_demander_nom_eleve_auquelle_on_cherche_ses_notes_dans_toutes_les_matiere)

        while  verif_nom_ou_prenom_exist(reponse) == False :
            reponse = input(texte_pour_re_demander_nom_eleve_auquelle_on_cherche_sa_moyenne)

        reponse = input(texte_pour_demander_nom_eleve_auquelle_on_cherche_ses_notes_dans_toutes_les_matiere_nom_ou_prenom)

        while verif_nom_ou_prenom_exist(reponse) == False:
            reponse = input(texte_pour_re_demander_nom_eleve_auquelle_on_cherche_ses_notes_dans_toutes_les_matiere_nom_ou_prenom)

    return(reponse)

def fct_qui_demande_a_l_utilisateur_ce_qu_il_veut():
    reponse = input(texte_qui_demande_a_l_utilisateur_ce_qu_il_veut)
    verification_positivie_ou_negative_sur_si_reponse_autorise_au_premier_input = \
    fct_qui_verifie_que_l_utilisateur_ne_rentre_pas_n_importe_quoi_au_premier_input(reponse)

    while verification_positivie_ou_negative_sur_si_reponse_autorisé_au_premier_input == False:

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