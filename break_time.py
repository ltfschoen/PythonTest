# IMPORT
import sys
import os
import time
import webbrowser
import site

# IMPORT CUSTOM FILES

site.addsitedir(sys.path[0]+'/helpers')
from helpers import reusable # __init__.py required in the helpers subdirectory
site.addsitedir(sys.path[0]+'/util')
from util import python_version

# SHOW INFO
print ( ("System path: {}".format(sys.path)) if (python_version.current_version() == 3) else ("System path: %s") % (sys.path) )
print ( ("Env keys: {}".format(os.environ.keys())) if (python_version.current_version() == 3) else ("Env keys: %s") % (os.environ.keys()) )
print ( ("Imported subfolder: {}/helpers".format(sys.path[0])) if (python_version.current_version() == 3) else ("Importing subfolder: %s") % (sys.path[0]+'/helpers') )

again = "y"
break_limit = 3
break_count = 0
remaining = break_limit

while again == "y" and break_count < break_limit:
    time.sleep(3) # seconds
    print ( ("You have {} remaining breaks to take advantage of!".format(remaining)) if (python_version.current_version() == 3) else ("You have %s remaining breaks to take advantage of!") % (remaining) )
    if remaining == break_limit:
        print(reusable.messages['exit_exhausted_breaks'])

    again = input("Take another break? y/n >>>") if (python_version.current_version() == 3) else raw_input("Take another break? y/n >>>")
    if again != "y":
        print(reusable.messages['exit_request_no_more_breaks'])
    else:
        webbrowser.open(reusable.urls['so'])
        break_count += 1
        remaining -= 1
print(reusable.messages['exit_common_message'])
