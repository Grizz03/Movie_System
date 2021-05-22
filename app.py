from movie import Movie  # Import files
from user import User

user = User('Steve')

my_movie = Movie("The Matrix", "Sci-Fi", True)

user.movies.append(my_movie)

print(user)
print(user.watched_movies())

