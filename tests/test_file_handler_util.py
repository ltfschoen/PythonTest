import sys
import pytest

# IMPORT CUSTOM FILES

import site
def get_main_path():
    test_path = sys.path[0] # sys.path[0] is current path in tests subdirectory 
    split_on_char = "/"
    return split_on_char.join(test_path.split(split_on_char)[:-1])
main_path = get_main_path()
print ("Importing subfolder: %s") % (main_path+'/util')
site.addsitedir(main_path+'/util')  
import file_handler_util

# UNIT TESTS

def test_file_handler_util_rand_char_length():
    assert len(file_handler_util.random_char(3)) == 3

def test_file_handler_util_random_number_already_exists_in_filename_45():
    assert file_handler_util.random_number_already_exists_in_filename("a_45_b", "45") == True

def test_file_handler_util_random_number_already_exists_in_filename_5():
    assert file_handler_util.random_number_already_exists_in_filename("a_45_b", "5") == True

def test_file_handler_util_random_number_already_exists_in_filename_with_no_numbers():   
    with pytest.raises(AssertionError):
        file_handler_util.random_number_already_exists_in_filename("a_b", "5")

def test_file_handler_util_remove_numbers_from_filename_and_append_rand_int(): 
    assert file_handler_util.remove_numbers_from_filename_and_append_rand_int("sa3m485ple45", "67") == "sample67"

def test_file_handler_util_replace_non_numbers_with_rand_chars(): 
    assert file_handler_util.replace_non_numbers_with_rand_chars("sample45") != "sample45"
