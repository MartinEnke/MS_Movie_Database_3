import matplotlib.pyplot as plt
from utils import color_text
from utils import GREEN, BLUE


def stats(storage):
    movies = storage._load_movies()
    ratings = [details["rating"] for details in movies.values()]

    count = len(ratings)
    average_rating = sum(ratings) / count
    print(f"Average rating: {average_rating:.2f}")

    sorted_ratings = sorted(ratings)
    if count % 2 == 1:
        median_rating = sorted_ratings[count // 2]
    else:
        mid1 = sorted_ratings[count // 2 - 1]
        mid2 = sorted_ratings[count // 2]
        median_rating = (mid1 + mid2) / 2
    print(f"Median rating: {median_rating:.2f}")

    max_rating = max(ratings)
    best_movies = [movie for movie, details in movies.items() if details["rating"] == max_rating]
    print(f"Best movie(s) with rating: {max_rating}:")
    for movie in best_movies:
        print(color_text(f"- {movie}", GREEN))

    min_rating = min(ratings)
    worst_movies = [movie for movie, details in movies.items() if details["rating"] == min_rating]
    print(f"Worst movie(s) with rating: {min_rating}:")
    for movie in worst_movies:
        print(color_text(f"- {movie}", GREEN))



def rating_histogram(storage):
    movies = storage._load_movies()
    ratings = [details["rating"] for details in movies.values()]

    plt.hist(ratings, bins=range(0, 11), edgecolor="yellow")
    plt.title('Movie Ratings Histogram')
    plt.ylabel('Frequency')
    plt.xlabel('Ratings')

    file_name = input(color_text("Enter filename to save histogram: ", BLUE))
    plt.savefig(file_name)
    print(color_text(f"Histogram successfully saved to '{file_name}'", GREEN))
    plt.show()
