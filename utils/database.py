import sqlite3


def create_movies_table():
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS movies(name text,year integer,director text,rating integer,watched text)')

    connection.commit()
    connection.close()


def add_movie(name, year, director, rating, watched):
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    try:
        cursor.execute('INSERT INTO movies VALUES(?, ?, ?, ?, ?)',
                       (name, year, director, rating, watched))
    except:
        print("Could not add the book.")

    connection.commit()
    connection.close()


def get_all_movies():
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM movies')
    movies_list = [{'name': row[0], 'year': row[1], 'director': row[2],
                    'rating': row[3], 'watched': row[4]} for row in cursor.fetchall()]

    connection.close()

    return movies_list


def mark_movie_as_watched(name):
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE movies SET watched="True" WHERE name=?', (name,))

    connection.commit()
    connection.close()


def delete_movie(name):
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM movies WHERE name=?', (name,))

    connection.commit()
    connection.close()
