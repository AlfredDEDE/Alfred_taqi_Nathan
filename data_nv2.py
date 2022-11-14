# Créé par clatr, le 13/11/2022 en Python 3.7

from random import *

liste_prenoms = ["sam","johny","mat","remy","sacha","eva","usama","justin","gator"
               ,"jean","bubblebea","ines","paul","hugo","lebron","david","lana",
               "aubin","sylvain","masdak"]

liste_noms = ["faitmal","sinz","legamos","fasol","touille","antouilette","fémal",
             "ptipeu","laligator","neimar","lemagatron","alamaternite",
             "emploi","boss","james","michigan","rhoades","sahalor","duryf",
             "code penal"]

#quelque variables
#utile pour des fonctions

notes = []
liste_note_dans_une_matiere= []
moyenne_sup_n = []
moyenne_inf_n = []
eleves_notes_gen_sup_m = []
moyenne_eleves_sup_n = []
nombre_de_note_creer = 0
Intervalle_entre_deux_notes = interval([n, m])

#variabkkles utiles pour le paramètrage du programme

nombre_eleves = len(liste_prenoms)
nombre_de_note_par_matiere = 5


#variable pour raccourcire le main()

texte_d_accueil = \
 "\n Bonjour bienvenue dans le programme pour demander la moyenne"\
 + "A tout moment vous pouvez sortir de l'application en tapant " + '"q"' + " ou " + '"quit"' + "\n"

texte_pour_demander_nom_eleve_auquelle_on_cherche_sa_moyenne=\
 "Veuillez entrer le nom de l'eleve pour qui vous voulez savoir sa moyenne"

texte_pour_demander_nom_eleve_auquelle_on_cherche_ses_notes_dans_toutes_les_matiere = \
    "Veuillez entrer le nom de l'eleve pour qui vous voulez savoir ses notes"


rejoue_commande = \
    ["y", "vasy", "go", "ok", "on y va", "let's go", "oui", "o", "O", "Oui"]

commande_pour_quitter = \
    ["q", "Q", "quitte", "Quit", "by", \
     "au revoir", "see u", "aurevoir", "salut", \
     "je fuis" , "bonne journee", "sortir", "s", "n", ]

texte_pour_re_demander_nom_eleve_auquelle_on_cherche_sa_moyenne = \
    ("\n L'une ou l'autre des situations suivantes s'est présentée :\n" \
    + " *) Vous avez entré un nom qui ne figure pas dans la liste d'eleve\n" \
    + " *) Vous avez entré une moyenne qui ne figure pas entre 0 et 20.\n" \
    +texte_pour_demander_nom_eleve)


texte_sortie_programme = \
   " Merci d avoir utilise ce programme et à la prochaine fois"

eleves_notes_gen = []


def sortie_application ():
    print (texte_sortie_programme)
    exit ()


