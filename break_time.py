# IMPORT
import sys
import os
import time
import webbrowser

# SHOW INFO
print ("System path: %s") % (sys.path)
print ("Env keys: %s") % (os.environ.keys())

# IMPORT CUSTOM FILES
import site
print ("Importing subfolder: %s") % (sys.path[0]+'/helpers')
site.addsitedir(sys.path[0]+'/helpers')
from helpers import reusable # __init__.py required in the helpers subdirectory

again = "y"
break_limit = 3
break_count = 0
remaining = break_limit

while again == "y" and break_count < break_limit:
    time.sleep(3) # seconds
    print("You have %s remaining breaks to take advantage of!") % (remaining)
    if remaining == break_limit:
        print(reusable.messages['exit_exhausted_breaks'])
    again = raw_input("Take another break? y/n >>>")
    if again != "y":
        print(reusable.messages['exit_request_no_more_breaks'])
    else:
        webbrowser.open(reusable.urls['so'])
        break_count += 1
        remaining -= 1
print(reusable.messages['exit_common_message'])
