import sys, os, urllib, json

# allow running program from PythonTest main directory and the profanity_detector subdirectory
if "/".join(os.getcwd().split("/")[-1:]) == "PythonTest": # current folder name
    use_path = os.getcwd() + "/profanity_detector/text"
elif "/".join(os.getcwd().split("/")[-1:]) == "profanity_detector": # current folder name
    use_path = os.getcwd() + "/text"

print ("Use path; %s") % (use_path)

def read_text():
    # create a File object/instance by calling its init function
    text_file = open(os.path.expanduser(use_path))
    print("Text file: %s") % (text_file)
    contents = text_file.read()
    print("Contents of file: %s") % (contents)
    text_file.close()
    check_profanity(contents)

def check_profanity(some_text):
    print("Filtering profanities from text...")
    response = urllib.urlopen("http://www.purgomalum.com/service/json?text=" + some_text + "&add=bloody,bomb,galaxy note 7" + "&fill_text=****")
    data = json.loads(response.read())
    print("Filtered text: %s") % (data["result"])
    response.close()

read_text()

