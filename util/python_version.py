import sys
import re

def current_version():
    return 3 if re.match(r"([^\s]+)", sys.version).group()[:1] == "3" else 2