import os

from IPython import embed

import tree

TREE_PATH = './tree_data/test_0'

#os.mkdir(TREE_PATH)

tree_root = tree.TreeNode()
tree_root.set_content('ROOT')

node_a = tree_root.add_tail()
node_a.set_content('A')


node_b = tree_root.add_tail()
node_b.set_content('B')

node_c = node_a.add_tail()
node_c.set_content('C')

#tree_root.save(TREE_PATH + '/tree.pkl')

tree.save_data(TREE_PATH, {'tree':tree_root, 'description':'test tree 0'})

loaded_data = tree.load_data(TREE_PATH)

embed()
