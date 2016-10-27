# author: Mohammad Kachuee

import pickle


class TreeNode:
    """
    This class implements each node of the tree using a linked list.
    Attributes:
        - node_id
        - node_type
        - node_content
        - node_heads
        - node_tails
    """
    current_id = 0

    def __init__(self, node_type=None, node_content=None, node_heads=None, node_tails=None):
        current_id += 1
        self.__node_id = current_id
        self.__node_content = node_content
        self.__node_heads = node_heads
        self.__node_tails = node_tails

    def save(self, filename):
        """
        saves the TreeNode object as a pkl file.
        """
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    def load(self, filename):
        """
        loads the TreeNode object as a pkl file.
        """
        with open(filename, 'wb') as f:
            self = pickle.load(f)

    def get_id(self):
        return self.__node_id

    def get_content(self):
        return self.__node_content

    def get_heads(self):
        return self.__node_heads

    def get_tails(self):
        return self.__node_tails
 
