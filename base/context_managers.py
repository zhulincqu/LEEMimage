import os
import time
import contextlib
import psycopg2

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
with in_dir(r'D:\programming\github\LEEMimage\doc'):
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

@contextlib.contextmanager
def open_read_only(filename):
    """A read-only version of 'open()' function.
    
    Args:
      filename (str): file to be opened.
    
    Yields:
      file object: reference to the read-only file
    """
    read_only_file = open(filename, 'r')
    
    # send control back to the context block
    # yield the reference to the file
    yield read_only_file 
    
    # close the open file
    read_only_file.close()
    
@contextlib.contextmanager
def database(url):
    """Setup code to connect to the database then 
disconnect the database after context block is done..

    Args:
      url (str): Place of the database. 
    
    Yields:
        db: Connected database.
    
    """
    # set up database connection
    db = psycopg2.connect(url)

    yield db

    # tear down database connection
    db.disconnect()
   
    
if __name__ == '__main__':

    # test 'in_dir()' context manager
    with in_dir(r'D:\programming\github\LEEMimage\doc') as new_dir:
        project_files = os.listdir()
        print(project_files)

    # test 'timer()' context manager        
    with timer():
        print('This should take approximately 0.25 seconds')
        time.sleep(0.25) 
        
    # test database()' context manager       
    url = 'http://dataquest.io/data'
    with database(url) as my_db:
        course_list = my_db.execute(
          'SELECT * FROM courses'
      )
        
    # test read-only 'open_read_only()' context manager
    with open_read_only(r'D:\programming\github\LEEMimage\doc\LEEM ImageHeader metadata field.txt') as f: 
        #print(f.read()) 
        pass
