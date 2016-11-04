# IMPORT CUSTOM FILES

import sys
import site
def get_main_path():
    app_path = sys.path[0] # sys.path[0] is current path in subdirectory
    split_on_char = "/"
    return split_on_char.join(app_path.split(split_on_char)[:-1])
main_path = get_main_path()
print (main_path)
site.addsitedir(main_path+'/util')
from util import python_version

import webbrowser
import cinema

# class definition with variables (state/data), methods, and constructor of instances
class Movie(cinema.Cinema):
    # pre-existing class variables __doc__
    """Movie class stores movie related information"""

    # class variables with constant values applicable to all instances
    VALID_RATINGS = ["G", "PG"]

    # constructor function that initialises memory for instance of class
    # first argument `self` is the instance (i.e. rambo) being created. it is added by default by Python
    def __init__(self,
                 cinema_name, cinema_location,
                 movie_title, movie_description, movie_thumbnail_url, movie_trailer_url):
        # initialise instance variables (state/data)
        cinema.Cinema.__init__(self, cinema_name, cinema_location)
        self.title = movie_title
        self.description = movie_description
        self.thumbnail_url = movie_thumbnail_url
        self.trailer_url = movie_trailer_url

    def show_info(self):
        print ( ("Movie {} info: {}, {}".format(self.title, self.cinema_name, self.cinema_location)) if (python_version.current_version() == 3) else ("Movie %s info: %s, %s") % (self.title, self.cinema_name, self.cinema_location) )

    # instance methods
    def show_trailer(self):
        webbrowser.open(self.trailer_url)