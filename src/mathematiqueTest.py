'''
Created on 29 déc. 2018

@author: rachid
'''
import unittest
from mathematique import Mathematique


class mathematiqueTest(unittest.TestCase):


    def testAdditionner(self):
        a = 3
        b = 5
        expected = 8
        actual = Mathematique().Additionner(a, b)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAdditionner']
    unittest.main()