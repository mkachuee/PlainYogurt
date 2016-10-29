# author: Mohammad Kachuee

import os
import pdb
import pickle
import PIL

from IPython import embed


class TreeNode:
    """
    This class implements each node of the tree using a linked list.
    Attributes:
        - node_id
        - node_content
        - node_tails
    """
    current_id = -1

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
        add a node to tail. if the node is not specified a node will be 
        created and added.
        """
        if node is None:
            node = TreeNode()
        self.__node_tails.append(node)
        node.__node_tails = []
        return node

    def walk(self, path=[]):
        """
        this method walks through the tree and returns all nodes in 
        each path to the leafs.
        """
        if self.__node_tails == []:
            path.append(self.__node_id)
            return path
        else:
            paths = []
            for branch in self.__node_tails:
                branch_path = branch.walk(path+[self.__node_id])
                if type(branch_path[0]) is list:
                    paths += (branch.walk(path+[self.__node_id]))
                else:
                    paths.append(branch.walk(path+[self.__node_id]))
            return paths
    
    def traverse(self):
        """
        this function visits every node in the tree, and returns a dictionary
        of {id:content}.
        """
        if self.__node_tails == []:
            return {self.__node_id: self.__node_content}
        else:
            contents = {self.__node_id: self.__node_content}
            for branch in self.__node_tails:
                contents.update(branch.traverse())
            return contents

    def to_list(self):
        """
        Describes a tree as a list of paths and a list of contents.
        """ 
        paths = self.walk(path=[])
        contents = self.traverse()
        return {'paths':paths, 'contents':contents}

    def remove_tail(self, node):
        """
        remove a node from tail. if it is found and removed returens True, 
        else returns False.
        """
        if node in self.__node_tails:
            __node_tails.remove(node)
            return True
        else:
            return False

def load_data(path):
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
            tree_data['image'] = PIL.Image.open(f)
    except:
        pass

    return tree_data

def save_data(path, tree_data):
    """
    tree_data  is  {'tree':, 'image':, 'description':}
    """
    if not os.path.isdir(path):
        os.mkdir(path, exists_ok=True)
    try:
        with open(path+'/'+'tree.pkl', 'wb') as f:
            pickle.dump(tree_data['tree'], f)

        with open(path+'/'+'tree.txt', 'w') as f:
            f.write(tree_data['description'])
    except:
        return False
    try:
        with open(path+'/'+'tree.png', 'wb') as f:
            tree_data['image'].save(f)
    except:
        pass

    return True
