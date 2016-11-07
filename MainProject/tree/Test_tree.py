import pickle

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

node_d = node_c.add_tail()
node_d.set_content('D')

node_E = node_c.add_tail()
node_E.set_content('E')

#tree_root.save(TREE_PATH + '/tree.pkl')

tree.save_data(TREE_PATH, {'tree':tree_root, 'description': 'test tree 0'})

loaded_data = tree.load_data(TREE_PATH)

tree_list = tree_root.to_list()

with open('./run_data/tree_list.pkl', 'wb') as f:
    pickle.dump(tree_list, f)
embed()
