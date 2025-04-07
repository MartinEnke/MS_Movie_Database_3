from utils import color_text, RED, GREEN, BLUE, get_movie_name
import random


def random_movie(storage):
    """
    Loads the information from the JSON file.
    Randomly picks and displays a movie from the database.
    """
    movies = storage._load_movies()
    movies_list = []
    for movie in movies:
        movies_list.append(movie)
    movie = random.choice(movies_list)
    rating = movies[movie]["rating"]
    year = movies[movie]["year"]

    print(color_text(f"Your movie for tonight: '{movie} ({year})', Rating: {rating}", GREEN))


def search_movie(storage):
    """
    Loads the information from the JSON file.
    Displays all movies which hold at least a substring of the movie name.
    """
    movies = storage._load_movies()
    movie = get_movie_name().casefold()

    found = False
    for movies, details in movies.items():
        if movie in movies.casefold():
            print(color_text(f"- {movies}: {details["rating"]}", GREEN))
            found = True
    if not found:
        print(color_text("No entry under this name", RED))


def movies_sorted_by_alphabet(storage):
    """
    Loads the information from the JSON file.
    The movies in the dictionary get sorted in alphabetical order using key lamdba.
    """
    while True:
        user_choice = input(color_text(f"Enter 'A' for ascending order or 'Z' for descending oder: ", BLUE))
        if user_choice.lower() in ("a", "z"):
            break
        else:
            print(color_text(f"Invalid input. Enter 'A' or 'Z'", RED))

    movies = storage._load_movies()
    if user_choice.lower() == "a":
        sorted_movies = sorted(movies.items(), key=lambda item: item[0].lower())

        print(color_text(f"Movies listed in alphabetical order (A-Z):", GREEN))
        for movie, details in sorted_movies:
            print(f"{movie} ({details["year"]}) {details["rating"]}")

    if user_choice.lower() == "z":
        sorted_movies = sorted(movies.items(), key=lambda item: item [0].lower(), reverse=True)

        print(color_text(f"Movies listed in alphabetical order (Z-A: ", GREEN))
        for movie, details in sorted_movies:
            print(f"{movie} ({details["year"]}) {details["rating"]}")


def movies_sorted_by_rating(storage):
    """
    Loads the information from the JSON file.
    The movies in the dictionary get sorted by rating using key lamdba.
    """
    movies = storage._load_movies()
    sorted_movies = sorted(movies.items(), key=lambda item: item [1]["rating"], reverse=True)

    print(color_text(f"Movies listed by rating:", GREEN))
    for movie, details in sorted_movies:
        print(f"Rating: {details["rating"]} - {movie} ({details["year"]})")


def movies_sorted_by_year(storage):
    """
    Loads the information from the JSON file.
    The movies in the dictionary get sorted by year using key lamdba
    in ascending or descending order depending on uer_choice.
    """
    while True:
        user_choice = input(color_text(f"Enter 'up' for ascending order or 'down' for descending order: ", BLUE))
        if user_choice.lower() in ("up", "down"):
            break
        else:
            print(color_text(f"Invalid input. Enter 'up' or 'down'", RED))

    movies = storage._load_movies()
    if user_choice.lower() == "up":
        sorted_movies = sorted(movies.items(), key=lambda item: item[1]["year"])

        print(color_text(f"Movies listed by years (oldest top):", GREEN))
        for movie, details in sorted_movies:
            print(f"{details["year"]} - {movie}: {details["rating"]}")


    if user_choice.lower() == "down":
        sorted_movies = sorted(movies.items(), key=lambda item: item[1]["year"], reverse=True)

        print(color_text(f"Movies listed by years (latest top):", GREEN))
        for movie, details in sorted_movies:
            print(f"{details["year"]} - {movie} {details["rating"]}")


def filtering_movies(storage):
    """
    Loads the information from the JSON file.
    Filters the movies based on minimum rating, as well as start & end year requested from the user.
    """
    movies = storage._load_movies()
    while True:
        min_rating = input(color_text(f"Enter minimum rating (leave blank for no minimum rating): ", BLUE))
        if min_rating == "":
            min_rating = 0
            break
        try:
            min_rating = float(min_rating)
            if 0.1 <= min_rating <= 10:
                break
            else:
                print(color_text(f"Invalid input. Please enter a valid number (0-10)", RED))
        except ValueError:
            print(color_text(f"Invalid input. Enter numeric value (0-10)", RED))

    while True:
        start_year = input(color_text(f"Enter start year (leave blank for no start year): ", BLUE))
        if start_year == "":
            start_year = 0 # Allowing blank input
            break
        try:
            start_year = int(start_year)
            if 1900 <= start_year <= 2025:
                break
            if start_year < 1900 or start_year > 2025:
                user_choice = input(color_text(f"The year you entered is unrealistic. Do you want to continue? Y/N: ", RED))
                if user_choice.lower() in ("no", "n"):
                    continue
                if user_choice.lower() in ("yes", "y"):
                    break
                else:
                    print(color_text(f"Enter Y/N", RED))
        except ValueError:
            print(color_text(f"Invalid input. Please enter a valid year.", RED))

    while True:
        end_year = input(color_text(f"Enter end year (leave blank for no end year): ", BLUE))
        if end_year == "":
            end_year = 2025 # Allowing blank input
            break
        try:
            end_year = int(end_year)
            if end_year < start_year:
                print(color_text(f"The year you entered is lower than your start year", RED))
                continue
            if end_year < 1900 or end_year > 2025:
                user_choice = input(color_text(f"The year you entered is unrealistic. Do you want to continue? Y/N: ", RED))
                if user_choice.lower() in ("no", "n"):
                    continue
                if user_choice.lower() in ("yes", "y"):
                    break
                else:
                    print(color_text(f"Enter Y/N", RED))
            if 1900 <= end_year <= 2025:
                break

        except ValueError:
            print(color_text(f"Invalid input. Please enter a valid year.", RED))


    filtered_by_rating = {}
    for movie, details in movies.items():
        if details["rating"] >= min_rating and start_year <= details["year"] and end_year >= details["year"]:
            filtered_by_rating[movie] = {"rating": details["rating"], "year": details["year"]}

    if filtered_by_rating:
        print(color_text(f"\nFiltered movies", GREEN))
        for movie, details in filtered_by_rating.items():
            print(f"{movie} ({details["year"]}): {details["rating"]}")
    else:
        print(color_text(f"No movies were filtered", RED))