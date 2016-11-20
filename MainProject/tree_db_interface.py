"""
An interface between file management (load, and save) 
to back end DB access.

"""
import dbaccess as db
from tree.tree import TreeNode, load_data, save_data
import os
from MainProject.settings import STATICFILES_DIRS as FILE_DIR

def get_categories():
    """
        description -
            return all the categories stored on db
        input -
            None
        output -
            Queryset object containing categories.
    """
    q = db.get_col_subjects("category")
    q = q.distinct()
    return q

def get_category_subjects():
    """
        description -
            return all the categories and subjects stored on db
        input -
            None
        output -
            Queryset object containing result.
    """
    q = db.get_col_subjects("category", "subject")
    return q

def get_subjects_in_category(str):
    """
        description -
            get list of subjects in category
        input -
            str : category name
        output -
            Queryset object containing result.
    """
    q = db.get_subjects_tuple(category=str)
    return q

def get_specific_tuples(category, subject=None, topic=None):
    q = db.get_subjects_tuple(category=category, subject=subject, topic=topic)
    return q

def get_all_in_subjects():
    """
        description -
            return all the info stored in the subject table
        input -
            None
        output -
            Queryset object containing result.
    """
    q = db.get_col_subjects("category", "subject", "topic")
    return q


def search_trees(str):
    """
    description -
        search database tree entries for potential matches to user query
    input -
        str: user input string

    return -
        Queryset object containing search results
    """

    if (not str):
        return None

    found_entries = None
    found_entries  = db.search_tree(str)
    return found_entries




def load_trees(qset_obj):
    """
        description -
            given Queryset object, load tree objects from file.
        input -
            qset_obj: Queryset object containing tree tuples.
        output -
            list of tree objects
    """
    tree_objects = []
    # load tree objects
    for tuple in qset_obj:
        dir = tuple['DIRLink']
        complete_dir = FILE_DIR[0] + '' + dir #os.path.abspath(os.path.join(os.getcwd(), dir))
        t = load_data(complete_dir)
        t['image'] = dir + '/tree.png'
        tree_objects.append(t)
    return tree_objects




def save_tree(tree_object, **tree_details):
    """


    """
    tree_info = db.get_specific_tree(**tree_details)
    temp_status = None
    if (tree_info == None):
        temp_status =  db.add_tree_info(**tree_details)
        if (temp_status != None):
            temp_status = save_data(['DIRLink'], tree_object)
    else:
        temp_status = save_data(tree_info['DIRLink'], tree_object)

    return temp_status
