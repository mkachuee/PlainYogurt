import pickle

from IPython import embed

import tree

TREE_PATH = './tree_data/test_0'

#os.mkdir(TREE_PATH)

tree_root = tree.TreeNode()
tree_root.load_xml('./run_data/tree_xml.xml')


embed()
