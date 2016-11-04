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

import fresh_tomatoes
import media
import cinema

ritz = cinema.Cinema("Ritz", "Sydney")
print ( ("Cinema location of Ritz is: {}".format(ritz.cinema_location)) if (python_version.current_version() == 3) else ("Cinema location of Ritz is: %s") % (ritz.cinema_location) )

rambo = media.Movie("Baroque Theatre",
                    "Melbourne",
                    "Rambo",
                    "Action movie",
                    "http://www.eujacksonville.com/pages/01-31-08/Rambo%20movie%20review.jpg",
                    "https://youtu.be/aL39jJN9hHM?t=27s")


print ( ("Rambo shown at: {}".format(rambo.show_info())) if (python_version.current_version() == 3) else ("Rambo shown at: %s") % (rambo.show_info()) )
print ( ("Rambo description: {}".format(rambo.description)) if (python_version.current_version() == 3) else ("Rambo description: %s") % (rambo.description) )
print ( ("Movie valid ratings: {}".format(media.Movie.VALID_RATINGS)) if (python_version.current_version() == 3) else ("Movie valid ratings: %s") % (media.Movie.VALID_RATINGS) )
print ( ("Movie documentation from __doc__: {}".format(media.Movie.__doc__)) if (python_version.current_version() == 3) else ("Movie documentation from __doc__: %s") % (media.Movie.__doc__) )
print ( ("Movie class __module__: {}".format(media.Movie.__module__)) if (python_version.current_version() == 3) else ("Movie class __module__: %s") % (media.Movie.__module__) )
print ( ("Movie class __name__: {}".format(media.Movie.__name__)) if (python_version.current_version() == 3) else ("Movie class __module__: %s") % (media.Movie.__name__) )

# rambo.show_trailer()
movies = [rambo]
fresh_tomatoes.open_movies_page(movies)