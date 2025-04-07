def color_text(text, color_code):
    # Applies an ANSI color code to the given text.
    return f"\033[{color_code}m{text}\033[0m"


# Define color codes
BLUE = "94"
RED = "31"
YELLOW = "33"
GREEN = "32"


def get_movie_name():
    """
    Gets the user input for the movie name which is used further in various functions.
    """
    while True:
        movie = input(color_text("Enter movie name: ", BLUE)).title()
        if movie == "":
            print(color_text(f"Invalid Input. Enter a valid name", RED))
            continue
        else:
            return movie


def get_movie_rating():
    """
    Gets the user input for the movie rating which is used further in various functions.
    """
    while True:
        rating = input(color_text("Enter movie rating (0-10): ", BLUE)).replace(",", ".")
        if rating.replace(".", "").isdigit():
            rating = float(rating)
            if 0.0 <= rating <= 10.0:
                return rating
            else:
                print(color_text("Rating must be between 0 and 10", RED))
        else:
            print(color_text("Invalid input. Please enter numeric value", RED))


def get_movie_year():
    """
    Gets the user input for the movie year which is used further in various functions.
    """
    while True:
        year = input(color_text("Enter movie year: ", BLUE)).strip()
        if year.isdigit():
            year = int(year)
            if 1900 < year < 2025:
                return year
            else:
                print(color_text("Year must be 1900 and 2025", RED))
        else:
            print(color_text("Invalid input. Please enter numeric value", RED))
