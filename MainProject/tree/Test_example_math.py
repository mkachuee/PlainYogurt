import pickle

from IPython import embed

import tree

TREE_PATH = './tree_data/example_cnn'

#os.mkdir(TREE_PATH)

#data['contents'][0] = {'name':'name 1', 'description':'des1', 'links':[{link:'//http',name:'wiki'}]}

tree_root = tree.TreeNode()
tree_root.set_content({'name':'Math',
    'description':'Important math resources', 
    'links':[]})

node_1 = tree_root.add_tail()
node_1.set_content({'name':'Linear Algebra',
    'description':'Linear Algebra fundamentals', 
    'links':[{'name':'link1', 
        'link':'https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/video-lectures/'},
        {'name':'link2', 'link':'https://www.khanacademy.org/math/linear-algebra'}]})

node_2 = tree_root.add_tail()
node_2.set_content({'name':'Probability and Statistics',
    'description':'Probability and Statistics fundamentals', 
    'links':[{'name':'mit ocw', 
        'link':'https://ocw.mit.edu/courses/find-by-topic/#cat=mathematics&subcat=probabilityandstatistics'}]})


node_3 = node_2.add_tail()
node_3.set_content({'name':'Discrete Math',
    'description':'Discrete Math basics', 
    'links':[{'name':'mit open courseware', 
        'link':'https://ocw.mit.edu/courses/mathematics/18-304-undergraduate-seminar-in-discrete-mathematics-spring-2015/'},
        {'name':'dmath', 'link':'https://ocw.mit.edu/courses/find-by-topic/#cat=mathematics&subcat=discretemathematics'}]})

node_4 = tree_root.add_tail()
node_4.set_content({'name':'Multivariable Calculus',
    'description':'Multivariable Calculus fundamentals', 
    'links':[{'name':'link1', 
        'link':'https://ocw.mit.edu/courses/mathematics/18-02sc-multivariable-calculus-fall-2010/'},
        {'name':'link2', 'link':'https://www.khanacademy.org/math/calculus-home/multivariable-calculus'}]})

node_5 = node_4.add_tail()
node_5.set_content({'name':'Single Variable Calculus',
    'description':'Single Variable Calculus basics', 
    'links':[{'name':'limitis', 
        'link':'https://www.youtube.com/playlist?list=PLE7EBBE9A482DC959'},
        {'name':'calc1', 'link':'https://www.coursera.org/learn/calculus1'}]})

node_6 = node_5.add_tail()
node_6.set_content({'name':'Pre-Calculus',
    'description':'Intro to Calculus', 
    'links':[{'name':'khan academy', 
        'link':'https://www.khanacademy.org/math/precalculus'},
        {'name':'storm', 'link':'https://www.brightstorm.com/math/precalculus/'}]})

tree_list = tree_root.to_list()

with open('./run_data/example_math.pkl', 'wb') as f:
    pickle.dump(tree_list, f)

embed()
