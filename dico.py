
from data_nv2 import *
from Outils_projet_2 import *


dico_globale = { \

    "dico_theorique" : { \

        "Prenom": {"Francais": creer_des_notes(nombre_de_note_par_matiere), "Math": creer_des_notes(nombre_de_note_par_matiere ), \
               "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere ), "Anglais": creer_des_notes(nombre_de_note_par_matiere ), \
               "Espagnol": creer_des_notes(nombre_de_note_par_matiere ), \
               }, \

        "Matière": {"Moyenne " : moyenne_eleves_gen_ds_une_matiere(), \
            "Moyenne de tous les eleves" :\
                moyenne_de_tous_les_eleves_ds_une_matiere(), \
            "Notes de tous les eleves" : \
                notes_de_tous_les_eleves_ds_une_matiere()
                  }


         }, \


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

        "bubblebea": {"Francais": creer_des_notes(), "Math": creer_des_notes(nombre_de_note_par_matiere ), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(nombre_de_note_par_matiere ), \
            "Espagnol": creer_des_notes()}, \

        "ines": {"Francais": creer_des_notes(), "Math": creer_des_notes(nombre_de_note_par_matiere ), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(nombre_de_note_par_matiere ), \
            "Espagnol": creer_des_notes()}, \

        "paul": {"Francais": creer_des_notes(), "Math": creer_des_notes(nombre_de_note_par_matiere ), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(nombre_de_note_par_matiere ), \
            "Espagnol": creer_des_notes()}, \

        "hugo": {"Francais": creer_des_notes(), "Math": creer_des_notes(nombre_de_note_par_matiere ), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(nombre_de_note_par_matiere ), \
            "Espagnol": creer_des_notes()}, \

        "lebron": {"Francais": creer_des_notes(), "Math": creer_des_notes(nombre_de_note_par_matiere ), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(nombre_de_note_par_matiere ), \
            "Espagnol": creer_des_notes()}, \

        "david": {"Francais": creer_des_notes(nombre_de_note_par_matiere ), "Math": creer_des_notes(nombre_de_note_par_matiere ), \
            "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere ), "Anglais": creer_des_notes(nombre_de_note_par_matiere ), \
            "Espagnol": creer_des_notes(nombre_de_note_par_matiere )}, \

        "lana": {"Francais": creer_des_notes(nombre_de_note_par_matiere ), "Math": creer_des_notes(nombre_de_note_par_matiere ), \
            "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere ), "Anglais": creer_des_notes(nombre_de_note_par_matiere ), \
            "Espagnol": creer_des_notes(nombre_de_note_par_matiere )}, \

        "aubin": {"Francais": creer_des_notes(nombre_de_note_par_matiere ), "Math": creer_des_notes(nombre_de_note_par_matiere ), \
            "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere ), "Anglais": creer_des_notes(nombre_de_note_par_matiere ), \
            "Espagnol": creer_des_notes(nombre_de_note_par_matiere )}, \

        "sylvain": {"Francais": creer_des_notes(nombre_de_note_par_matiere ), "Math": creer_des_notes(nombre_de_note_par_matiere ), \
            "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere ), "Anglais": creer_des_notes(nombre_de_note_par_matiere ), \
            "Espagnol": creer_des_notes(nombre_de_note_par_matiere )}, \

        "masdak": {"Francais": creer_des_notes(nombre_de_note_par_matiere ), "Math": creer_des_notes(nombre_de_note_par_matiere ), \
            "Histoire-Geo": creer_des_notes(nombre_de_note_par_matiere ), "Anglais": creer_des_notes(nombre_de_note_par_matiere ), \
            "Espagnol": creer_des_notes(nombre_de_note_par_matiere )}, \
     \
    "dico_matiere_a_note": { \

        "Francais": {"Moyenne " : moyenne_eleves_gen_ds_une_matiere(), \
            "Moyenne de tous les eleves" :\
                moyenne_de_tous_les_eleves_ds_une_matiere(), \
            "Notes de tous les eleves" : \
                notes_de_tous_les_eleves_ds_une_matiere(),
                  }, \

        "Math": {"Moyenne " : moyenne_eleves_gen_ds_une_matiere(), \
            "Moyenne de tous les eleves" :\
                moyenne_de_tous_les_eleves_ds_une_matiere(), \
            "Notes de tous les eleves" : \
                notes_de_tous_les_eleves_ds_une_matiere(),
                  }, \

        "Histoire-Geo": {"Moyenne " : moyenne_eleves_gen_ds_une_matiere(), \
            "Moyenne de tous les eleves" : \
                moyenne_de_tous_les_eleves_ds_une_matiere(), \
            "Notes de tous les eleves" : \
                notes_de_tous_les_eleves_ds_une_matiere(),
                  }, \

        "Anglais": {"Moyenne " : moyenne_eleves_gen_ds_une_matiere(), \
            "Moyenne de tous les eleves" :\
                moyenne_de_tous_les_eleves_ds_une_matiere(), \
            "Notes de tous les eleves" : \
                notes_de_tous_les_eleves_ds_une_matiere(),
                  }, \

        "Espagnol": {"Moyenne " : moyenne_eleves_gen_ds_une_matiere(), \
            "Moyenne de tous les eleves" :\
                moyenne_de_tous_les_eleves_ds_une_matiere(), \
            "Notes de tous les eleves" : \
                notes_de_tous_les_eleves_ds_une_matiere(),
                  }, \

    } \


    }
    }
