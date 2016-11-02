import sys
import os

# allow running program from PythonTest main directory and the lie_detector subdirectory
if "/".join(os.getcwd().split("/")[-1:]) == "PythonTest": # current folder name
    use_path = os.getcwd() + "/lie_detector/text"
elif "/".join(os.getcwd().split("/")[-1:]) == "lie_detector": # current folder name
    use_path = os.getcwd() + "/text"

print ("Use path; %s") % (use_path)

def read_text():
    # create a File object/instance by calling its init function
    text_file = open(os.path.expanduser(use_path))
    print("Text file: %s") % (text_file)
    contents = text_file.read()
    print("Contents of file: %s") % (contents)
    text_file.close()

read_text()

