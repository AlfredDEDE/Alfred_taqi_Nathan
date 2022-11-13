from random import *
from data import *
from dico import *
from outil import *

def creer_une_note():
    marks.append(randint(0, 20))
    return marks

def determiner_le_nombre_de_note():
    length = randint(3, 8)
    return length

def creer_des_notes():
    for i in range(determiner_le_nombre_de_note()):
        creer_une_note()
    return marks

