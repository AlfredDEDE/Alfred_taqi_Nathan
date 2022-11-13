liste_prenoms = ["sam","johny","mat","remy","sacha","eva","usama","justin","gator"
               ,"jean","bubblebea","ines","paul","hugo","lebron","david","lana",
               "aubin","sylvain","masdak"]

liste_noms = ["faitmal","sinz","legamos","fasol","touille","antouilette","fémal",
             "ptipeu","laligator","neimar","lemagatron","alamaternite",
             "emploi","boss","james","michigan","rhoades","sahalor","duryf",
             "code penal"]

marks = []

texte_d_accueil = \
 "Bonjour bienvenue dans le programme"

texte_pour_demander_nom_eleve =\
 "Veuillez entrer le nom de l'eleve"


#///////////////////////

id_pas_valide = "PAs bon"

def est_bon_prenom (a):
    return a in liste_prenoms

def pas_bon_prenom (a):
    return not (liste_prenoms(a))

def est_bon_nom (a):
    return a in liste_noms

def pas_bon_nom (a):
    return not (liste_noms(a))



def verif_nom_ou_prenom_exist(a) :

    if pas_bon_prenom(a) == False :
        return (est_un_bon_prenom(a))

    if pas_bon_nom(a) == False :
        return (est_un_bon_nom(a))

    if pas_bon_prenom(a) == True :
            print(id_pas_valide)


x = verif_nom_ou_prenom_exist("sam")
print(x)