from movie import Movie


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    # Defines the string when printed out.
    def __repr__(self):
        return '<User {}'.format(self.name)

    def add_movie(self, name, genre):
        self.movies.append(Movie(name, genre, False))

    def delete_movie(self, name):
        list(filter(lambda movie: movie.name != name, self.movies))

    #  Filter method
    def watched_movies(self):
        # If false will remove from list
        return list(filter(lambda x: x.watched, self.movies))
