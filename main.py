from random import *
from Outils_projet_2 import *
from dico import *
from data_nv2 import *
reponse = 0
question_plus_precise = 0

#////////////////////////////////////////////////////////////////////////////

#fonction qui interagissent avec le dico
# ds le main
#fonction qui font ce que l'énoncé demande


def fct_qui_traite_la_reponse_pour_savoir_ce_l_utilisateur_veut():

    if reponse == :
        question_plus_precise =

    if reponse == :
        question_plus_precise =

    if reponse == :
        question_plus_precise =

    if reponse == :
        question_plus_precise =

    return(question_plus_precise)

def fct_qui_demande_a_l_utilisateur_ce_qu_il_veut():
    reponse = input(texte_qui_demande_a_l_utilisateur_ce_qu_il_veut)
    fct_qui_verifie_que_l_utilisateur_ne_rentre_pas_n_importe_quoi()
    fct_qui_traite_la_reponse_pour_savoir_ce_l_utilisateur_veut()

def main():

    fct_qui_demande_a_l_utilisateur_ce_qu_il_veut()
    fct_qui_cherche_ds_le_dico_l_info()
    fct_qui_traite_l_info()
    fct_qui_donne_ce_que_l_utilisateur_a_demander()


#////////////////////////////////////////////////////////////////////////////

print(texte_d_accueil)

main()

print(texte_sortie_programme)