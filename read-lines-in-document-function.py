# Create function to read the lines of a document
def get_lines(filename)
  """
  Reads filename (a text file) and returns the lines of test as a list.
  Args:
   filename: a string for the target filepath
  returns:
   A list of strings with 1 string per line 
  """
  with open(filename, "r") as f:
    return f.readlines()
    
