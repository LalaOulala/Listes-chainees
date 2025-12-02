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

## Principes d’implémentation (fiche de révision)

### Parcours d’une liste chaînée
- On part toujours de `current = self.mfirst`.
- On utilise `while current is not None:` pour avancer sans risque de déréférencer `None`.
- `for range(self.size)` est possible mais moins souple : il force à gérer les accès aux pointeurs et ne protège pas naturellement des tailles incohérentes.

### Insertion
- **En tête** (`insert_first`) : créer une nouvelle `Cell`, pointer son `next` vers l’ancienne tête, puis déplacer `mfirst` sur elle, incrémenter `size`.
- **À un indice** (`insert_at`) : vérifier l’indice (`assert 0 <= i <= size`), cas `i == 0` délégué à `insert_first`, sinon avancer `i-1` fois puis insérer en rechaînant `next`.
- **En fin** (`insert_last`) : se repose sur `insert_at` avec l’indice `length()` pour éviter de réécrire la logique.

### Suppression (`delete_value`)
- Deux pointeurs : `prev` (maillon précédent) et `current` (maillon candidat à supprimer).
- Cas tête : si `mfirst.data == v`, déplacer `mfirst` sur `mfirst.next`, décrémenter `size`.
- Sinon, avancer jusqu’à trouver `v`. Quand trouvé, “sauter” le maillon : `prev.next = current.next`. Le maillon n’est plus référencé, donc “déconnecté”.
- La taille est décrémentée uniquement si une suppression a eu lieu.

### Accès par indice
- `get_at`/`get_value` : vérifier l’indice (`assert 0 <= i < size`), partir de `mfirst`, avancer `i` fois avec un `while`, renvoyer la cellule ou sa donnée.
- Cette approche protège des indices hors bornes et évite les `NoneType` inattendus.

### Opérations fonctionnelles
- `map` : parcourt avec `while`, applique `f` à chaque valeur et insère dans une nouvelle liste via `insert_last`.
- `filter` : pour chaque élément, évalue `result = f(data)`, vérifie que le retour est bien un booléen (`assert type(result) == bool`), puis conserve l’élément si `result` est vrai.
- `count` : parcours simple, incrémente un compteur quand `data == v`.
- `reduce` (à compléter dans le TP) : applique une fonction binaire cumulée sur tous les éléments en partant d’une valeur initiale.

### Pourquoi `while current is not None` ?
- On arrête naturellement au bon moment (pointeur nul) sans dépendre d’une taille potentiellement fausse.
- On peut insérer/supprimer pendant le parcours si besoin, car on suit les liens réels plutôt qu’un indice calculé.

## Utilisation

Depuis ce dossier, lancer les tests “maison” avec :

```bash
python3 listes_tests.py
```

Le script affiche dans le terminal les différentes listes et valeurs renvoyées par les méthodes de `Liste`, ce qui permet de vérifier au fur et à mesure que chaque fonction est correctement codée.
