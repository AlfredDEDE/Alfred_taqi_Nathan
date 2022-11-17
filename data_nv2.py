# Créé par clatr, le 13/11/2022 en Python 3.7

from random import *

liste_prenoms = ["sam","johny","mat","remy","sacha","eva","usama","justin","gator"
               ,"jean","bubblebea","ines","paul","hugo","lebron","david","lana",
               "aubin","sylvain","masdak"]

liste_noms = ["faitmal","sinz","legamos","fasol","touille","antouilette","fémal",
             "ptipeu","laligator","neimar","lemagatron","alamaternite",
             "emploi","boss","james","michigan","rhoades","sahalor","duryf",
             "code penal"]

liste_matiere = [ "Francais", "Math", "Histoire-Geo", "Anglais", "Espagnol" ]

nombre_de_note_par_matiere = 5



#/////////////////////////////////////////////////////////////////////////////

#variables utiles pour le programme

nombre_eleves = len(liste_prenoms)
nombre_de_matière = len(liste_matière)
nombre_de_note_totale = nombre_de_matière * nombre_de_note_par_matiere

#variables utile pour des fonctions

notes = []
liste_note_dans_une_matiere= []
moyenne_sup_n = []
moyenne_inf_n = []
eleves_notes_gen_sup_m = []
moyenne_eleves_sup_n = []
moyenne_inf_n = []
nombre_de_note_creer = 0
# c bon corrige , nouvelle fct intervalle dans outil + ligne de dessous
des_notes = []


note_entre_0_et_20 = []
eleves_notes_gen = []
verification_positivie_ou_negative_sur_si_reponse_autorise_au_premier_input = "Non"

#variables utile pour les fct ds main


reponse_autoriser_au_premier_input = []
reponse = 0
question_plus_precise = 0


#variable pour raccourcire le main()

texte_pour_rejouer = \
    ["Voulez vous relancer une rechercher ?"]

rejoue_commande = \
    ["y", "vasy", "go", "ok", "on y va", "let's go", "oui", "o", "O", "Oui" ,"yes"]

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

texte_qui_demande_mot_clef = "Entrez les mots clef correspondants :"

texte1 = "Si vous desirez savoir le nombre ou la liste d'eleve ayant une moyenne generale superieur ou inferieur à celle-ci " + texte_qui_demande_mot_clef
texte2 = "Si vous desirez savoir le nombre ou la liste d'eleve ayant une moyenne dans une matière superieur ou inferieur à celle-ci " + texte_qui_demande_mot_clef
texte3 = "Si vous desirez savoir le nombre ou la liste d'eleve ayant une moyenne generale comprise entre un intervalle" + texte_qui_demande_mot_clef
texte4 = "Si vous desirez savoir les notes et/ou la moyenne d'un eleve" + texte_qui_demande_mot_clef


mot_clee_correpondant_au_texte1 = "eleve_moyenne_diff_matiere"
mot_clee_correpondant_au_texte2 = "eleve_moyenne_diff_generale"
mot_clee_correpondant_au_texte3 = "eleve_moyenne_comprise_entre_deux_notes"
mot_clee_correpondant_au_texte4 = "eleve_notes_ou_moyenne"

texte_qui_demande_a_l_utilisateur_ce_qu_il_veut = \
    "Que voulez-vous faire ?" + \
    "\nVous avez le choix entre : " + \
    "\n-" + texte1 + "\nLe mot clée correpondant est " + mot_clee_correpondant_au_texte1 + \
    "\n-" + texte2 + "\nLe mot clée correpondant est " + mot_clee_correpondant_au_texte2 + \
    "\n-" + texte3 + "\nLe mot clée correpondant est " + mot_clee_correpondant_au_texte3 +\
    "\n-" + texte4 + "\nLe mot clée correpondant est " + mot_clee_correpondant_au_texte4 + \
    \
    "\nMettez seulement le mot clée correpondant"
texte_qui_indique_que_la_note_pas_entre_0_et_20 = \
    "\n La moyenne entrée n'est pas entre 0 et 20"
texte_qui_re_demande_a_l_utilisateur_ce_qu_il_veut = \
    "Vous n'avez pas entrer un mot clée" +\
    "\n Pensez à verifier l'orthographe" + \
    texte_qui_demande_a_l_utilisateur_ce_qu_il_veut



#texte des questions plus précise

texte_pour_demander_nom_eleve_auquelle_on_cherche_sa_moyenne=\
 "Veuillez entrer le nom de l'eleve dont vous voulez savoir sa moyenne"

texte_pour_demander_nom_eleve_auquelle_on_cherche_ses_notes_dans_toutes_les_matiere = \
    "Veuillez entrer le nom de l'eleve dont vous voulez savoir ses notes"

texte_pour_re_demander_nom_eleve_auquelle_on_cherche_sa_moyenne = \
    ("\n L'une ou l'autre des situations suivantes s'est présentée :\n" \
    + " *) Vous avez entré un nom qui ne figure pas dans la liste d'élève\n" \
    + " *) Vous avez entré une moyenne qui ne figure pas entre 0 et 20.\n" \
    +texte_pour_demander_nom_eleve_auquelle_on_cherche_sa_moyenne)

texte_pour_demander_nom_eleve_auquelle_on_cherche_ses_notes_dans_toutes_les_matiere_nom_ou_prenom = \
    "Voulez vous recherchez pas son nom ou prenom" + "Entrez soit nom soit prenom (sans maj ou accent)"

texte_pour_re_demander_nom_eleve_auquelle_on_cherche_ses_notes_dans_toutes_les_matiere_nom_ou_prenom = \
    "Ecrivez bien le nom ou prenom" + "Voici leur ecriture" + liste_prenoms + \
    "\n" + liste_noms + \
    "\n" + texte_pour_demander_nom_eleve_auquelle_on_cherche_ses_notes_dans_toutes_les_matiere_nom_ou_prenom

# endessus ce sont les question que tu (alfred) m'a (Taqi) de faire :


# La liste et/ou le nombre d’élèves ayant n moyennes supérieures à m sur 20

texte_pour_demander_la_liste_eleve_ayant_moyennes_supérieures_à_m_sur_20 = \
    "Entrer la moyenne dont vous voulez savoir la liste ou le nombre d’élèves ayant une moyenne génerale supérieure"

texte_pour_redemander_la_liste_eleve_ayant_moyennes_supérieures_à_m_sur_20= \
("\n L'une ou l'autre des situations suivantes s'est présentée :\n"  "Vous n'avez pas entré un nombre"
 + ") Vous avez entré une moyenne qui ne figure pas entre 0 et 20.\n" +texte_pour_demander_nom_eleve)

texte_pr_demander_plus_precisement_liste_ou_note = ("Voulez vous la liste ou le nombre d’élèves")

# La liste et/ou le nombre d’élèves ayant une moyenne en Maths supérieure à n/20

texte_pour_demander_le_nombre_eleve_ayant_une_moyenne_dans_une_matiere_supérieure_à_n_sur_20 = \
("Veuillez entrer la moyenne pour laquelle vous voulez savoir la liste ou nombre d’eleve ayant une moyenne dans une matiere supérieur a celle-ci") + \
 "\n Entrez en premier la moyenne puis une virgule et la matiere (Maths,Francais,HG, Anglais, Espagnol)"

texte_pour_redemander_nombre_eleve_ayant_une_moyenne_en_maths_supérieure_à_n_sur_20 = \
("\n L'une ou l'autre des situations suivantes s'est présentée :\n"  + " Vous avez entré un nom qui ne figure pas dans la liste d'eleve\n"
+ "Vous avez entré une moyenne qui ne figure pas entre 0 et 20.\n" +texte_pour_redemander_nombre_eleve_ayant_une_moyenne_en_maths_supérieure_à_n_sur_20)\

texte_pr_demander_plus_precisement = ("Voulez vous la liste ou le nombre d’élèves")

# La liste et/ou le nombre d’élèves ayant une moyenne générale comprise entre n1/20 et n2/20

texte_pour_demander_le_nombre_eleve_ayant_une_moyenne_entre_n1_sur_20_et_n2_sur_20 = \
("Veuillez entrer la note n1 puis la note n2 pour trouver le nombre d'eleves ayant une moyenne entre elles")

text_pour_redemander_le_nombre_eleve_ayant_une_moyenne_entre_n1_sur_20_et_n2_sur_20 = \
("\n L'une ou l'autre des situations suivantes s'est présentée :\n"  + " Vous avez entré une note n1 superieur a n2" \
 + "Vous avez entré des notes qui ne sont pas entre 0 et 20" + texte_pour_demander_le_nombre_eleve_ayant_une_moyenne_entre_n1_sur_20_et_n2_sur_20)

texte_pr_demander_plus_precisement = ("Voulez vous la liste ou le nombre d’élèves")

#les notes de l’élève nom: "Jacquesson", prénom: "Michel"

texte_pour_demander_le_nom_et_prenom_eleve = \
("Veuillez entrer le nom puis le prénom de l'élève recherché")

texte_pour_redemander_le_nom_et_prenom_eleve = \
("\n Le nom se trouve pas dans la base de donnée" + texte_pour_demander_le_nom_et_prenom_eleve )
