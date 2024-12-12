# -*- coding: utf-8 -*-

import itertools
import json
import os
import sys

def lire_dictionnaire(fichier_chemin):
    if not os.path.isfile(fichier_chemin):
        raise FileNotFoundError(f"Le fichier {fichier_chemin} n'existe pas.")
    
    with open(fichier_chemin, 'r', encoding='utf-8') as fichier:
        mots = [ligne.strip().lower() for ligne in fichier if ligne.strip()]
    return mots


def generer_permutations_uniques(mot):
    return sorted(set(''.join(p) for p in itertools.permutations(mot)))

def creer_fichier_json(mot, permutations, dossier_sortie):

    nom_fichier = mot + '.json'
    chemin_fichier = os.path.join(dossier_sortie, nom_fichier)
    
    data = {
        "permutations": permutations
    }
    
    with open(chemin_fichier, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def creer_combinations_separates(mots, dossier_sortie, max_longueur, afficher_interval):

    lst_file = os.listdir("G:/T3/")

    if not os.path.exists(dossier_sortie):
        os.makedirs(dossier_sortie)
        print(f"Répertoire de sortie créé : {dossier_sortie}")
    
    total_mots = len(mots)
    mots_traite = 0
    mots_inclus = 0
    mots_exclus = 0

    for mot in mots:
        mots_traite += 1
        if mot:
            if len(mot) <= max_longueur:
                if mot+".json" not in lst_file:
                    permutations = generer_permutations_uniques(mot)
                    creer_fichier_json(mot, permutations, dossier_sortie)
                    mots_inclus += 1
                else:
                   mots_exclus += 1 
            else:
                mots_exclus += 1
        
        if mots_traite % afficher_interval == 0:
            print(f"{mots_traite}/{total_mots} mots traités...")

    print(f"\nTraitement terminé. {mots_inclus} mots inclus et {mots_exclus} mots exclus.")
    print(f"Les fichiers JSON ont été sauvegardés dans le répertoire '{dossier_sortie}'.")

def main():
    fichier_entree = 'd_word_lst.txt'
    dossier_sortie = 'G:/T3/'
    MAX_LONGUEUR = 10
    AFFICHER_INTERVAL = 5

    try:
        mots = lire_dictionnaire(fichier_entree)
        print(f"{len(mots)} mots ont été lus depuis '{fichier_entree}'.")
        
        creer_combinations_separates(mots, dossier_sortie, max_longueur=MAX_LONGUEUR, afficher_interval=AFFICHER_INTERVAL)
        
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        sys.exit(1)

# if __name__ == "__main__":
#     main()




