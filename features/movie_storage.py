from utils import color_text, BLUE, RED, GREEN


def list_movies(storage):
    """
    Lists all movies of the movie database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = storage.list_movies()
    for movie_name, details in movies.items():
        print(f"{movie_name} ({details["year"]}): {details["rating"]}")


def add_movie(storage, get_movie_rating, get_movie_year):
    """
    Adds a movie to the movie database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = storage.list_movies()
    while True:
        movie = input(color_text("Enter movie name or 'X' to exit: ", BLUE)).title()
        if movie.lower() == "x":
            return
        if movie in movies:
            print(color_text(f"Movie '{movie}' already exists", RED))
            return

        rating = get_movie_rating()
        year = get_movie_year()

        while True:
            user_escape = input(color_text(f"Save the movie: '{movie} ({year}) - {rating}'? Y/N: ", GREEN))
            if user_escape.lower() not in ("n", "y"):
                print(color_text("Enter Y/N", RED))
                continue
            if user_escape.lower() == "n":
                break
            if user_escape.lower() == "y":
                storage.add_movie(title=movie, year=year, rating=rating, poster=None)
                print(color_text(f"Movie '{movie}' successfully added", GREEN))
                break


from utils import color_text, BLUE, RED, GREEN

def delete_movie(storage, title):
    """
    Deletes a movie from the movie database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. Prompts user for confirmation and shows correct movie data.
    """
    movies = storage.list_movies()

    while True:
        movie = input(color_text("Enter movie name or 'X' to exit: ", BLUE)).title()

        if movie == "":
            print(color_text("Invalid Input. Enter a valid name", RED))
            continue
        if movie.lower() == "x":
            return
        if movie not in movies:
            print(color_text(f"Movie '{movie}' doesn't exist", RED))
            continue

        # ✅ Now fetch the correct year & rating AFTER validation
        details = movies[movie]
        rating = details["rating"]
        year = details["year"]

        while True:
            user_choice = input(color_text(f"Delete: {movie} ({year}) {rating}? - Y/N: ", RED))
            if user_choice == "":
                print("Enter Y/N")
                continue
            if user_choice.lower() == "n":
                return
            if user_choice.lower() == "y":
                storage.delete_movie(movie)
                print(color_text(f"Movie '{movie}' successfully deleted", GREEN))
                return


from utils import color_text, BLUE, RED, GREEN


def update_movie(storage, get_movie_name, get_movie_rating):
    """
   Updates a movie in the movie database.
   Loads the information from the JSON file, updates the movie,
   and saves it. Prompts user for confirmation and shows correct movie data.
   """
    movies = storage.list_movies()

    while True:
        movie = input(color_text("Enter movie name or 'X' to exit: ", BLUE)).title()
        if movie == "":
            print(color_text("Invalid Input. Enter a valid name", RED))
            continue
        if movie.lower() == "x":
            return
        if movie not in movies:
            print(color_text(f"Movie '{movie}' doesn't exist", RED))
            continue

        details = movies[movie]
        year = details["year"]

        choice = input(color_text("Do you want to update the movie name? (Y/N): ", BLUE))

        if choice.lower() == "y":
            new_name = get_movie_name()
            rating = get_movie_rating()
            storage.delete_movie(movie)
            storage.add_movie(title=new_name, year=year, rating=rating, poster=None)
            print(color_text(f"Movie name and rating updated to '{new_name}'", GREEN))

        elif choice.lower() == "n":
            rating = get_movie_rating()
            storage.update_movie(title=movie, rating=rating)
            print(color_text(f"Rating for movie '{movie}' successfully updated", GREEN))

        else:
            print(color_text("Please enter Y or N", RED))
            continue

        break
