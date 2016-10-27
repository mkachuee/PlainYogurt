# author: Mohammad Kachuee

import pickle


class TreeNode:
    """
    This class implements each node of the tree using a linked list.
    Attributes:
        - node_id
        - node_type
        - node_content
        - node_outputs
        - node_inputs
    """
    current_id = 0

    def __init__(self, node_type, node_content, node_outputs, node_inputs):
        current_id += 1
        self.node_id = current_id
        self.node_content = node_content
        self.node_outputs = node_outputs
        self.node_inputs = node_inputs

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



        
