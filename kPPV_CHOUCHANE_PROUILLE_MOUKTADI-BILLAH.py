"""
Choixpeaux Magique partie 1


REGLES:
Après le lancement du programme, il suffit d'entrer une valeur de k qui determinera 
le nombre des k plus proche voisins utilisés lors de la recherche. Les résultats pour les profils types 
s'affiche alors dans la foulée. 
On vous demandera alors si vous souhaitez entrer manuellement des valeurs pour les 4 caractéristiques. 
Si oui, après les avoir rentrées, le résultat s'affichera. 


AUTEURS:
Malik Chouchane 
Samy Mouktadi Billah
Odon Prouille

LICENCE:
Pas de licence 

VERSION:
FINALE de la 1ere partie

DATE DE DERNIERE REVISION:
02/02/2024


ADRESSE GITHUB: 
https://github.com/odonp/Choixpeaux-Magique

"""

# coding: utf-8

#import des modules

import csv
from math import sqrt

#définition des constantes


profils_tab = \
    [{'Courage': 9,'Ambition': 2,'Intelligence': 8,'Good': 9},
     {'Courage': 6,'Ambition': 7,'Intelligence': 9,'Good': 7},
     {'Courage': 3,'Ambition': 8,'Intelligence': 6,'Good': 3},
     {'Courage': 2,'Ambition': 3,'Intelligence': 7,'Good': 8},
     {'Courage': 3,'Ambition': 4,'Intelligence': 8,'Good': 8}]


#définition des variables 

poudlard_characters = []


#définition des fonctions dans l'ordre d'utilisation

def k_plus_proche_voisin(tab_caracteres, profil_carateristiques, k):
    '''
    Renvoie la table des k plus proche voisins
    
    Entrée : Une table contenant des dictionnaires. Chaque dictionnaire correspond à un personnages 
    d’Harry Potter avec ses 4 caractéristiques et sa maison. 
    Et Une table contenant un/des dictionnaire(s) avec 4 clés qui sont des caractéristiques 
    (Courage, Ambition, Intelligence, Good) avec en valeur un entier de 1 à 10.
    
    Sortie : Une table avec le nombre de dictionnaire correspondant au nombre de k plus proche voisin, avec leurs caractéristiques,
    leur maison, et leur distance par rapport au profil recherché 
    '''
    # Pour chaque dictionnaire on créé une nouvelle clé distance pour pouvoir la trier et avoir les personnage les ples proche
    for perso in tab_caracteres:
        distance = 0
        somme_carré = 0
        # Theoreme de pythagore
        for caracteristique in profil_carateristiques:
            somme_carré += (int(perso[caracteristique]) - profil_carateristiques[caracteristique]) ** 2
        distance = sqrt(somme_carré)
        
        perso['Distance'] = distance
    
    
    tab_caracteres.sort(key= lambda x: x['Distance'])
    tab_k_plus_proche_voisin = tab_caracteres[:k]
    
    return tab_k_plus_proche_voisin


#persos_proche est obtenue apres avoir utlisier la fonction k_plus_proche_voisin
def maison_profil(persos_proches ):
    '''
    Renvoie une liste de tuple trier afin d'avoir la maison du profil

    Entrée : liste de dictionnaire des k plus proche voisin 
    Sortie : liste de tuple contenant la maision et le nombre de personnages des persos proches qui font partie
    de la maison
    '''
    dico_maison = {'Gryffindor' : 0, 'Ravenclaw' : 0, 'Slytherin' : 0, 'Hufflepuff' : 0}
    
    for perso in persos_proches:
        dico_maison[perso['House']] += 1
        
    list_maison = list(dico_maison.items())
    
    list_maison.sort(key=lambda x: x[1], reverse=True)

    return list_maison


def affichage (profil, caracteres, k) :
    '''
    Affiche dans le terminal les résultats mise en page 

    Entrées : une table contenant les caractéristiques d'un profil, une table des personnage les plus proche du
    profil et un entier k qui determine le nombre de personnage selectionné
    Sortie : Des chaines de caractères
    '''
    

    for persos in k_plus_proche_voisin(caracteres, profil, k):
        print(f" - \033[92m{persos['Name']}\033[0m de la maison \033[92m{persos['House']}\033[0m est à une distance de \033[92m{persos['Distance']}\033[0m")
    maison = maison_profil(k_plus_proche_voisin(caracteres, profil, k))
    print(f"\nLa maison du profil est donc \033[92m{maison[0][0]}\033[0m")



"""
PROGRAMME PRINCIPAL
"""



#ouvre le csv "Characters"
with open("Characters.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    characters_tab = [{key : value for key, value in element.items()} for element in reader]
    

#ouvre le csv "Caracteristiques_des_persos"
with open("Caracteristiques_des_persos.csv", mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';')
    caractéristique_tab = [{key : value for key, value in element.items()} for element in reader]



# On fait la fusion en rajoutant la maison de chaque personnage
for poudlard_character in caractéristique_tab:
    for character_HP in characters_tab:
        if poudlard_character['Name'] == character_HP['Name']:
            poudlard_character['House'] = character_HP['House']
            poudlard_characters.append(poudlard_character) 


k = int(input("Saisiser un entier pour k : "))
for profil in profils_tab:
    print(f"\n\n\n Les 5 personnages les plus proches du profil ayant pour caracteristique {profil} sont :\n")
    affichage (profil, poudlard_characters, k)

print("\n\n")

rep = input("Voulez-vous entrer les caractéristiques d'un personnage ? Si oui tapez 1 : ")
if rep == '1' :
    tab_perso_modifiable = {'Courage': 0,'Ambition': 0,'Intelligence': 0,'Good': 0}
    tab_perso_modifiable['Courage']  = int(input("Donnez une valeur de 1 à 10 pour la valeur de courage du personnage : ")) 
    tab_perso_modifiable['Ambition'] = int(input("Donnez une valeur de 1 à 10 pour la valeur d'ambition du personnage : "))
    tab_perso_modifiable['Intelligence'] = int(input("Donnez une valeur de 1 à 10 pour la valeur d'intelligence du personnage : "))
    tab_perso_modifiable['Good'] = int(input("Donnez une valeur de 1 à 10 pour la valeur de bonté du personnage : "))

    print(f"\nRésumé : {tab_perso_modifiable}\n")
    affichage(tab_perso_modifiable, poudlard_characters, k)