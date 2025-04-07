from storage.storage_json import StorageJson
from features.movie_app import MovieApp
from utils import color_text, BLUE


"""
This program contains a json file which holds a dictionary
of a dictionary about movies, their year of appearance and their ratings.
It serves as a "Movie Database," offering features such as
listing, adding, deleting, updating, viewing statistics,
random selection, searching, sorting by ,
and filtering by rating or year.
Adding movies is possible via omdb API or manually.
A demo website to visualize all movies in the database can be generated.
To enhance the visual experience, various colors have been applied.
"""


def main():
    print(color_text("\n********** MOVIE DATABASE **********", BLUE))
    storage = StorageJson("movies.json")
    #storage = StorageCsv("movies.csv")
    app = MovieApp(storage)
    app.run()

if __name__ == "__main__":
    main()
