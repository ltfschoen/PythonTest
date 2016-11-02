import sys
import os
from os import listdir
from os import path
from random import randint

# IMPORT CUSTOM FILES
import site
print ("Importing subfolder: %s") % (sys.path[0]+'/util')
site.addsitedir(sys.path[0]+'/util')  
import file_handler_util

def rename_filename(samples_folder_name, samples_absolute_path, filename, new_filename):
    os.rename(samples_absolute_path + filename, samples_absolute_path + new_filename)
    return os.listdir(''.join(['./', samples_folder_name]))
    
def rename_files():
    # get filenames from folder
    current_directory = os.getcwd()
    samples_folder_name = "temp"
    samples_absolute_path = current_directory + ''.join(['/', samples_folder_name, '/'])
    print("Sample path %s") % (samples_absolute_path)
    file_list = os.listdir(''.join(['./', samples_folder_name]))
    print("Subdirectory contents: %s") % (file_list)
    
    # rename each file with new random suffix
    for index, filename in enumerate(file_list, 0):
        print("Before - Index: %s, Filename: %s") % (index, filename)
        random_filename_suffix = str(randint(0,99))

        # generate new random file suffix until it does not match any numbers already in the filename
        while file_handler_util.random_number_already_exists_in_filename(filename, random_filename_suffix):
            random_filename_suffix = str(randint(0,99))

        new_filename_random_no = file_handler_util.remove_numbers_from_filename_and_append_rand_int(filename, random_filename_suffix)
        new_filename = file_handler_util.replace_non_numbers_with_rand_chars(new_filename_random_no)
        updated_file_list = rename_filename(samples_folder_name, samples_absolute_path, filename, new_filename)
        print("After - Index: %s, Filename: %s") % (index, updated_file_list[index])

rename_files()
