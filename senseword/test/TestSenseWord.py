'''
Created on Nov 27, 2021

@author: pappa
'''
import unittest
from senseword.senseword import SenseWord

class TestSenseWord(unittest.TestCase):
    
    def testSenseWord(self):
        sense_word=SenseWord()
        result=sense_word.sense("aaa","aaa")
        self.assertEqual(result,True,"Oops")
