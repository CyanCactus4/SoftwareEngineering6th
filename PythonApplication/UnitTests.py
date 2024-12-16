from PythonApplication import ferm_theorem
import unittest

#Тесты
class Test(unittest.TestCase):
    def test1(self):
        self.assertTrue(ferm_theorem(3, 4, 5, 3))
        self.assertTrue(ferm_theorem(3, 4, 5, 4))
    def test2(self):
        self.assertTrue(ferm_theorem(6, 8, 10, 3))
        self.assertTrue(ferm_theorem(6, 8, 10, 4))
    def test3(self):
        self.assertTrue(ferm_theorem(12, 16, 20, 3))
        self.assertTrue(ferm_theorem(12, 16, 20, 4))
        

if __name__ == "__main__":
    unittest.main()
    
# Верна ли теорема Ферма при a = 3, b = 4, c = 5 для
# n = 3: True
# n = 4: True
# n = 5: True
# n = 6: True
# n = 7: True
# n = 8: True
# n = 9: True
# n = 10: True
# n = 11: True
# n = 12: True

# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s