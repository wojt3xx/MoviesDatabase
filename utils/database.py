from .db_connection import DatabaseConnection


def create_movies_table():
    with DatabaseConnection('movies.db') as connection:
        cursor = connection.cursor()

        cursor.execute(
            'CREATE TABLE IF NOT EXISTS movies(name text,year integer,director text,rating integer,watched text)')


def add_movie(name, year, director, rating, watched):
    with DatabaseConnection('movies.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO movies VALUES(?, ?, ?, ?, ?)',
                           (name, year, director, rating, watched))


def get_all_movies():
    with DatabaseConnection('movies.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM movies')
        movies_list = [{'name': row[0], 'year': row[1], 'director': row[2],
                        'rating': row[3], 'watched': row[4]} for row in cursor.fetchall()]
    return movies_list


def mark_movie_as_watched(name):
    with DatabaseConnection('movies.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE movies SET watched="True" WHERE name=?', (name,))


def delete_movie(name):
    with DatabaseConnection('movies.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM movies WHERE name=?', (name,))
