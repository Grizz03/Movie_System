class User:
    def __init__(self, name):
        self.name = name
        self.movies = []

    # Defines the string when printed out.
    def __repr__(self):
        return '<User {}'.format(self.name)

    #  Filter method
    def watched_movies(self):
        # If false will remove from list
        return list(filter(lambda x: x.watched, self.movies))

