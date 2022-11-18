
from data_nv2 import *
from Outils_projet_2 import *


dico_globale = { \




    "dico_liste_nom_a_prenom" : \

        {  "faitmal":"sam" , "sinz" : "johny" ,  "legamos" : "mat", "fasol" : "remy" ,"touille" : "sacha" , "antouilette" : "eva" \
        , "fémal": "usama" , "ptipeu" : "justin" ,  "laligator": "gator"\
        ,  "neimar" : "jean" ,  "lemagatron" : "bubblebea",  "alamaternite" : "ines" , "emploi" : "paul" ,  "boss" : "hugo", "james" : "lebron",\
        "david" : "michigan","lana" :"rhoades", \
          "sahalor" : "aubin",  "duryf" : "sylvain",  "code penal" :"masdak"  },\

    "dico_eleve_a_matiere_a_note": {\


        "sam" : {"Francais" : creer_des_notes(nombre_de_note_par_matiere ), "Math" : creer_des_notes(nombre_de_note_par_matiere ), \
                "Histoire-Geo" : creer_des_notes(nombre_de_note_par_matiere ) , "Anglais" :creer_des_notes(nombre_de_note_par_matiere ), \
                "Espagnol" : creer_des_notes(nombre_de_note_par_matiere ) , \
                 }, \

        "johny" : {"Francais" : creer_des_notes(nombre_de_note_par_matiere ), "Math" : creer_des_notes(nombre_de_note_par_matiere ), \
                "Histoire-Geo" : creer_des_notes(nombre_de_note_par_matiere ) , "Anglais" :creer_des_notes(nombre_de_note_par_matiere ), \
                "Espagnol" : creer_des_notes(nombre_de_note_par_matiere ) }, \

        "mat" : {"Francais" : creer_des_notes(nombre_de_note_par_matiere ), "Math" : creer_des_notes(nombre_de_note_par_matiere ), \
                "Histoire-Geo" : creer_des_notes(nombre_de_note_par_matiere ) , "Anglais" :creer_des_notes(nombre_de_note_par_matiere ), \
                "Espagnol" : creer_des_notes(nombre_de_note_par_matiere ) }, \

        "remy" : {"Francais" : creer_des_notes(nombre_de_note_par_matiere ), "Math" : creer_des_notes(nombre_de_note_par_matiere ), \
                "Histoire-Geo" : creer_des_notes(nombre_de_note_par_matiere ) , "Anglais" :creer_des_notes(nombre_de_note_par_matiere ), \
                "Espagnol" : creer_des_notes(nombre_de_note_par_matiere ) },\

        "sacha" : {"Francais" : creer_des_notes(nombre_de_note_par_matiere ), "Math" : creer_des_notes(nombre_de_note_par_matiere ), \
                "Histoire-Geo" : creer_des_notes(nombre_de_note_par_matiere ) , "Anglais" :creer_des_notes(nombre_de_note_par_matiere ), \
                "Espagnol" : creer_des_notes(nombre_de_note_par_matiere ) },\

        "eva" : {"Francais" : creer_des_notes(nombre_de_note_par_matiere ), "Math" : creer_des_notes(nombre_de_note_par_matiere ), \
                "Histoire-Geo" : creer_des_notes(nombre_de_note_par_matiere ) , "Anglais" :creer_des_notes(nombre_de_note_par_matiere ), \
                "Espagnol" : creer_des_notes(nombre_de_note_par_matiere ) }, \

        "usama" : {"Francais" : creer_des_notes(nombre_de_note_par_matiere ), "Math" : creer_des_notes(nombre_de_note_par_matiere ), \
                "Histoire-Geo" : creer_des_notes(nombre_de_note_par_matiere ) , "Anglais" :creer_des_notes(nombre_de_note_par_matiere ), \
                "Espagnol" : creer_des_notes(nombre_de_note_par_matiere ) }, \

        "justin": {"Francais": creer_des_notes(nombre_de_note_par_matiere ), "Math": creer_des_notes(nombre_de_note_par_matiere ), \
            "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere ), "Anglais": creer_des_notes(nombre_de_note_par_matiere ), \
            "Espagnol": creer_des_notes(nombre_de_note_par_matiere )},

        "gator": {"Francais": creer_des_notes(nombre_de_note_par_matiere ), "Math": creer_des_notes(nombre_de_note_par_matiere ), \
            "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere ), "Anglais": creer_des_notes(nombre_de_note_par_matiere ), \
            "Espagnol": creer_des_notes(nombre_de_note_par_matiere )}, \

        "jean": {"Francais": creer_des_notes(nombre_de_note_par_matiere ), "Math": creer_des_notes(nombre_de_note_par_matiere ), \
            "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere ), "Anglais": creer_des_notes(nombre_de_note_par_matiere ), \
            "Espagnol": creer_des_notes(nombre_de_note_par_matiere )},

        "bubblebea": {"Francais": creer_des_notes(nombre_de_note_par_matiere),
                      "Math": creer_des_notes(nombre_de_note_par_matiere), \
                      "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere),
                      "Anglais": creer_des_notes(nombre_de_note_par_matiere), \
                      "Espagnol": creer_des_notes(nombre_de_note_par_matiere)}, \
 \
        "ines": {"Francais": creer_des_notes(nombre_de_note_par_matiere),
                 "Math": creer_des_notes(nombre_de_note_par_matiere), \
                 "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere),
                 "Anglais": creer_des_notes(nombre_de_note_par_matiere), \
                 "Espagnol": creer_des_notes(nombre_de_note_par_matiere)}, \
 \
        "paul": {"Francais": creer_des_notes(nombre_de_note_par_matiere),
                 "Math": creer_des_notes(nombre_de_note_par_matiere), \
                 "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere),
                 "Anglais": creer_des_notes(nombre_de_note_par_matiere), \
                 "Espagnol": creer_des_notes(nombre_de_note_par_matiere)}, \
 \
        "hugo": {"Francais": creer_des_notes(nombre_de_note_par_matiere),
                 "Math": creer_des_notes(nombre_de_note_par_matiere), \
                 "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere),
                 "Anglais": creer_des_notes(nombre_de_note_par_matiere), \
                 "Espagnol": creer_des_notes(nombre_de_note_par_matiere)}, \
 \
        "lebron": {"Francais": creer_des_notes(nombre_de_note_par_matiere),
                   "Math": creer_des_notes(nombre_de_note_par_matiere), \
                   "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere),
                   "Anglais": creer_des_notes(nombre_de_note_par_matiere), \
                   "Espagnol": creer_des_notes(nombre_de_note_par_matiere)}, \
 \
        "david": {"Francais": creer_des_notes(nombre_de_note_par_matiere),
                  "Math": creer_des_notes(nombre_de_note_par_matiere), \
                  "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere),
                  "Anglais": creer_des_notes(nombre_de_note_par_matiere), \
                  "Espagnol": creer_des_notes(nombre_de_note_par_matiere)}, \
 \
        "lana": {"Francais": creer_des_notes(nombre_de_note_par_matiere),
                 "Math": creer_des_notes(nombre_de_note_par_matiere), \
                 "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere),
                 "Anglais": creer_des_notes(nombre_de_note_par_matiere), \
                 "Espagnol": creer_des_notes(nombre_de_note_par_matiere)}, \
 \
        "aubin": {"Francais": creer_des_notes(nombre_de_note_par_matiere),
                  "Math": creer_des_notes(nombre_de_note_par_matiere), \
                  "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere),
                  "Anglais": creer_des_notes(nombre_de_note_par_matiere), \
                  "Espagnol": creer_des_notes(nombre_de_note_par_matiere)}, \
 \
        "sylvain": {"Francais": creer_des_notes(nombre_de_note_par_matiere),
                    "Math": creer_des_notes(nombre_de_note_par_matiere), \
                    "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere),
                    "Anglais": creer_des_notes(nombre_de_note_par_matiere), \
                    "Espagnol": creer_des_notes(nombre_de_note_par_matiere)}, \
 \
        "masdak": {"Francais": creer_des_notes(nombre_de_note_par_matiere),
                   "Math": creer_des_notes(nombre_de_note_par_matiere), \
                   "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere),
                   "Anglais": creer_des_notes(nombre_de_note_par_matiere),
                   "Espagnol": creer_des_notes(nombre_de_note_par_matiere)}
 \
 \

}
}


print(moyenne(dico_globale["dico_eleve_a_matiere_a_note"]["david"]["Francais"]))