'''
Created on 29 déc. 2018

@author: rachid
'''
import sys
from classLibrary import Personne
from datetime import date

def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]
        
    print("This is the main routine.")
    print("It should do something interesting.")
    # Do argument parsing here (eg. with argparse) and anything else
    # you want your project to do.

    
    p = Personne("NAJJAR", "Rachid", date(1974, 10, 24))
    print(p.Nom)
    print(p.Prenom)
    print(p.DateNaissance)
    print(p.ObtenirAge())


    

if __name__ == '__main__':
    main()