import sys
from pydash import py_ # PyDash
import re # regular expressions
import random
import string

# IMPORT CUSTOM FILES

import site
def get_main_path():
    app_path = sys.path[0] # sys.path[0] is current path in subdirectory
    split_on_char = "/"
    return split_on_char.join(app_path.split(split_on_char)[:-1])
main_path = get_main_path()

site.addsitedir(main_path+'/util')
from util import python_version # __init__.py required in the helpers subdirectory

print ( ("Imported subfolder: {}/util".format(main_path)) if (python_version.current_version() == 3) else ("Importing subfolder: %s") % (main_path+'/util') )

def random_char(char_qty):
    return ''.join(random.choice(string.ascii_letters) for char in range(char_qty))

def random_number_already_exists_in_filename(filename, random_filename_suffix):
    randfile_ints_found = re.findall('\d+', filename) # array of numbers found in filename
    # suffix_matches_found = py_(randfile_ints_found).map(lambda x: x == random_filename_suffix).each(print).value()
    suffix_matches_found = py_(randfile_ints_found).map(lambda x: x == random_filename_suffix).each().value()
    print ( ("Numbers in filename matching proposed new random no: {}".format(suffix_matches_found)) if (python_version.current_version() == 3) else ("Numbers in filename matching proposed new random no: %s") % (suffix_matches_found) )

    assert (len(suffix_matches_found) > 0), 'Filename does not contain any numbers!'
    return True if any(element for element in suffix_matches_found) else False

def remove_numbers_from_filename_and_append_rand_int(filename, random_filename_suffix):
    return filter(lambda f: f.isalpha(), filename) + random_filename_suffix

def replace_non_numbers_with_rand_chars(new_filename_random_no):
    return re.sub("[^-0-9\/]+", random_char(5), new_filename_random_no)

