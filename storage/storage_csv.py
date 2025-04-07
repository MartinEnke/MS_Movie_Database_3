import csv
from storage.istorage import IStorage


class StorageCsv(IStorage):
    """
    A CSV-based implementation of the IStorage interface for managing movies.
    Stores and retrieves movie data from a specified CSV file.
    """

    def __init__(self, file_path):
        """
        Initializes the storage with the path to the CSV file.

        Args:
            file_path (str): Path to the CSV file used for movie storage.
        """
        self.file_path = file_path

    def _load_movies(self):
        """
        Loads movie data from the CSV file.

        Returns:
            dict: Dictionary of movies with title as key and attributes as values.
        """
        movies = {}
        try:
            with open(self.file_path, newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row["title"]
                    movies[title] = {
                        "year": int(row["year"]),
                        "rating": float(row["rating"]),
                        "poster": row.get("poster", None)
                    }
        except FileNotFoundError:
            pass  # Treat missing file as an empty movie list
        return movies

    def _save_movies(self, movies):
        """
        Saves movie data to the CSV file.

        Args:
            movies (dict): Dictionary of movies to be saved.
        """
        with open(self.file_path, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["title", "year", "rating", "poster"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for title, details in movies.items():
                writer.writerow({
                    "title": title,
                    "year": details["year"],
                    "rating": details["rating"],
                    "poster": details.get("poster", "")
                })

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
        movies[title] = {"year": year, "rating": rating, "poster": poster}
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
