"""
unittest for NodeTree class.
"""
import os
import unittest

import tree

class NodeTreeTest(unittest.TestCase):
    """
    Basic unittests for the NodeTree class.
    """
    def setUp(self):
        """
        Initialize test.
        """
        print('Setting Up NodeTree for unittest ...')
        self.__test_node = tree.TreeNode()
        self.__test_content = 'hello is salam'
        self.__test_file = 'test_tree_tmp.pkl'

    def tearDown(self):
        """
        Finalize test.
        """
        print('Test finished, cleaning...')
        try:
            os.remove(self.__test_file)
        except:
            pass

    def test_init(self):
        """
        Test the constructor method.
        """
        self.assertFalse(self.__test_node is None)
        self.assertTrue(self.__test_node.get_content() is None)
        self.assertListEqual(self.__test_node.get_tails(), [])
    
    def test_content(self):
        """
        Test content set and get methods.
        """
        self.__test_node.set_content(self.__test_content)
        self.assertEqual(self.__test_node.get_content(), 
                self.__test_content)
        self.__test_node.set_content(None)
    
    def test_addremove(self):
        """
        test tail add and remove methods.
        """
        tail_new = tree.TreeNode()
        self.__test_node.add_tail(tail_new)
        self.assertEqual(tail_new, self.__test_node.get_tails()[0])
        self.__test_node.remove_tail(tail_new)
        self.assertListEqual(self.__test_node.get_tails(), [])

    def test_saveload(self):
        """
        Test save and load methods.
        """
        self.__test_node.save(self.__test_file)
        loaded_node = self.__test_node.load(self.__test_file)
        self.assertEqual(type(loaded_node), type(self.__test_node))
        
if __name__ == "__main__":
    unittest.main()

