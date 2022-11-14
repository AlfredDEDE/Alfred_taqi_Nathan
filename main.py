from random import *
from Outils_projet_2 import *
from dico import *
from data_nv2 import *


#////////////////////////////////////////////////////////////////////////////

#fonction qui interagissent avec le dico
# ds le main
#fonction qui font ce que l'énoncé demande


def fct_qui_cherche_ds_le_dico_l_info():



 def fct_qui_traite_la_reponse_pour_savoir_ce_l_utilisateur_veut_plus_precisemment(reponse):

    if reponse == mot_clee_correpondant_au_texte1:
        question_plus_precise = 1

    if reponse == mot_clee_correpondant_au_texte2 :
        question_plus_precise = 2

    if reponse == mot_clee_correpondant_au_texte3 :
        question_plus_precise = 3

    if reponse == mot_clee_correpondant_au_texte4 :
        question_plus_precise = 4

    return(question_plus_precise)

def fct_qui_demande_a_l_utilisateur_ce_qu_il_veut():
 reponse = input(texte_qui_demande_a_l_utilisateur_ce_qu_il_veut)
 verification_positivie_ou_negative_sur_si_reponse_autorisé_au_premier_input = \
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