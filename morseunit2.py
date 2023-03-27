import morse2 as morse
import unittest

class TestMorse(unittest.TestCase):
    def test_morseencode(self):
        self.assertEqual( morse.encode('morse'), '-- --- .-. ... .')
        self.assertEqual( morse.encode('binary'), '-... .. -. .- .-. -.--')
        self.assertEqual( morse.encode('full'), '..-. ..- .-.. .-..')
        # self.assertEqual( morse.encode('encoder'), '. -. -.-. --- -..') #fail
        self.assertEqual( morse.encode('us'), '..- ...')
        self.assertEqual(morse.encode('Hello;'),'.... . .-.. .-.. --- -.-.-.')
    
    def test_decodemorse(self):
        self.assertEqual( morse.decode("-- --- .-. ... ."), 'morse')
        self.assertEqual( morse.decode(". -. -.-. --- -.. . .-."), 'encoder')
        self.assertEqual( morse.decode("-- ---"), 'mo')
        self.assertEqual( morse.decode("..-.."), 'g') # fail
        self.assertEqual( morse.decode("- . ... -"), 'test')

    def test_emptytree(self):
        tree = morse.BTree()

        self.assertIsNone(tree.root) # assert Tree Empty -> None

    def test_notemptytree(self):
        tree = morse.BTree()
        tree.insert("H", ".")
        tree.insert(")", "-")

        self.assertIsNotNone(tree) # assert Tree Not Empty -> None

    def test_insert(self):
        mbt = morse.BTree()
        mbt.insert("B", ".")
        mbt.insert("AA","-")
        mbt.insert("MORSE", "..")

        self.assertTrue(mbt.find("B")) # assert True
        self.assertTrue(mbt.find("AA")) # assert True
        self.assertTrue(mbt.find("MORSE")) # assert True

    def test_delete(self):
        mbt = morse.BTree()
        mbt.insert("G", "-")
        mbt.insert("N", ".")

        mbt.delete("G") # delete G node value
        mbt.insert("HAD", "..") #
        mbt.delete("HAD")
        self.assertFalse(mbt.find("G")) # assert False
        self.assertFalse(mbt.find("HAD")) # assert False

    def test_find(self):
        # search the Morse Binary Tree defined in the module

        self.assertTrue(morse.find("G")) # assertTrue
        self.assertTrue(morse.find(")")) # assert True

        self.assertTrue(morse.find("\\")) # assert failed

if __name__ == '__main__':
    unittest.main()