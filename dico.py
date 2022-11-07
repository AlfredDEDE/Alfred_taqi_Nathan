
#from data import *

#from outils import *


dico = {\

    "Prenom" : {"Francais" : creer_des_notes(), "Math" : creer_des_notes(), \
                "Histoire-Geo" : creer_des_notes() , "Anglais" :creer_des_notes(), \
                "Espagnol" : creer_des_notes() }

                }



print("Les notes de votre fils est " , dico["Prenom"]["Francais"])
