# PyDash
from pydash import py_
import os
from os import listdir
from os import path
from random import randint
import re # regular expressions
import random
import string

def random_char(char_qty):
    return ''.join(random.choice(string.ascii_letters) for char in range(char_qty))

def random_number_already_exists_in_filename(filename, random_filename_suffix):
    randfile_ints_found = re.findall('\d+', filename) # array of numbers found in filename
    # suffix_matches_found = py_(randfile_ints_found).map(lambda x: x == random_filename_suffix).each(print).value()
    suffix_matches_found = py_(randfile_ints_found).map(lambda x: x == random_filename_suffix).each().value()
    print("Numbers in filename matching proposed new random no: %s") % (suffix_matches_found)
    return True if any(element for element in suffix_matches_found) else False

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
        while random_number_already_exists_in_filename(filename, random_filename_suffix):
            random_filename_suffix = str(randint(0,99))
            
        # remove all numbers from filename and append random integer
        new_filename_random_no = filter(lambda f: f.isalpha(), filename) + random_filename_suffix

        # new filename with non-numbers replaced with random string of characters
        new_filename = re.sub("[^-0-9\/]+", random_char(5), new_filename_random_no)

        os.rename(samples_absolute_path + filename, samples_absolute_path + new_filename)
        updated_file_list = os.listdir(''.join(['./', samples_folder_name]))
        print("After - Index: %s, Filename: %s") % (index, updated_file_list[index])

rename_files()
