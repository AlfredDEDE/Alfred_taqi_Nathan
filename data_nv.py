# Créé par clatr, le 13/11/2022 en Python 3.7
liste_prenoms = ["sam","johny","mat","remy","sacha","eva","usama","justin","gator"
               ,"jean","bubblebea","ines","paul","hugo","lebron","david","lana",
               "aubin","sylvain","masdak"]

liste_noms = ["faitmal","sinz","legamos","fasol","touille","antouilette","fémal",
             "ptipeu","laligator","neimar","lemagatron","alamaternite",
             "emploi","boss","james","michigan","rhoades","sahalor","duryf",
             "code penal"]

notes = []



texte_d_accueil = \
 "\n Bonjour bienvenue dans le programme pour demander la moyenne"\
 + "A tout moment vous pouvez sortir de l'application en tapant " + '"q"' + " ou " + '"quit"' + "\n"
texte_pour_demander_nom_eleve =\
 "Veuillez entrer le nom de l'eleve pour qui vous voulez savoir sa moyenne"

rejoue_commande = \
    ["y", "yes", "vasy", "go", "ok", "Yes", "on y va", "let's go", "oui", "o", "O", "Oui"]
commande_pour_quitter = \
    ["q", "Q", "quitte", "Quit", "ko", "by", \
     "au revoir", "see u", "aurevoir", "ciao", \
     "je fuis" , "bye", "Out", "sortir", "s", "n", ]

texte_pour_re_demander_nom_eleve = \
    "\nL'une ou l'autre des situations suivantes s'est présentée :\n" \
    + " *) Vous avez entré un nom qui ne figure pas dans la liste d'eleve\n" \
    + " *) Vous avez entré une moyenne qui ne figure pas entre 0 et 20.\n" \
    +texte_pour_demander_nom_eleve



