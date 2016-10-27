# author: Mohammad Kachuee

import os
import pdb
import pickle

from IPython import embed


class TreeNode:
    """
    This class implements each node of the tree using a linked list.
    Attributes:
        - node_id
        - node_content
        - node_tails
    """
    current_id = 0

    def __init__(self, node_content=None, node_heads=[], node_tails=[]):
        """
        TreeNode constructor.
        
        node_id:
            - a unique id for each node, it is implemented using a static counter in the class.
        node_content:
            - it is None by default which means that it is neither a root node nor a resource node, 
            so it can be interpereted as a prerequisite node.
        node_tails:
            - stores the list of each node's tail nodes in a linked-list like fashion. 
            empty tail means termination of the tree.
        """
        TreeNode.current_id += 1
        self.__node_id = TreeNode.current_id
        self.__node_content = node_content
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
        """
        get uinique node id.
        """
        return self.__node_id

    def get_content(self):
        """
        get node content.
        """
        return self.__node_content

    def get_tails(self):
        """
        get tail nodes.
        """
        return self.__node_tails

    def set_content(self, content):
        """
        set node contents.
        """
        self.__node_content = content

    def add_tail(self, node=None):
        """
        add a node to tail. if the node is not specified a node will be created and added.
        """
        if node is None:
            node = TreeNode()
        self.__node_tails.append(node)
        node.__node_tails = []
        return node

    def remove_tail(self, node):
        """
        remove a node from tail. if it is found and removed returens True, else returns False.
        """
        if node in self.__node_tails:
            __node_tails.remove(node)
            return True
        else:
            return False

def load_tree(path):
    """
    Loads all files associated with a tree, including tree object, image, and discription.
    Input is a path which indicates to the storage folder.
    Returns a dictionary if read was successful, else returns None.
    """
    tree_data = {'tree':None, 'image':None, 'description':None}
    
    try:
        with open(path+'/'+'tree.pkl', 'rb') as f:
            tree_data['tree'] = pickle.load(f)

        with open(path+'/'+'tree.txt', 'rb') as f:
            tree_data['description'] = f.read()
    except:
        return None
    try:
        with open(path+'/'+'tree.png', 'rb') as f:
            tree_data['image'] = None # TODO: add image loading
    except:
        pass

    return tree_data

def save_data(path, tree, description, image):
    pass # TODO: add tree saving
