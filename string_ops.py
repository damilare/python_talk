import unittest
from string_utils import upper, lower

class TestStringMethods(unittest.TestCase):

   def test_upper(self):
       self.assertEqual(upper('foo'), 'FOO')

   def test_lower(self):
       self.assertEqual(lower('FOO'), 'foo')

   def test_split(self):
       with self.assertRaises(TypeError):
           lower(1)

if __name__ == '__main__':
   unittest.main()
