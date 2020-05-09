import os

@contextlib.contextmanager # decorator for context manager
def in_dir(path):
    """Change the current working directory to a specific 'path' 
and then change it back after the context block is done.

    Args:
    path (str): The target working directory.
    
    Returns:
    str : Target working directory.
    
    Notes:
    'in_dir()' is a context manager. 
Refer to context manager for more detail.
    
    Example:
with in_dir('/data/project_1/'):
    project_files = os.listdir()    
    """
    
    # save current working directory
    old_dir = os.getcwd()
    # switch to new working directory
    os.chdir(path)
    new_path = os.getcwd()

    # return new working directory
    yield new_path 

    # change back to previous
    # working directory
    os.chdir(old_dir)