import webbrowser

# class definition with variables (state/data), methods, and constructor of instances
class Movie():
    # constructor function that initialises memory for instance of class
    # first argument `self` is the instance (i.e. rambo) being created. it is added by default by Python
    def __init__(self, movie_title, movie_description, movie_thumbnail_url, movie_trailer_url):
        # initialise instance variables (state/data)
        self.title = movie_title
        self.description = movie_description
        self.thumbnail_url = movie_thumbnail_url
        self.trailer_url = movie_trailer_url

    # instance methods
    def show_trailer(self):
        webbrowser.open(self.trailer_url)