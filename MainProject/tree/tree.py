# author: Mohammad Kachuee

import os
import pdb
import pickle

import xml.etree.ElementTree as xmlet
from html.parser import HTMLParser
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
    current_id = -1 # static id counter

    def __init__(self, node_content=None, node_tails=[]):
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
        TreeNode.current_id += 1 # increment the static id counter
        self.__node_id = TreeNode.current_id
        self.__node_content = node_content
        self.__node_tails = node_tails
        self.__path = None

    def save(self, filename):
        """
        Description:
            saves the TreeNode object as a pkl file.
        Input:
            - filename: the file path to store the pickle dump file to.
        """
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    def load(self, filename):
        """
        Description:
            loads the TreeNode object from a dumped pkl file.
        Input:
            - filename: the pickle file path to load from.
        """
        with open(filename, 'rb') as f:
            self = pickle.load(f)

        return self

    def get_id(self):
        """
        Description:
            get uinique node id.
        Output:
            - returns the unique ID of the TreeNode instance.
        """
        return self.__node_id

    def get_content(self):
        """
        Description:
            get node content.
        Output:
            - the content attribute of the TreeNode instance.
        """
        return self.__node_content

    def get_tails(self):
        """
        Description:
            get tail nodes.
        Output:
            - returns the list of tails which are linked with the instance.
        """
        return self.__node_tails

    def set_path(self, path):
        """
        Description:
            set node path.
        Input:
            - path: sets the path attribute equal to the provided path.
        """
        self.__path = path

    def get_path(self):
        """
        Description:
            get node path.
        Output:
            - returns the node path.
        """
        return self.__path

    def set_content(self, content):
        """
        Description:
            set node contents.
        Input:
            - content: sets the content attribute equal to the provided content.
        """
        self.__node_content = content

    def add_tail(self, node=None):
        """
        Description:
            add a node to tail. If the node is not specified a node will be
            created and added.
        Input:
            - node: the node to append. if not provided a new NodeTree will be
                    created and linked.
        Output:
            - returns the newly linked TreeNode instance.
        """
        if node is None:
            node = TreeNode()
        self.__node_tails.append(node)
        node.__node_tails = []
        return node

    def remove_tail(self, node):
        """
        Description:
            removes a node from tail. if it is found and removed returens True,
            else returns False.
        Input:
            - node: the node object to be removed from tail nodes list.
        Output:
            - returns True if the node is found and removed, else returns False.
        """
        if node in self.__node_tails:
            self.__node_tails.remove(node)
            return True
        else:
            return False

    def walk(self, path=[]):
        """
        Description:
            this method walks through the tree and returns all nodes in
            each path to the leafs.
        Output:
            - returns the list of all possible pathes from the current node
              to the leaf terminal nodes of the tree.
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
        Description:
            this function visits every node in the tree, and returns a dictionary
            of {id:content}.
        Ouptut:
            - returns a dictionary containing node-ids as key
              and node contents as values for each node in the tree
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
        Description:
            Describes a tree as a list of paths and a list of contents.
        Output:
            - returns a dictionary with to key-words: "path" and "contents".
              each describing the possible paths and node contents.
        """
        paths = self.walk(path=[])
        contents = self.traverse()
        return {'paths':paths, 'contents':contents}
    
    
    def load_xml(self, filename):
        """
        Description:
            loads the TreeNode object from a xml file.
        Input:
            - filename: the xml file path to load from.
        """
        def content_parser(html_content):
            node_content = {'name':'','description':'',
                    'links':[]}
            texts = []
            links = []


            class MyHTMLParser(HTMLParser):
                def handle_starttag(self, tag, attrs):
                    #print("Encountered a start tag:", tag)
                    for (name,val) in attrs:
                        if name == 'href':
                            links.append({'name':'', 'link':val})
                def handle_endtag(self, tag):
                    pass#print("Encountered an end tag :", tag)
                    if len(links)>0 and len(texts)>0:
                        if links[-1]['name']=='':
                            links[-1]['name'] = texts[-1]
                            del texts[-1]
                    #print(texts)
                    #print(links)
                    #pdb.set_trace()
                def handle_data(self, data):
                    texts.append(data)
                    #print("Encountered some data  :", data)
            
            parser = MyHTMLParser()
            parser.feed(html_content)
            if len(texts) > 0:
                node_content['name'] = texts[0]
            if len(texts) > 1:
                node_content['description'] = ''.join(texts[1:])
            node_content['links'] = links

            #print('NAME:' + node_content['name'])
            #print('DES:' + node_content['description'])
            #print('LINKS:' + str(node_content['links']))
            return node_content

        
        xml_tree = xmlet.parse(filename)
        nodes_dict = {}
        connections_list = []
        # iterate over xml objects
        for obj in xml_tree.getroot()[0]:
            # if it is a node
            if 'value' in obj.keys():
                nodes_dict[obj.get('id')] = \
                        TreeNode(node_content=content_parser(
                            obj.get('value')))
                        #TreeNode(node_content=obj.get('value'))
            # if it is a connector
            elif 'source' in obj.keys():
                connections_list.append(obj)
        
        # make connections
        target_ids = set()
        source_ids = set()
        for connection in connections_list:
            source = nodes_dict[connection.get('source')]
            target = nodes_dict[connection.get('target')]
            source_ids.add(connection.get('source'))
            target_ids.add(connection.get('target'))
            source.add_tail(target)

        root_id = (source_ids - target_ids).pop()
        self.__node_tails = nodes_dict[root_id].__node_tails
        self.__node_content = nodes_dict[root_id].__node_content

        return self


def load_data(path):
    """
    Description:
        Loads all files associated with a tree, including tree object, image, and discription.
        Input is a path which indicates to the storage folder.
        Returns a dictionary if read was successful, else returns None.
    Input:
        - path: the directory path of the tree.
    Output:
        - tree data dictionary. containing "tree", "description", and "image" key-words.
    """
    tree_data = {'tree':None, 'image':None, 'description':None}

    try:
        with open(path+'/'+'tree.pkl', 'rb') as f:
            tree_data['tree'] = pickle.load(f)
    except:
        pass
    try:
        with open(path+'/'+'tree.txt', 'rb') as f:
            tree_data['description'] = f.read()
    except:
        pass
    try:
        # with open(path+'/'+'tree.png', 'rb') as f:
            tree_data['image'] = path+'/'+'tree.png'
    except:
        pass

    return tree_data

def save_data(path, tree_data):
    """
    Description:
        tree_data  is  {'tree':, 'image':, 'description':}
    Inputs:
        - path: the tree directory path
    Output:
        - returns True if the save was successful, else returns False.
    """
    if not os.path.isdir(path):
        os.mkdir(path)#, exists_ok=True)
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

