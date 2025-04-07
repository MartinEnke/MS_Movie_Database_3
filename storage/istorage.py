from abc import ABC, abstractmethod


class IStorage(ABC):
    """
    Abstracts base class that defines the interface for any storage system
    used in the movie application.

    All concrete storage classes (e.g., StorageJson) must implement these methods
    to ensure compatibility with the app's expected behavior.
    """

    @abstractmethod
    def list_movies(self):
        """
        Retrieves all movies from storage.
        Returns:
            dict: A dictionary of movie data.
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """
        Adds a new movie to the storage.
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        Deletes a movie from the storage by title.
        """
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """
        Updates the rating of an existing movie.
        """
        pass


'''
🧩 What is this file?
This defines your interface for storage — it's called IStorage, and it’s based on Python’s abc (abstract base class) system.

🧠 Purpose of IStorage:
It’s like a contract that says:

“Any class that wants to behave like a storage system must implement these exact methods.”

That means your StorageJson class is guaranteed to have:

list_movies()

add_movie(...)

delete_movie(...)

update_movie(...)

So when you pass around a variable of type storage, your code doesn’t need to know how it's implemented — just that it has these methods.

✅ Benefits:
Plug & play architecture
Later, you could build:

StorageCSV

StorageSQL

StorageFirebase

And as long as they implement IStorage, your app won’t care!

Editor/autocomplete help
PyCharm, VSCode, etc. will show method hints and warn you if a method is missing.

Cleaner code and easier testing
You can mock or replace storage logic for testing.

🎯 Real-world example:

def list_movies(storage: IStorage):
    movies = storage.list_movies()
    ...
Doesn’t matter whether storage is:

A StorageJson("movies.json")

Or a StorageCSV("movies.csv")

It will just work.

🛠 What to do with it:
Leave this file exactly as it is ✅
It’s perfect — and your StorageJson already inherits from it correctly:

class StorageJson(IStorage)
'''