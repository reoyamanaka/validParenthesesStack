import unittest
import validParenthesesStack as f

class TestValidParenthesesStack(unittest.TestCase):
    def test_validParentheses(self):
        self.assertTrue(f.validP("({a+b})"), "Test value is True.")
        self.assertFalse(f.validP("))((a+b}{"), "Test value is False.")
        self.assertTrue(f.validP("((a+b))"), "Test value is True.")
        self.assertFalse(f.validP("))"), "Test value is False.")
        self.assertTrue(f.validP("[a+b]*(x+2y)*{gg+kk}"), "Test value is True.")
    
if __name__ == "__main__":
    unittest.main()
