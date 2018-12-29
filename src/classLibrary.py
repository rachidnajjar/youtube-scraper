'''
Created on 29 déc. 2018

@author: rachid
'''
from datetime import date


class Personne(object):
    '''
    classdocs
    '''


    def __init__(self, nom, prenom, dateNaissance):
        '''
        Constructor
        '''
        self.Nom = nom
        self.Prenom = prenom
        self.DateNaissance = dateNaissance
        
    def ObtenirAge(self):
        resultat = date.today().year - self.DateNaissance.year
        return resultat
    
    