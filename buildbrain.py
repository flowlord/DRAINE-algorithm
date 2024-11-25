import itertools
import json
import os
import string
import sys

def lire_dictionnaire(fichier_chemin):
    """
    Lit le fichier contenant le dictionnaire de mots.
    Chaque mot doit être sur une ligne séparée.
    """
    if not os.path.isfile(fichier_chemin):
        raise FileNotFoundError(f"Le fichier {fichier_chemin} n'existe pas.")
    
    with open(fichier_chemin, 'r', encoding='utf-8') as fichier:
        # Lire les mots, enlever les espaces et convertir en minuscules
        mots = [ligne.strip().lower() for ligne in fichier if ligne.strip()]
    return mots

def generer_permutations_uniques(mot):
    """
    Génère toutes les permutations uniques des lettres d'un mot.
    """
    # Utiliser set pour éliminer les doublons si le mot contient des lettres répétées
    return sorted(set(''.join(p) for p in itertools.permutations(mot)))

def nettoyer_nom_fichier(mot):
    """
    Nettoie le mot pour l'utiliser comme nom de fichier.
    Remplace les caractères non alphanumériques par des underscores.
    """
    valid_chars = f"-_.() {string.ascii_letters}{string.digits}"
    cleaned = ''.join(c if c in valid_chars else '_' for c in mot)
    return cleaned

def creer_fichier_json(mot, permutations, dossier_sortie):
    """
    Crée un fichier JSON pour un mot donné avec ses permutations.
    
    Args:
        mot (str): Le mot original.
        permutations (list): Liste des permutations uniques.
        dossier_sortie (str): Répertoire où sauvegarder les fichiers JSON.
    """
    # Nettoyer le nom du fichier
    nom_fichier = mot + '.json'
    chemin_fichier = os.path.join(dossier_sortie, nom_fichier)
    
    # Préparer le contenu JSON
    data = {
        "mot": mot,
        "permutations": permutations
    }
    
    # Écrire dans le fichier JSON
    with open(chemin_fichier, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def creer_combinations_separates(mots, dossier_sortie, max_longueur=8, afficher_interval=100):
    """
    Crée un fichier JSON distinct pour chaque mot avec ses permutations uniques,
    en limitant la longueur des mots pour des raisons de performance.
    
    Args:
        mots (list): Liste des mots à traiter.
        dossier_sortie (str): Répertoire où sauvegarder les fichiers JSON.
        max_longueur (int): Longueur maximale des mots à traiter.
        afficher_interval (int): Intervalle pour afficher le nombre de mots traités.
    """

    lst_file = os.listdir("G:/T2/")

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
        
        # Afficher le nombre de mots traités à intervalle régulier
        if mots_traite % afficher_interval == 0:
            print(f"{mots_traite}/{total_mots} mots traités...")

    print(f"\nTraitement terminé. {mots_inclus} mots inclus et {mots_exclus} mots exclus.")
    print(f"Les fichiers JSON ont été sauvegardés dans le répertoire '{dossier_sortie}'.")

def main():
    fichier_entree = 'world_lst_fr.txt'  # Remplacez par le chemin de votre fichier d'entrée
    dossier_sortie = 'G:/T2/'  # Nom du répertoire de sortie
    MAX_LONGUEUR = 10  # Définir une longueur maximale pour éviter les permutations trop grandes
    AFFICHER_INTERVAL = 1000  # Intervalle pour afficher le nombre de mots traités

    try:
        mots = lire_dictionnaire(fichier_entree)
        print(f"{len(mots)} mots ont été lus depuis '{fichier_entree}'.")
        
        creer_combinations_separates(mots, dossier_sortie, max_longueur=MAX_LONGUEUR, afficher_interval=AFFICHER_INTERVAL)
        
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        sys.exit(1)

# if __name__ == "__main__":
#         main()
