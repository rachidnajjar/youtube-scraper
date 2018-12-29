'''
Created on 29 déc. 2018

@author: rachid
'''
import unittest
import classLibrary
import datetime


class PersonneTest(unittest.TestCase):


    def testObtenirAge(self):
        nom = "NAJJAR"
        prenom = "Amine"
        dateNaissance = datetime.date(2008, 6, 14)
        expected = 10
        p = classLibrary.Personne(nom, prenom, dateNaissance)
        actual = p.ObtenirAge()
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testObtenirAge']
    unittest.main()