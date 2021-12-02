import unittest
import os

class Testmain(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_main_noargs(self):
        result = os.system("python3 ../main.py")
        self.assertEqual(result, 256) # ¤?*256
        
    def test_main_help(self):
        result = os.system("python3 ../main.py -h")
        self.assertEqual(result, 0)    

    def test_main_match(self):
        result = os.system("python3 ../main.py 'aaa' 'aaa'")
        self.assertEqual(result, 0)
        
    def test_main_mismatch(self):
        result = os.system("python3 ../main.py 'aaa' 'bbb'")
        self.assertEqual(result, 256)
        
    def test_main_toomanyargs(self):
        result = os.system("python3 ../main.py -h 'aaa' 'bbb'")
        self.assertEqual(result, 256)       

    def test_main_badargs(self):
        result = os.system("python3 ../main.py -x")
        self.assertEqual(result, 512)       

    def tearDown(self):
        pass