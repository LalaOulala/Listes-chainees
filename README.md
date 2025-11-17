# TP5 – Listes chaînées en Python

Petit TP d’initiation aux structures de données, dont l’objectif est d’implémenter une **liste chaînée** simple en Python et quelques opérations de base dessus.

## Contenu du projet

- `listes.py`  
  - classe `Cell` : représente un maillon (valeur + pointeur vers le suivant) ;  
  - classe `Liste` : implémente une liste chaînée simple avec, entre autres :
    - `is_empty_list`, `length`, `__str__` ;
    - `insert_first`, `insert_last`, `insert_at` (insertion en tête / fin / position i) ;
    - `delete_value` (suppression d’une valeur) ;
    - `get_at`, `get_value` (accès à un maillon / à sa valeur) ;
    - `map`, `count`, `filter`, `reduce` (opérations de type fonctionnel sur la liste).
  - quelques fonctions utilitaires utilisées dans les tests (par ex. `incr`, `carre`, `test_negative`, `f`).

- `listes_tests.py`  
  Script simple qui crée des listes de test et affiche le résultat de chaque méthode pour vérifier le bon fonctionnement de l’implémentation.

- `TP5-listes (1).pdf`  
  Énoncé du TP (description détaillée des fonctions à coder et des questions théoriques).

## Objectifs pédagogiques

- Comprendre la structure d’une **liste chaînée** (maillons + liens).
- Savoir implémenter les opérations classiques (insertion, suppression, parcours).
- Manipuler des listes avec un style plus **fonctionnel** : `map`, `filter`, `reduce`.
- Travailler proprement dans un module Python et tester son code.

## Utilisation

Depuis ce dossier, lancer les tests “maison” avec :

```bash
python3 listes_tests.py
```

Le script affiche dans le terminal les différentes listes et valeurs renvoyées par les méthodes de `Liste`, ce qui permet de vérifier au fur et à mesure que chaque fonction est correctement codée.

