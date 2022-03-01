import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://user1:1234@localhost:5432/user1')
connection = engine.connect()

connection.execute("""insert into musician(id, name)
    values
    (1, 'Glass Animals'),
    (2, 'Ed Sheeran'),
    (3, 'Muni Long'),
    (4, 'Sebastian Yatra'),
    (5, 'Eric Church'),
    (6, 'Ari Lennox'),
    (7, 'Jessica Darrow'),
    (8, 'Latto');""")

connection.execute("""insert into album(id, name, year_of_issue)
    values
    (1, 'Your Love', 2018),
    (2, 'No.6 Collaborations Project', 2019),
    (3, 'Public Displays Of Affection', 2021),
    (4, 'FANTASIA', 2019),
    (5, 'Heart', 2021),
    (6, 'Grounded', 2020),
    (7, 'Encanto', 2021),
    (8, 'Queen of Da Souf', 2020);""")

connection.execute("""insert into genre(id, name)
    values
    (1, 'indie'),
    (2, 'pop'),
    (3, 'soul'),
    (4, 'country music'),
    (5, 'r&b'),
    (6, 'hip-hop');""")

connection.execute("""insert into compilation(id, name, year_of_issue)
    values
    (1, 'Mad', 2020),
    (2, 'Beautiful', 2019),
    (3, 'Training', 2021),
    (4, 'Art', 2019),
    (5, 'Energetic', 2021),
    (6, 'Mood', 2020),
    (7, 'Sad', 2021),
    (8, 'Dancing', 2020);""")

connection.execute("""insert into track(id, album_id, name, duration)
    values
    (1, 1, 'My Love', 3.54),
    (2, 2, 'Beautiful People', 3.17),
    (3, 2, 'South of the Border', 3.24),
    (4, 2, 'I Dont Care', 3.39),
    (5, 3, 'IMU', 3.08),
    (6, 3, 'No Signal', 2.43),
    (7, 3, 'Just Beginning', 3.30),
    (8, 4, 'Respiro', 1.29),
    (9, 4, 'Vuelve', 3.45),
    (10, 5, 'Heart On Fire', 4.17),
    (11, 5, 'Heart Of The Night', 3.18),
    (12, 6, 'Grounded', 1.29),
    (13, 7, 'Waiting On A Miracle', 2.48),
    (14, 8, 'Muwop', 3.20),
    (15, 8, 'On God', 1.53);""")

connection.execute("""insert into GenreMusician(genre_id, musician_id)
    values
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (6, 7),
    (6, 8);""")

connection.execute("""insert into MusicianAlbum(musician_id, album_id)
    values
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (1, 2);""")

connection.execute("""insert into TrackCompilation(track_id, compilation_id)
    values
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
    (9, 1),
    (10, 2),
    (11, 3),
    (12, 4),
    (13, 5);""")
#
# connection.execute("""DELETE from musician;""")
# connection.execute("""DELETE from album;""")
# connection.execute("""DELETE from genre;""")
# connection.execute("""DELETE from compilation;""")
# connection.execute("""DELETE from track;""")
# connection.execute("""DELETE from GenreMusician;""")
# connection.execute("""DELETE from MusicianAlbum;""")
# connection.execute("""DELETE from TrackCompilation;""")
#
# sel = connection.execute("""SELECT * FROM musician;""").fetchall()
# print(sel)
# sel = connection.execute("""SELECT * FROM album;""").fetchall()
# print(sel)
# sel = connection.execute("""SELECT * FROM genre;""").fetchall()
# print(sel)
# sel = connection.execute("""SELECT * FROM compilation;""").fetchall()
# print(sel)
# sel = connection.execute("""SELECT * FROM track;""").fetchall()
# print(sel)
# sel = connection.execute("""SELECT * FROM GenreMusician;""").fetchall()
# print(sel)
# sel = connection.execute("""SELECT * FROM MusicianAlbum;""").fetchall()
# print(sel)
# sel = connection.execute("""SELECT * FROM TrackCompilation;""").fetchall()
# print(sel)