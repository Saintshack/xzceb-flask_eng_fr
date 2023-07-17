import unittest

from translator import englishToFrench, frenchToEnglish


class Testtranslation(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("hello"), "bonjour")  # test when hello is given as input the output is bonjour.
        self.assertNotEqual(englishToFrench("Hello"), "bonjour")
    def test2(self):
        self.assertEqual(frenchToEnglish("bonjour"), "hello") # test when bonjour is given as input the output is hello.
        self.assertNotEqual(frenchToEnglish("onjour"), "hello")

if __name__ == '__Main__':
    unittest.main()