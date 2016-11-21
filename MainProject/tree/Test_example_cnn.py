import pickle

from IPython import embed

import tree

TREE_PATH = './tree_data/example_cnn'

#os.mkdir(TREE_PATH)

tree_root = tree.TreeNode()
tree_root.set_content('Deep Learning')

node_1 = tree_root.add_tail()
node_1.set_content('Convolutional Neural Networks \n Resource: Imagenet classification with deep convolutional neural networks \n A Krizhevsky, et al., 2012 ImageNet2012(Link)')


node_2 = node_1.add_tail()
node_2.set_content('')

node_3 = node_2.add_tail()
node_3.set_content('Machine Learning: Supervised Learning \n Resource: Christopher M. Bishop. 2006. Pattern Recognition and Machine Learning (Information Science and Statistics). Springer-Verlag New York, Inc., Secaucus, NJ, USA. (Link) Part: Ch 3 and 4')

node_4 = node_3.add_tail()
node_4.set_content('Machine Learning: Conventional Neural Networks \n Resource: Christopher M. Bishop. 2006. Pattern Recognition and Machine Learning (Information Science and Statistics). Springer-Verlag New York, Inc., Secaucus, NJ, USA. (Link) \n Part:Ch 5')

node_5 = node_2.add_tail()
node_5.set_content('Image Processing: Low-level Vision \n Resource: Online Tutorial (Link)')

node_6 = node_2.add_tail()
node_6.set_content('Digital Signal Processing: 2-D Digital Filtering \n Resource: Online Tutorial (Link)')

node_7 = node_6.add_tail()
node_7.set_content('Digital Signal Processing: 1-D Digital Filtering \n Resource: Alan V. Oppenheim, Ronald W. Schafer, and John R. Buck. 1999. Discrete-Time Signal Processing (2nd Ed.). Prentice-Hall, Inc., Upper Saddle River, NJ, USA. (Link) \n Part:Ch 8, 9 , and 10')

#tree_root.save(TREE_PATH + '/tree.pkl')

tree.save_data(TREE_PATH, {'tree':tree_root, 'description': 'Deep learning (also known as deep structured learning, hierarchical learning or deep machine learning) is a branch of machine learning based on a set of algorithms that attempt to model high level abstractions in data by using a deep graph with multiple processing layers, composed of multiple linear and non-linear transformations.'})

loaded_data = tree.load_data(TREE_PATH)

tree_list = tree_root.to_list()

with open('./run_data/example_cnn.pkl', 'wb') as f:
    pickle.dump(tree_list, f)
embed()
