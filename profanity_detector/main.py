import sys, os, json

# allow running program from PythonTest main directory and the profanity_detector subdirectory
if "/".join(os.getcwd().split("/")[-1:]) == "PythonTest": # current folder name
    use_path = os.getcwd() + "/profanity_detector/text"
elif "/".join(os.getcwd().split("/")[-1:]) == "profanity_detector": # current folder name
    use_path = os.getcwd() + "/text"

# IMPORT CUSTOM FILES

import site
def get_main_path():
    app_path = sys.path[0] # sys.path[0] is current path in subdirectory
    split_on_char = "/"
    return split_on_char.join(app_path.split(split_on_char)[:-1])
main_path = get_main_path()
print (main_path)
site.addsitedir(main_path+'/util')
from util import python_version

if (python_version.current_version() == 3):
    import urllib.request
else:
    import urllib

print ( ("Imported subfolder: {}/util".format(sys.path[0])) if (python_version.current_version() == 3) else ("Imported subfolder: %s") % (sys.path[0]+'/util') )

print ( ("Use path: {}".format(use_path)) if (python_version.current_version() == 3) else ("Use path; %s") % (use_path) )

def read_text():
    # create a File object/instance by calling its init function
    text_file = open(os.path.expanduser(use_path))
    print ( ("Text file: {}".format(text_file)) if (python_version.current_version() == 3) else ("Text file: %s") % (text_file) )

    contents = text_file.read()
    print ( ("Contents of file: {}".format(contents)) if (python_version.current_version() == 3) else ("Contents of file: %s") % (contents) )

    text_file.close()
    check_profanity(contents)

def check_profanity(some_text):
    print("Filtering profanities from text...")
    if (python_version.current_version() == 3):
        url = "http://www.purgomalum.com/service/json?"
        data = {
            'text': some_text,
            'add': 'bloody,bomb,galaxy note 7',
            'fill_text': '****'
        }
        encodeddata = urllib.parse.urlencode(data).encode('UTF-8')
        # data=u"{}&add=bloody,bomb,galaxy note 7&fill_text=****".format(some_text)
        # encodeddata = data.encode('utf-8')
        # req = urllib.request.Request(url, encodeddata) # POST (not desired!)
        req = urllib.request.Request(url + encodeddata) # GET
        response = urllib.request.urlopen(req)
    else:
        response = urllib.urlopen("http://www.purgomalum.com/service/json?text=" + some_text + "&add=bloody,bomb,galaxy note 7" + "&fill_text=****")
    data = json.loads(response.read().decode('utf8'))
    print ( ("Filtered text: {}".format(data["result"])) if (python_version.current_version() == 3) else ("Filtered text: %s") % () )
    response.close()

read_text()

