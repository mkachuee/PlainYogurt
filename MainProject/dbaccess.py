from home.models import Subjects, TreeInfo
from django.db import IntegrityError
from django.core.exceptions import FieldError
import uuid
import os

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

def add_to_category(category, subject=None, topic=None):
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
        subjects = Subjects(category=category, subject="", topic="")
        try:
            subjects.save()
        except IntegrityError as e:
            return None
    elif (topic == None):
        subjects = Subjects(category=category, subject=subject, topic="")
        try:
            subjects.save()
        except IntegrityError as e:
            return None
    elif (subject == None):
        subjects = Subjects(category=category, subject="", topic=topic)
        try:
            subjects.save()
        except IntegrityError as e:
            return None
    else:
        subjects = Subjects(category=category, subject=subject, topic=topic)
        try:
            subjects.save()
        except IntegrityError as e:
            return None
    return 1

def get_subjects_tuple(**kwargs):
    subjects = Subjects.objects
    if ('category' in kwargs):
        subjects = subjects.filter(category__icontains=kwargs['category'])
    if ('subject' in kwargs):
        subjects = subjects.filter(subject__icontains=kwargs['subject'])
    if ('topic' in kwargs):
        subjects = subjects.filter(topic__icontains=kwargs['topic'])

    try:
        return subjects.values()
    except FieldError as e:
        return None



def add_tree_info(name, category, subject, topic, keys):
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

    def generate_dir_name(str):
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

    def get_dir_link(dirname):
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

    dirlink = generate_dir_name(name)
    dirlink = get_dir_link(dirlink)

    treeInfo = TreeInfo(name = name, topic = topic,
        category = category, subject = subject,
        DIRLink = dirlink, tags = keys)
    try:
        treeInfo.save()
    except  ValueError as e:
        return None

def get_col_subjects(*args):

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
        return Subjects.objects.values()
    elif (length == 1):
        try:
            fieldName = args[0]
            i = fields.index(fieldName.lower())
            return Subjects.objects.values(subjectsFieldName[i])
        except FieldError as e:
            return None
    elif (length == 2):
        try:
            fieldName1 = args[0]
            fieldName2 = args[1]
            i = fields.index(fieldName1.lower())
            j = fields.index(fieldName2.lower())
            return Subjects.objects.values(subjectsFieldName[i], subjectsFieldName[j])
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
            return Subjects.objects.values(subjectsFieldName[i], subjectsFieldName[j],
                                                  subjectsFieldName[k])
        except FieldError as e:
            return None
    else:
        return None



def get_col_tree(*args):
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
        return TreeInfo.objects.values()
    elif (length == 1):
        fieldName = args[0]
        try:
            i = [s.lower() for s in treeInfoFieldName].index(fieldName.lower())
            return TreeInfo.objects.values(treeInfoFieldName[i])
        except FieldError as e:
            return None
    elif (length == 2):
        try:
            fields = [s.lower() for s in treeInfoFieldName]
            fieldName1 = args[0]
            fieldName2 = args[1]
            i = fields.index(fieldName1.lower())
            j = fields.index(fieldName2.lower())
            return TreeInfo.objects.values(treeInfoFieldName[i],
                                                  treeInfoFieldName[j])
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
            return TreeInfo.objects.values(treeInfoFieldName[i], treeInfoFieldName[j],
                                                  treeInfoFieldName[k])
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
            return TreeInfo.objects.values(treeInfoFieldName[i], treeInfoFieldName[j],
                                                  treeInfoFieldName[k], treeInfoFieldName[z])
        except FieldError as e:
            return None
    else:
        return None

def get_specific_tree(**kwargs):

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
    tree = TreeInfo.objects
    if ('name' in kwargs):
        tree = tree.filter(name__icontains=kwargs['name'])
    if ('key' in kwargs):
        tree = tree.filter(keys__icontains=kwargs['key'])
    if ('category' in kwargs):
        tree = tree.filter(category__icontains=kwargs['category'])
    if ('subject' in kwargs):
        tree = tree.filter(subject__icontains=kwargs['subject'])
    if ('topic' in kwargs):
        tree = tree.filter(topic__icontains=kwargs['topic'])
    try:
        return tree.values()
    except FieldError as e:
        return None