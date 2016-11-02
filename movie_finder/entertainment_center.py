import fresh_tomatoes
import media

rambo = media.Movie("Rambo",
                    "Action movie",
                    "http://www.eujacksonville.com/pages/01-31-08/Rambo%20movie%20review.jpg",
                    "https://youtu.be/aL39jJN9hHM?t=27s")

print ("Rambo description: %s") % (rambo.description)

# rambo.show_trailer()
movies = [rambo]
fresh_tomatoes.open_movies_page(movies)