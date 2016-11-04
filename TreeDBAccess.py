#import models
#from django.db import IntegrityError
#from django.core.exceptions import FieldError
import uuid
import DBAccessToSaveLoad
subjectsFieldName = ['subject', 'category', 'topic']
treeInfoFieldName = ['name', 'topic', 'category', 'subject', 'DIRLink', 'tags']


"""
	The database consists of two relations:
	
	Subjects(category, subject, topic)
		
		Descirpion:
			Table containing categories, their corresponding subjects and topics
		
	
	TreeInfo(name, category, subject, topic, DIRLink, key)
	
		Description:
			Contains info on individual trees.
		
		name:
			name of tree
		category:
			category tree belongs to
		subject:
			subject of category tree belongs to
		topic:
			topics covered by tree
		DIRLink:
			link to object dump file, used for load/save
		key:
			tags used to search for tree

				


"""

def addToCategory(category, subject, topic):
	"""
		description - 
			Will add tupple (category, subject, topic) to Subjects relation.
		input - 
			category : string - category (eg. Math)
			subject : string - subject( eg. Algebra)
			topic : string  -  topic (eg. Addition)
		return -
			on failure returns None

	"""

	if (subject == None and topic == None):
		Subjects = models.Subjects(category=category, subject="", topic="")
		try:
			Subjects.save()
		except IntegrityError as e:
			return None
	elif (topic == None):
		Subjects = models.Subjects(category=category, subject=subject, topic="")
		try:
			Subjects.save()
		except IntegrityError as e:
			return None
	else:
		Subjects = models.Subjects(category=category, subject=subject, topic=topic)
		try:
			Subjects.save()
		except IntegrityError as e:
			return None
	return 1



def addToTreeInfo(name, category, subject, topic, keys):
	"""
		description - 
			Add tree to database, will create a unique path for tree to be added.
		input - 
			name : string - name of tree
			category : string - category (eg. Math)
			subject : string - subject( eg. Algebra)
			topic : string  -  topic (eg. Addition)
			keys : string - comma seperated tags
		return -
			None on failure

	"""

	dirlink = DBAccessToSaveLoad.generateDirName(name)
	dirlink = DBAccessToSaveLoad.getDirLink(dirlink)

	TreeInfo = models.TreeInfo(name = self.name, topic = self.topic, 
		category = self.category, subject = self.subject, 
		DIRLink = dirlink, tags = self.keys)
	try:
		TreeInfo.save()
	except IntegrityError as e:
		return None

def getColSubjects(*args):

	"""
		description - 
			filter Subjects relation given column field names, 
			column strings should be any of {category, subject, topic}
		input - 
			args[0] - specifiy one column 
			args[1] - optional 2nd column

		return -
			returns Queryset object

	"""
	length = len(args)
	fields = [s.lower() for s in subjectsFieldName]
	if (length == 0):
		return models.Subjects.objects.values()
	elif (length == 1):
		try:
			fieldName = args[0]
			i = fields.index(fieldName.lower())
			return models.Subjects.objects.values(subjectsFieldName[i])
		except FieldError as e:
			return None	
	elif (length == 2):
		try:
			fieldName1 = args[0]
			fieldName2 = args[1]
			i = fields.index(fieldName1.lower())
			j = fields.index(fieldName2.lower())
			return models.Subjects.objects.values(subjectsFieldName[i], subjectsFieldName[j])
		except FieldError as e:
			return None	
	elif (length == 3):
		try:
			fieldName1 = args[0]
			fieldName2 = args[1]
			fieldName3 = args[2]
			i = fields.index(fieldName1.lower())
			j = fields.index(fieldName2.lower())
			k = fields.index(fieldName3.lower())
			return models.Subjects.objects.values(subjectsFieldName[i], subjectsFieldName[j], subjectsFieldName[k])
		except FieldError as e:
			return None	
	else:
		return None



def getColTreeInfo(*args):
	"""
		description - 
			return TreeInfo relation with given column field names, 
			column strings should be any of {name, category, subject, topic, keys}
		input - 
			args[0] - specifiy one column 
			args[1] - optional 2nd column
			args[2] - optional 3rd column
			args[3] - optional 4th column
			args[4] - optional 5th column
		return -
			returns Queryset object

	"""	

	length = len(args)

	if (length == 0):
		return models.TreeInfo.objects.values()
	elif (length == 1):
		fieldName = args[0]
		try:
			i = [s.lower() for s in treeInfoFieldName].index(fieldName.lower())
			return models.TreeInfo.objects.values(treeInfoFieldName[i])
		except FieldError as e:
			return None	
	elif (length == 2):
		try:
			fields = [s.lower() for s in treeInfoFieldName]
			fieldName1 = args[0]
			fieldName2 = args[1]
			i = fields.index(fieldName1.lower())
			j = fields.index(fieldName2.lower())
			return models.TreeInfo.objects.values(treeInfoFieldName[i], treInfoFieldName[j])
		except FieldError as e:
			return None	
	elif (length == 3):
		try:
			fields = [s.lower() for s in treeInfoFieldName]
			fieldName1 = args[0]
			fieldName2 = args[1]
			fieldName3 = args[2]
			i = fields.index(fieldName1.lower())
			j = fields.index(fieldName2.lower())
			k = fields.index(fieldName3.lower())
			return models.TreeInfo.objects.values(treeInfoFieldName[i], treeInfoFieldName[j], treeInfoFieldName[k])
		except FieldError as e:
			return None	
	elif (length == 4):
		try:
			fields = [s.lower() for s in treeInfoFieldName]
			fieldName1 = args[0]
			fieldName2 = args[1]
			fieldName3 = args[2]
			fieldName4 = args[3]
			i = fields.index(fieldName1.lower())
			j = fields.index(fieldName2.lower())
			k = fields.index(fieldName3.lower())
			z = fields.index(fieldName4.lower())
			return models.TreeInfo.objects.values(treeInfoFieldName[i], treeInfoFieldName[j], treeInfoFieldName[k], treeInfoFieldName[z])
		except FieldError as e:
			return None	
	else:
		return None

def getTrees(name=None, *agrs):

	"""
		description - 
			queries database for trees info
		input - 
			args[0] - string - name filter
			args[1] - string - key filter
			args[2] - string - category filter
			args[3] - string - subject filter
			args[4] - string - topic filter
		return -
			returns Queryset object

	"""	
	length = len(args)

	tree = models.TreeInfo.objects
	if (name != None):
		tree = tree.filter(name__icontains=name)
	if (length >= 1):
		tree = tree.filter(keys__icontains=args[0])
	if (length >= 2):
		tree = tree.filter(category__icontains=args[1])
	if (length >= 3):
		tree = tree.filter(subject__icontains=args[2])
	if (length >= 4):
		tree = tree.filter(topic__icontains=args[3])
		
	try:
		return tree.values()
	except FieldError as e:
		return None

	
