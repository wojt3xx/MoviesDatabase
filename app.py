from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new movie
- 'l' to list all movies
- 'w' to mark a movie as watched
- 'd' to delete a movie
- 'q' to quit

Your choice: """


def menu():
    database.create_movies_table()  # just to make sure the file is created
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_movie()
        elif user_input == 'l':
            list_movies()
        elif user_input == 'w':
            prompt_watch_movie()
        elif user_input == 'd':
            prompt_delete_movie()
        else:
            print("Unknown command. Please try again.")

        user_input = input(USER_CHOICE)


def prompt_add_movie():
    name = input("Enter the name of the movie: ")
    year = int(input("Enter the year movie was released: "))
    director = input("Enter the director of the movie: ")
    rating = int(input("Enter the rating of the movie from 1 to 10: "))
    watched = input("Have you already watched this movie (True or False): ")

    watched_format = watched.title()

    database.add_movie(name, year, director, rating, watched_format)


def list_movies():
    movies = database.get_all_movies()
    for movie in movies:
        is_watched = 'YES' if movie['watched'] else 'NO'
        print(
            f"{movie['name']} by {movie['director']} released in {movie['year']}, rating: {movie['rating']}, watched: {movie[is_watched]}")


def prompt_watch_movie():
    name = input("Enter the name of the movie you just finished watching: ")
    database.mark_movie_as_watched(name)


def prompt_delete_movie():
    name = input("Enter the name of the movie you wish to delete: ")
    database.delete_movie(name)


menu()
