
from data import *
from outils import *

dico_eleve_a_matire_a_note = { \
 \
    "Prenom": {"Francais": creer_des_notes(), "Math": creer_des_notes(), \
               "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(), \
               "Espagnol": creer_des_notes()}, \



    "sam" : {"Francais" : creer_des_notes(), "Math" : creer_des_notes(), \
                "Histoire-Geo" : creer_des_notes() , "Anglais" :creer_des_notes(), \
                "Espagnol" : creer_des_notes() }, \

    "johny" : {"Francais" : creer_des_notes(), "Math" : creer_des_notes(), \
                "Histoire-Geo" : creer_des_notes() , "Anglais" :creer_des_notes(), \
                "Espagnol" : creer_des_notes() }, \

    "mat" : {"Francais" : creer_des_notes(), "Math" : creer_des_notes(), \
                "Histoire-Geo" : creer_des_notes() , "Anglais" :creer_des_notes(), \
                "Espagnol" : creer_des_notes() }, \

    "remy" : {"Francais" : creer_des_notes(), "Math" : creer_des_notes(), \
                "Histoire-Geo" : creer_des_notes() , "Anglais" :creer_des_notes(), \
                "Espagnol" : creer_des_notes() },\

    "sacha" : {"Francais" : creer_des_notes(), "Math" : creer_des_notes(), \
                "Histoire-Geo" : creer_des_notes() , "Anglais" :creer_des_notes(), \
                "Espagnol" : creer_des_notes() },\

    "eva" : {"Francais" : creer_des_notes(), "Math" : creer_des_notes(), \
                "Histoire-Geo" : creer_des_notes() , "Anglais" :creer_des_notes(), \
                "Espagnol" : creer_des_notes() }, \

    "usama" : {"Francais" : creer_des_notes(), "Math" : creer_des_notes(), \
                "Histoire-Geo" : creer_des_notes() , "Anglais" :creer_des_notes(), \
                "Espagnol" : creer_des_notes() }, \

    "justin": {"Francais": creer_des_notes(), "Math": creer_des_notes(), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(), \
            "Espagnol": creer_des_notes()},

    "gator": {"Francais": creer_des_notes(), "Math": creer_des_notes(), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(), \
            "Espagnol": creer_des_notes()}, \

    "jean": {"Francais": creer_des_notes(), "Math": creer_des_notes(), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(), \
            "Espagnol": creer_des_notes()},

    "bubblebea": {"Francais": creer_des_notes(), "Math": creer_des_notes(), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(), \
            "Espagnol": creer_des_notes()}, \

    "ines": {"Francais": creer_des_notes(), "Math": creer_des_notes(), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(), \
            "Espagnol": creer_des_notes()}, \

    "paul": {"Francais": creer_des_notes(), "Math": creer_des_notes(), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(), \
            "Espagnol": creer_des_notes()}, \

    "hugo": {"Francais": creer_des_notes(), "Math": creer_des_notes(), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(), \
            "Espagnol": creer_des_notes()}, \

    "lebron": {"Francais": creer_des_notes(), "Math": creer_des_notes(), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(), \
            "Espagnol": creer_des_notes()}, \

    "david": {"Francais": creer_des_notes(), "Math": creer_des_notes(), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(), \
            "Espagnol": creer_des_notes()}, \

    "lana": {"Francais": creer_des_notes(), "Math": creer_des_notes(), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(), \
            "Espagnol": creer_des_notes()}, \

    "aubin": {"Francais": creer_des_notes(), "Math": creer_des_notes(), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(), \
            "Espagnol": creer_des_notes()}, \

    "sylvain": {"Francais": creer_des_notes(), "Math": creer_des_notes(), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(), \
            "Espagnol": creer_des_notes()}, \

    "masdak": {"Francais": creer_des_notes(), "Math": creer_des_notes(), \
            "Histoire-Geo": creer_des_notes(), "Anglais": creer_des_notes(), \
            "Espagnol": creer_des_notes()}, \
    }


dico_matiere_a_note = { \

    "Francais": {"Moyenne " : moyenne_eleves_gen_ds_une_matiere() \
            "Moyenne de tous les eleves" :\
                moyenne_de_tous_les_eleves_ds_une_matiere() \
            "Notes de tous les eleves" : \
                notes_de_tous_les_eleves_ds_une_matiere()
                  }, \

    "Math": {"Moyenne " : moyenne_eleves_gen_ds_une_matiere() \
            "Moyenne de tous les eleves" :\
                moyenne_de_tous_les_eleves_ds_une_matiere() \
            "Notes de tous les eleves" : \
                notes_de_tous_les_eleves_ds_une_matiere()
                  }, \

    "Histoire-Geo": {"Moyenne " : moyenne_eleves_gen_ds_une_matiere() \
            "Moyenne de tous les eleves" :\
                moyenne_de_tous_les_eleves_ds_une_matiere() \
            "Notes de tous les eleves" : \
                notes_de_tous_les_eleves_ds_une_matiere()
                  }, \

    "Anglais": {"Moyenne " : moyenne_eleves_gen_ds_une_matiere() \
            "Moyenne de tous les eleves" :\
                moyenne_de_tous_les_eleves_ds_une_matiere() \
            "Notes de tous les eleves" : \
                notes_de_tous_les_eleves_ds_une_matiere()
                  }, \

    "Espagnol": {"Moyenne " : moyenne_eleves_gen_ds_une_matiere() \
            "Moyenne de tous les eleves" :\
                moyenne_de_tous_les_eleves_ds_une_matiere() \
            "Notes de tous les eleves" : \
                notes_de_tous_les_eleves_ds_une_matiere()
                  }, \

    }

