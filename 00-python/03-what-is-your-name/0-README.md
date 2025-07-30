📝 Exercice 02 – What is your name
🎯 Objectif

Dans cet exercice, tu vas écrire une fonction pour construire le nom complet d’un utilisateur puis créer une petite interface qui lui demande ses informations et les affiche correctement.

🛠️ Étape 1 – Compléter la fonction
📂 Fichier : what_is_your_name.py

def compute_name(first_name, middle_name, last_name):
    # TODO : Retourner "first_name middle_name last_name"
    pass
👉 Consignes :

La fonction doit concaténer les 3 paramètres avec un espace entre chaque.

Si middle_name est vide, il ne doit pas y avoir d’espace en trop.

Exemple :

compute_name("Ada", "", "Lovelace")  # ➜ "Ada Lovelace"
compute_name("Boris", "Alexandre", "Papillard")  # ➜ "Boris Alexandre Papillard"

🖥️ Étape 2 – Interface utilisateur
📂 Fichier : interface.py

Demander à l’utilisateur :

son prénom

son deuxième prénom (laisser vide si aucun)

son nom de famille

Utiliser la fonction compute_name() pour générer le nom complet.

Afficher le résultat.

Exemple d’exécution :


Quel est ton prénom ? Ada
As-tu un deuxième prénom ?
Quel est ton nom de famille ? Lovelace

Ton nom complet est : Ada Lovelace

