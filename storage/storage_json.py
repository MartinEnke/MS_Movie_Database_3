from storage.istorage import IStorage
import json


class StorageJson(IStorage):
    """
    A JSON-based implementation of the IStorage interface for managing movies.
    Stores and retrieves movie data from a specified JSON file.
    """

    def __init__(self, file_path):
        """
        Initializes the storage with the path to the JSON file.
        """
        self.file_path = file_path

    def _load_movies(self):
        """
        Loads movie data from the JSON file.

        Returns:
            dict: Dictionary of movies where keys are titles and values are metadata.
        """
        with open(self.file_path, "r") as file:
            return json.load(file)

    def _save_movies(self, movies):
        """
        Saves movie data to the JSON file.
        """
        with open(self.file_path, "w") as file:
            json.dump(movies, file, indent=4)

    def list_movies(self):
        """
        Retrieves all movies from storage.

        Returns:
            dict: Dictionary of movies.
        """
        return self._load_movies()

    def add_movie(self, title, year, rating, poster):
        """
        Adds a new movie to the database.

        Raises:
            ValueError: If the movie already exists.
        """
        movies = self._load_movies()
        if title in movies:
            raise ValueError(f"Movie {title} already exists")
        movies[title] = {"rating": rating, "year": year, "poster": poster}
        self._save_movies(movies)

    def delete_movie(self, title):
        """
        Deletes a movie from the database.

        Raises:
            ValueError: If the movie does not exist.
        """
        movies = self._load_movies()
        if title not in movies:
            raise ValueError(f"Movie {title} doesn't exist")
        del movies[title]
        self._save_movies(movies)

    def update_movie(self, title, rating):
        """
        Updates the rating of an existing movie.

        Raises:
            ValueError: If the movie does not exist.
        """
        movies = self._load_movies()
        if title not in movies:
            raise ValueError(f"Movie {title} doesn't exist")
        movies[title]["rating"] = rating
        self._save_movies(movies)


'''
Why are _save_movies() and _load_movies() and all _commands() set to "internal"?
Because they're:
- Not meant to be called from outside your class (StorageJson)
- But still useful for re-use inside the class
- Marked with _ to say: "Hey, don't use this unless you know what you're doing."
- They’re part of the internal implementation, not the public API.

Why not make them private with __double_underscore?
Because:
- You don’t really need full privacy in this case
- Name mangling (e.g. __save_movies) makes debugging and testing harder
- _ is enough for most cases in Python — it’s clear and readable, and keeps things simple
- You’d only use __name for something like:
  - Preventing subclass override
  - Hiding sensitive logic
  - Protecting state in libraries

Why public methods like list_movies() don’t use _
Because those methods are the interface:
- They're called by your app (movie_app)
- They're exposed on purpose (like API endpoints)
- They’re intended to be accessed from outside the class
'''