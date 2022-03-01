import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://user1:1234@localhost:5432/user1')
connection = engine.connect()

connection.execute("""create table if not exists musician (
    id serial primary key,
    name varchar(20) not null unique
    );""")

connection.execute("""create table if not exists album (
    id serial primary key,
    name varchar(40) not null unique,
    year_of_issue integer not null
    );""")

connection.execute("""create table if not exists genre (
    id serial primary key,
    name varchar(20) not null unique
    );""")

connection.execute("""create table if not exists GenreMusician (
    genre_id integer references genre(id),
    musician_id integer references musician(id),
    constraint GM primary key (genre_id, musician_id)
    );""")

connection.execute("""create table if not exists MusicianAlbum (
    musician_id integer references musician(id),
    album_id integer references album(id),
    constraint MA primary key (musician_id, album_id)
    );""")

connection.execute("""create table if not exists track (
    id serial primary key,
    album_id integer references album(id),
    name varchar(20) not null unique,
    duration numeric(3,2) not null
    );""")

connection.execute("""create table if not exists compilation (
    id serial primary key,
    name varchar(20) not null unique,
    year_of_issue integer not null
    );""")

connection.execute("""create table if not exists TrackCompilation (
    track_id integer references track(id),
    compilation_id integer references compilation(id),
    constraint TC primary key (track_id, compilation_id)
    );""")

# connection.execute("""drop table musician cascade;""")
# connection.execute("""drop table album cascade;""")
# connection.execute("""drop table genre cascade;""")
# connection.execute("""drop table GenreMusician cascade;""")
# connection.execute("""drop table MusicianAlbum cascade;""")
# connection.execute("""drop table track cascade;""")
# connection.execute("""drop table compilation cascade;""")
# connection.execute("""drop table TrackCompilation cascade;""")
