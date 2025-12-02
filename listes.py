# -*- coding: utf-8 -*-
from locale import currency


class Liste:
    """ The class Liste allows to represent a list from chained elements of type Cell. Each element of the 
    list contains a value and a pointer towards the next element. """
    
    def __init__(self):
        """Creates an instance of class Liste
        input   -- self : instance of class Liste
                    set the first element to None, and the size of the list to 0
        """
        self.mfirst = None
        self.size = 0

    def is_empty_list(self):
        """ Returns True if and only if Liste self is empty
        input   -- self : instance of class Liste
        output  -- v : bool
        """
        v = (self.mfirst == None)
        return v
    
    def __str__(self):
        """ Returns a string representing Liste self
        input   -- self : instance of class Liste
        output  -- string
        """
        if self.is_empty_list():
            return "[]"
        else:
            sortie = "["
            current = self.mfirst
            while current.next != None:
                sortie += str(current.data)
                sortie += ", "
                current = current.next
            sortie += str(current.data) # Le dernier cas avec que current soit None
            return sortie + "]"
    
    def length(self):
        """ Returns the lenght of the list
        input   -- self : instance of class Liste
        output  -- n : int
        """
        return self.size
    
    def head(self):
        """ Returns the first element of the list (of type Cell)
        input   -- self : instance of class Liste
                pre-cond: self n'est pas vide
        output  -- p : element of type Cell
        """
        if self.mfirst == None:
            print("empty list")
        else:
            p = self.mfirst
            return p
        
    def first_value(self):
        """ Returns the value of the first element of the list of type object
        input   -- self : instance of class Liste
                pre-cond: self is not empty
        output  -- v : value of type object
        """
        if self.mfirst == None:
            print("liste vide")
        else:
            v = self.mfirst.data
            return v
        
    def insert_first(self, v):
        """ Inserts the value v at the head of the list
        input   -- self : instance of class Liste
                -- v : value of type object to insert at the first position
        output  -- self in which the element of value v has been inserted at the head of the list
                    the size of the list is updated
        """
        m = Cell()
        m.data=v
        if self.mfirst == None:
            m.next = None
        else:
            m.next=self.mfirst
        self.mfirst = m
        self.size += 1
        
    def insert_at(self,v,i):
        """ Returns the list in which the element of value v has been inserted at index i
        input   -- self : instance of class Liste
                -- v : value of type object to insert
                -- i : int index at which the element of value v is inserted
                    exception when the index i is too small or too big
        output  -- self in which the element of value v has been inserted at index i of the list
                    the size of the list is updated
        """
        assert 0 <= i <= self.size, "Error indice."
        if i == 0: # Dans le cas où la liste est vide, j'insère la cellule en tête
            self.insert_first(v)
        else: # Sinon, j'itère sur la liste chaînée
            insert_cell = Cell() # la cellule a insérer
            insert_cell.data = v
            current = self.mfirst
            for j in range(i-1):
                current = current.next
            insert_cell.next = current.next
            current.next = insert_cell
            self.size += 1
            return self

    def insert_last(self,v):  
        """ Inserts the value v at the end of the list
        input   -- self : instance of class Liste
                -- v : value of type object to insert at the last position
        output  -- self in which the element of value v has been inserted at the end of the list
                    the size of the list is updated 
        """
        i = self.length()
        if i == 0:
            self.insert_first(v)
        else:
            self.insert_at(v,i)
        
    def delete_value(self,v):
        """ Returns the list in which the element of value v i has been deleted
        input   -- self : instance of class Liste
                -- v : value of type object
        output  -- self in which the element of value v has been deleted
                    the size of the list is updated 
        """
        if self.size < 0:
            print("Erreur de taille, size est négatif.")
        if self.size == 0:
            print("Erreur, liste vide.")
        if self.mfirst.data == v: # si la première cellule vaut la valeur
                self.mfirst = self.mfirst.next
        else:
            prev = self.mfirst # le début de ma liste
            current = prev.next # la deuxième cellule
            while current.next != None:
                if current.data == v:
                    prev.next = current.next # On saute la cellule current <=> supprimer current
                prev = prev.next
                current = current.next
            if current.data == v: # On gère le cas où la valeur est a supprimer est en dernière position
                prev.next = None
        self.size -= 1 # On met à jour la taille de la liste chainée

    def get_at(self,i):
        """ Returns the element of the Liste self at index i
        input   -- self
                -- i : int (index of the searched element) 
        output  -- element of type Cell 
        """
        current = self.mfirst
        j = 0
        while current.next != None and j<i:
            current = current.next
            j+=1
        print(current)
        return current
                
    def get_value(self,i):
        """ Returns the value of the element of the liste at index i
        input   -- self
                -- i : int (index of the searched element) 
        output  -- v : object 
        """
        assert 0 <= i < self.size, "indice out of range"
        current = self.mfirst
        j = 0
        while current.next != None and j<i:
            current = current.next
            j += 1
            print(f'la valeur de j : {j}')
        
        return current.data       
    
    def map(self,f):
        """ Applies function f to each value of Liste self
        input   -- self : instance of class Liste
                -- f : function
        output  -- lmap: new Liste in which each value has been modified by function f
                    self is not modified
        """  
        lmap = Liste() # Une nouvelle liste vierge
        current = self.mfirst
        while current is not None:
            lmap.insert_last(f(current.data))
            print(current)
            current = current.next
        lmap.size = self.size
        return lmap
    
    def count(self, v):
        """ Counts the number of occurrences of v in Liste self
        input   -- self : instance of class Liste
                -- v : object
        output  -- int : number of times v occurs in Liste self
        """
        number_of_v = 0 # Le nombre de v dans la liste chainée
        current = self.mfirst
        while current is not None:
            if current.data == v:
                number_of_v += 1
            current = current.next
        return number_of_v
        
    def filter(self, f):
        """ Returns the list of the elements x of Liste self that verify f(x) = True
        input   -- self : instance of class Liste
                -- f : function
                pre-cond: verify that f returns True or False
        output  -- lfilter: new Liste of elements whose values verify f(x) = True
        """
        lfilter = Liste() # Une nouvelle instance de Liste
        current = self.mfirst
        while current is not None:
            result = f(current.data)
            assert type(result) == bool, "La fonction f ne renvoie pas de booléen."
            if result:
                lfilter.insert_last(current.data)
            current = current.next
        lfilter.size = self.size # mise à jour de la taille
        return lfilter
    
    def reduce(self, f,x):
        """ Returns the value obtained by applying the function f(x,y) to each value y of Liste self
        input   -- self : instance of class Liste
                -- f : function
                -- x : initial value of type object
        output  -- final value of type object
        """
        lreduce = Liste()
        current = self.mfirst
        while current is not None:
            lreduce.insert_last(f(x,current.data))
            current = current.next
        lreduce.size = self.size # mise à jour de la taille
        return lreduce
                    
class Cell():
    """ The class Cell represents an element of the list. It contains 2 attributes: a data of type object and a link to the next element
    """
 
    def __init__(self):
        """ Creates an instance of class Cell
        input   -- self : instance of class Cell
        """
        self.data = object
        self.next = None
        
    def __str__(self):
        """ Returns a string representing the self Cell
        input   -- self : instance of class Cell
        output  -- string, representation of the self cell
        """
        result = str(self.data) + ', next:'
        if self.next == None:
            result += 'None'
        else:
            result += str(self.next.data)
        return '{ ' + result + ' }' 
        
def incr(n):
    """ Returns an increments of n by 1
    input   -- n : number, the value to increment
    output  -- number, n+1
    """
    return n+1

def carre(n):
    """ Returns the squared value of n
    input   -- n : number
    output  -- number, n^2
    """
    return n * n

def test_negative(n):
    """ Tests if n is negative
    input   -- n : number(int or float)
    output  -- bool : True if n is negative, False otherwise"""
    return n < 0

def f(x,y):
    """ Adds y to x and returns the result
    input   -- x : Any
               y : Any
    output  -- Any, x + y
    """
    return x + y
        
if __name__ == "__main__":
    print("Hello Liste !!!")
