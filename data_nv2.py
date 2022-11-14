# Créé par clatr, le 13/11/2022 en Python 3.7

from random import *

liste_prenoms = ["sam","johny","mat","remy","sacha","eva","usama","justin","gator"
               ,"jean","bubblebea","ines","paul","hugo","lebron","david","lana",
               "aubin","sylvain","masdak"]

liste_noms = ["faitmal","sinz","legamos","fasol","touille","antouilette","fémal",
             "ptipeu","laligator","neimar","lemagatron","alamaternite",
             "emploi","boss","james","michigan","rhoades","sahalor","duryf",
             "code penal"]


#variables utiles pour le paramètrage du programme

nombre_eleves = len(liste_prenoms)
nombre_de_note_par_matiere = 5

#variables utile pour des fonctions

notes = []
liste_note_dans_une_matiere= []
moyenne_sup_n = []
moyenne_inf_n = []
eleves_notes_gen_sup_m = []
moyenne_eleves_sup_n = []
nombre_de_note_creer = 0
# c faux A CORRIGER TAQI --> Intervalle_entre_deux_notes = interval([n, m])
eleves_notes_gen = []
verification_positivie_ou_negative_sur_si_reponse_autorisé_au_premier_input = "Non"

#variables utile pour les fct ds main


reponse_autoriser_au_premier_input = []
reponse = 0
question_plus_precise = 0


#variable pour raccourcire le main()

rejoue_commande = \
    ["y", "vasy", "go", "ok", "on y va", "let's go", "oui", "o", "O", "Oui"]

commande_pour_quitter = \
    ["q", "Q", "quitte", "Quit", "by", \
     "au revoir", "see u", "aurevoir", "salut", \
     "je fuis" , "bonne journee", "sortir", "s", "n", ]


#textes utilise comme quesiton pr le main()

texte_d_accueil = \
 "\nBonjour bienvenue dans le programme. "\
 + "\nCe programme vous permet de demander une multitude de chose en rapport avec la classe. "\
 + "\nA tout moment vous pouvez sortir de l ' application en tapant " + '"q"' + " ou " + '"quit"'


texte_sortie_programme = \
   " Merci d avoir utilise ce programme et à la prochaine fois"

#Variable sur texte_qui_demande_a_l_utilisateur_ce_qu_il_veut

ensemble_des_mots_clees =  ["eleve_moyenne_diff_matiere" ,"eleve_moyenne_diff_generale", \
                           "eleve_moyenne_comprise_entre_deux_notes", "eleve_notes_ou_moyenne" ]
mot_clee_correpondant_au_texte1 = "eleve_moyenne_diff_matiere"
mot_clee_correpondant_au_texte2 = "eleve_moyenne_diff_generale"
mot_clee_correpondant_au_texte3 = "eleve_moyenne_comprise_entre_deux_notes"
mot_clee_correpondant_au_texte4 = "eleve_notes_ou_moyenne"

texte_qui_demande_a_l_utilisateur_ce_qu_il_veut = \
    "Que voulez-vous faire ?" + \
    "\nVous avez le choix entre : " + \
    "\n-texte1" + "\nLe mot clée correpondant est " + mot_clee_correpondant_au_texte1 + \
    "\n-texte2" + "\nLe mot clée correpondant est " + mot_clee_correpondant_au_texte2 + \
    "\n-texte3" + "\nLe mot clée correpondant est " + mot_clee_correpondant_au_texte3 +\
    "\n-texte4 " + "\nLe mot clée correpondant est " + mot_clee_correpondant_au_texte4 + \
    \
    "\nMettez seulement le mot clée correpondant"

texte_qui_re_demande_a_l_utilisateur_ce_qu_il_veut = \
    "Vous n'avez pas entrer un mot clée" +\
    "\n Pensez à verifier l'orthographe" + \
    texte_qui_demande_a_l_utilisateur_ce_qu_il_veut



#texte des questions plus précise

texte_pour_demander_nom_eleve_auquelle_on_cherche_sa_moyenne=\
 "Veuillez entrer le nom de l'eleve pour qui vous voulez savoir sa moyenne"

texte_pour_demander_nom_eleve_auquelle_on_cherche_ses_notes_dans_toutes_les_matiere = \
    "Veuillez entrer le nom de l'eleve pour qui vous voulez savoir ses notes"

texte_pour_re_demander_nom_eleve_auquelle_on_cherche_sa_moyenne = \
    ("\n L'une ou l'autre des situations suivantes s'est présentée :\n" \
    + " *) Vous avez entré un nom qui ne figure pas dans la liste d'eleve\n" \
    + " *) Vous avez entré une moyenne qui ne figure pas entre 0 et 20.\n" \
    +texte_pour_demander_nom_eleve_auquelle_on_cherche_sa_moyenne)











