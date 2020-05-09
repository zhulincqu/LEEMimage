import os
import time
import contextlib


@contextlib.contextmanager # decorator for context manager
def in_dir(path):
    """Change the current working directory to a specific 'path' 
and then change it back after the context block is done.

    Args:
      path (str): The target working directory.
    
    Yields:
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

    # Send control back to the context block
    # Yield a new working directory
    yield new_path 

    # change back to previous
    # working directory
    os.chdir(old_dir)
    
@contextlib.contextmanager
def timer():
    """Time the execution of a context block.

    Yields:
      None
      
    Example:
with timer():
    print('This should take approximately 0.25 seconds')
    time.sleep(0.25)       
    """
    
    start = time.time()
    
    # Send control back to the context block
    yield
    
    end = time.time()
    print('Elapsed: {:.2f}s'.format(end - start))