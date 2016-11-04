import os
import tree

"""
An interface between file management (load, and save) 
to back end DB access.

"""
def generateDirName(str):
	"""
		description - 
			generates a unique folder name for tree
		input - 
			str : string will be appeneded to a unique id
		return -
			dirname : unique name

	"""
	cat = uuid.uuid1()
	cat_str = cat.urn
	dirname = str + cat_str[9:18] 
	return dirname

def getDirLink(dirname):
	"""
		description -
			get the present working directory and return path using directory name
		input -
			dirname: the directory name
		output -
			PATH: path to directory na

	"""

	PATH = os.getcwd()
	PATH = PATH + '/' + dirname
	return PATH


def fetchTrees(query):
	"""
		description -
			given query, fetch trees from the database
		input - 
			query: string submitted by user to search trees
		output -
			list of tree's 
	"""
	


def loadTree(*args):
	"""
		description - 
			using *args fetch tree to be loaded.
		input - 
			*args: can contain key, name, category, subject, topic, id of tree of interest

		output - 
			return object dump to front-end
	"""

	return



def saveTree(tree):

	"""
		description -
			dump tree object to file and update database
		input - 
			tree: object containing information on tree
		output -
			None

	"""

	return
