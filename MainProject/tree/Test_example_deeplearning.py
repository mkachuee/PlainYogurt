import pickle

from IPython import embed

import tree

TREE_PATH = './tree_data/example_cnn'

#os.mkdir(TREE_PATH)

tree_root = tree.TreeNode()
tree_root.set_content({'name':'Deep Learning', 'description':'', 'links':[]})

node_1 = tree_root.add_tail()
node_1.set_content({'name':'Convolutional Neural Networks', 
    'description': 'Resource: Imagenet classification with deep convolutional neural networks, A Krizhevsky, et al., 2012 ImageNet2012', 
    'links':[{'name':'paper', 'link':'https://scholar.google.com/citations?view_op=view_citation&hl=en&user=xegzhJcAAAAJ&citation_for_view=xegzhJcAAAAJ:u5HHmVD_uO8C'}]})


node_2 = node_1.add_tail()
node_2.set_content('')

node_3 = node_2.add_tail()
node_3.set_content({'name':'Machine Learning: Supervised Learning', 'description': 'Resource: Christopher M. Bishop. 2006. Pattern Recognition and Machine Learning (Information Science and Statistics). Springer-Verlag New York, Inc., Secaucus, NJ, USA. Part: Ch 3 and 4', 
    'links':[{'name':'paper', 'link':'http://dl.acm.org/citation.cfm?id=1162264'}]})

node_4 = node_3.add_tail()
node_4.set_content({'name':'Machine Learning: Conventional Neural Networks', 'description':'Resource: Christopher M. Bishop. 2006. Pattern Recognition and Machine Learning (Information Science and Statistics). Springer-Verlag New York, Inc., Secaucus, NJ, USA. Part:Ch 5',
    'links':[{'name':'paper', 'link':'http://dl.acm.org/citation.cfm?id=1162264'}]})

node_5 = node_2.add_tail()
node_5.set_content({'name':'Image Processing: Low-level Vision', 
    'description':'Resource: Online Tutorial (Link)', 
    'links':[{'name':'tutorial', 'link':'http://www.tutorialspoint.com/dip/'}]})

node_6 = node_2.add_tail()
node_6.set_content({'name':'Digital Signal Processing: 2-D Digital Filtering', 'description':'Resource: Online Tutorial', 
    'links':[{'name':'tutorial', 'link':'http://lodev.org/cgtutor/filtering.html'}]})

node_7 = node_6.add_tail()
node_7.set_content({'name':'Digital Signal Processing: 1-D Digital Filtering' , 'description':'Resource: Alan V. Oppenheim, Ronald W. Schafer, and John R. Buck. 1999. Discrete-Time Signal Processing (2nd Ed.). Prentice-Hall, Inc., Upper Saddle River, NJ, USA. Part:Ch 8, 9 , and 10', 
    'links':[{'name':'DSP book', 'link':'https://www.amazon.com/Digital-Signal-Processing-Alan-Oppenheim/dp/0132146355'}]})



tree_list = tree_root.to_list()

with open('./run_data/example_cnn.pkl', 'wb') as f:
    pickle.dump(tree_list, f)
embed()
