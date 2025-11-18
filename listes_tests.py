# -*- coding: utf-8 -*-

import listes

# %% Test de la fonction __str__ L = [3,2,1]

L=listes.Liste()
L.insert_first(1)
L.insert_first(2)
L.insert_first(3)
print("L : ", L)

# %% Test de la méthode length(), L = [3,2,1]
L=listes.Liste()
L.insert_first(1)
L.insert_first(2)
L.insert_first(3)
print("L : ", L)
print("L.length() :", L.length())


# %% Test de la méthode get_at(), L = [3,2,1]
L=listes.Liste()
L.insert_first(1)
L.insert_first(2)
L.insert_first(3)
print("L.get_at(0) :", L.get_at(0))
print("L.get_at(2) :", L.get_at(2))

# %% Test de la méthode get_value(), L = [1,2,3]
L=listes.Liste()
L.insert_first(1)
L.insert_first(2)
L.insert_first(3)
print("L.get_value(0) :", L.get_value(0))
print("L.get_value(3) :", L.get_value(2))

# %% Test de la méthode insert_at 
L=listes.Liste()
L.insert_at(1,0)
L.insert_at(2,1)
L.insert_at(3,2)
L.insert_at(4,3)
L.insert_at(5,4)
print("L :", L)
exit()
# %% Test de la méthode delete_value
L=listes.Liste()
L.insert_last(1)
L.insert_last(2)
L.insert_last(3)
L.insert_last(4)
L.insert_last(5)
print(L)

L.delete_value(3)
print("L after delete_value 3 :", L)
L.delete_value(5)
L.delete_value(2)
L.delete_value(1)
L.delete_value(4)
print("L after delete_value 5,2,1,4 :", L)
# L.delete_value(4)

# %% Test de la méthode map
L=listes.Liste()
L.insert_first(1)
L.insert_last(2)
L.insert_last(3)
print("L :", L)
    
L1 = L.map(listes.incr)
print("L1 :", L1)

L2 = L.map(listes.carre)    
print("L2 :", L2)

# %% Test de la méthode count
L=listes.Liste()
L.insert_first(1)
L.insert_last(2)
L.insert_last(2)
L.insert_last(5)
L.insert_last(1)
L.insert_last(2)
print("L :", L)
print("L.count(2) :", L.count(2))

# %% Test de la méthode filter
L=listes.Liste()   
L.insert_at(1,0)
L.insert_at(-2,1)
L.insert_at(3,2)
L.insert_at(-4,3)
L.insert_at(5,4)
print("L :", L)
L3 = L.filter(listes.test_negative)
print("L3 :", L3)

# %% Test de la méthode reduce
L=listes.Liste()
L.insert_first(1)
L.insert_first(2)
L.insert_first(3)
print("L :", L)
x = L.reduce(listes.f,1)
print("x :", x)
