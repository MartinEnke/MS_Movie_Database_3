from utils import color_text, BLUE, GREEN, RED, get_movie_name, get_movie_rating, get_movie_year
from features.stats import stats
from features.process_movies import (
    random_movie, search_movie, movies_sorted_by_rating,
    movies_sorted_by_year, movies_sorted_by_alphabet, filtering_movies)
from services.omdb_api import fetch_movie_data
import sys
import os


class MovieApp:
    """
    Main app class that provides interactive menu
    to manage a movie database, like adding, deleting, updating,
    viewing stats, sorting, searching, and more.
    """

    def __init__(self, storage):
        """
        Initialize the MovieApp with a storage backend.
        """
        self._storage = storage

    def _command_list_movies(self):
        """
        Displays all movies stored in the database along with their year and rating.
        """
        movies = self._storage.list_movies()
        if not movies:
            print(color_text("No movies found.", RED))
            return
        for title, details in movies.items():
            print(f"{title} ({details['year']}): {details['rating']}")

    def _command_add_movie(self):
        title = get_movie_name()

        movie_data = fetch_movie_data(title)

        if movie_data:
            print(color_text(f"OMDb found '{movie_data['title']}'!", GREEN))
            print(f"Year: {movie_data['year']}, Rating: {movie_data['rating']}, Poster: {movie_data['poster']}")
            confirm = input(color_text("Do you want to use this data? (Y/N): ", BLUE)).strip().lower()
            if confirm == "n":
                movie_data = None

        if not movie_data:
            # fallback to manual entry
            year = get_movie_year()
            rating = get_movie_rating()
            movie_data = {
                "title": title,
                "year": year,
                "rating": rating,
                "poster": None
            }
        confirm = input(color_text(f"Add {title}? (Y/N): ", BLUE)).strip().lower()
        if confirm == "n":
            return
        try:
            self._storage.add_movie(
                title=movie_data["title"],
                year=movie_data["year"],
                rating=movie_data["rating"],
                poster=movie_data["poster"]
            )
            print(color_text(f"'{movie_data['title']}' added successfully!", GREEN))
        except ValueError as e:
            print(color_text(str(e), RED))

    def _command_delete_movie(self):
        """
        Prompts user to enter a movie name and delete it from the database.
        """
        title = get_movie_name()
        if title not in self._storage.list_movies():
            print(color_text(f"Movie '{title}' not found.", RED))
            return
        confirm = input(color_text(f"Delete {title}? (Y/N): ", BLUE)).strip().lower()
        if confirm == "n":
            return
        self._storage.delete_movie(title)
        print(color_text(f"'{title}' deleted.", GREEN))

    def _command_update_movie(self):
        """
        Prompts user to enter a movie name and update its rating.
        """
        title = get_movie_name()
        if title not in self._storage.list_movies():
            print(color_text(f"Movie '{title}' not found.", RED))
            return

        rating = get_movie_rating()
        confirm = input(color_text(f"Update {title}? (Y/N): ", BLUE)).strip().lower()
        if confirm == "n":
            return
        self._storage.update_movie(title, rating)
        print(color_text(f"'{title}' rating updated.", GREEN))

    def _command_movie_stats(self):
        """
        Displays statistical information about movie ratings
        """
        stats(self._storage)

    def _command_random_movie(self):
        """
        Displays a randomly selected movie from the database.
        """
        random_movie(self._storage)

    def _command_search_movie(self):
        """
        Prompts user to search for movies by keyword.
        Displays matching results.
        """
        search_movie(self._storage)

    def _command_movies_sorted_by_rating(self):
        """
        Displays the list of movies sorted by rating.
        """
        movies_sorted_by_rating(self._storage)

    def _command_movies_sorted_by_year(self):
        """
        Displays the list of movies sorted by release year.
        """
        movies_sorted_by_year(self._storage)

    def _command_generate_website(self):
        """
        Generates an HTML website from the current movie database using a predefined template.
        Replaces placeholders with the app title and the HTML movie grid.
        """
        # Dynamically locate the template file based on this file's location
        current_dir = os.path.dirname(__file__)
        template_path = os.path.join(current_dir, "..", "static", "index_template.html")
        output_path = os.path.join(current_dir, "..", "index.html")

        try:
            with open(template_path, "r") as template_file:
                template_html = template_file.read()
        except FileNotFoundError:
            print(color_text("Template file not found.", RED))
            return

        # Replace title
        template_html = template_html.replace("__TEMPLATE_TITLE__", "Martin's Movie Database")

        # Build movie grid
        movies = self._storage.list_movies()
        movie_html = ""
        for title, data in movies.items():
            movie_html += f"""
            <div class="movie">
                <img src="{data.get("poster", "")}" alt="{title} poster" title="{data.get("notes", "")}">
                <div class="movie-title">{title}</div>
                <div class="movie-year">{data.get("year", "Unknown")}</div>
                <div class="movie-rating">{data.get("rating", "N/A")}</div>
            </div>
            """

        template_html = template_html.replace("__TEMPLATE_MOVIE_GRID__", movie_html)

        # Write to output HTML file
        with open(output_path, "w") as output_file:
            output_file.write(template_html)

        print(color_text("Website was generated successfully.", GREEN))

    def run(self):
        """
        Starts interactive movie app menu and handles user commands.
        Loops until the user chooses to exit.
        """

        while True:
            print()
            menu_text = """Menu:
0. Exit
1. List movies
2. Add movie
3. Delete movie
4. Update movie
5. Stats
6. Random movie
7. Search movie
8. Movies sorted by rating
9. Movies sorted by year
10. Movies sorted alphabetically
11. Filter movies
12. Generate website
"""
            print(color_text(menu_text, BLUE))

            choice = input(color_text("Choose an option (0–12): ", BLUE))

            if choice == "1":
                self._command_list_movies()
            elif choice == "2":
                self._command_add_movie()
            elif choice == "3":
                self._command_delete_movie()
            elif choice == "4":
                self._command_update_movie()
            elif choice == "5":
                self._command_movie_stats()
            elif choice == "6":
                self._command_random_movie()
            elif choice == "7":
                self._command_search_movie()
            elif choice == "8":
                self._command_movies_sorted_by_rating()
            elif choice == "9":
                self._command_movies_sorted_by_year()
            elif choice == "10":
                self._command_movies_sorted_by_alphabet()
            elif choice == "11":
                self._command_filtering_movies()
            elif choice == "12":
                self._command_generate_website()
            elif choice == "0":
                print(color_text("Bye!", GREEN))
                sys.exit()
            else:
                print(color_text("Invalid choice. Try again.", RED))
