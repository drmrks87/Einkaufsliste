FILEPATH = "items.txt"

def get_items(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        items_local = file_local.readlines()
    return items_local


def write_items(items_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, "w") as file:
        file.writelines(items_arg)
