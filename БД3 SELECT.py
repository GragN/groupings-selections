import sqlalchemy
engine = sqlalchemy.create_engine('postgresql://user1:1234@localhost:5432/user1')
connection = engine.connect()

sel = connection.execute("""select name, count(musician_id) from genre g
    join GenreMusician gm on g.id = gm.genre_id
    group by name;""").fetchall()
print(sel)

sel = connection.execute("""select a.name, count(t.name) from album a
    join track t on a.id = t.album_id
    where year_of_issue between 2019 and 2020
    group by a.name;""").fetchall()
print(sel)

sel = connection.execute("""select a.name, round(avg(t.duration), 2) from album a
    join track t on a.id = t.album_id
    group by a.name;""").fetchall()
print(sel)

sel = connection.execute("""select a.year_of_issue, m.name from album a
    join MusicianAlbum ma on a.id = ma.album_id
    join musician m on m.id = ma.musician_id
    where m.name not in (select m.name from musician m
    join MusicianAlbum ma on m.id = ma.musician_id
    join album a on a.id = ma.album_id
    where year_of_issue = 2020)
    ;""").fetchall()
print(sel)

sel = connection.execute("""select c.name, m.name from compilation c
    join TrackCompilation tc on c.id = tc.compilation_id
    join track t on t.id = tc.track_id
    join album a on a.id = t.album_id
    join MusicianAlbum ma on a.id = ma.album_id
    join musician m on m.id = ma.musician_id
    where m.name = 'Ed Sheeran';""").fetchall()
print(sel)

sel = connection.execute("""select a.name from album a
    join MusicianAlbum ma on a.id = ma.album_id
    join musician m on m.id = ma.musician_id
    join GenreMusician gm on gm.musician_id = m.id
    join genre g on g.id = gm.genre_id
    group by a.name
    having count(g.name) >= 2;""").fetchall()
print(sel)

sel = connection.execute("""select t.name from track t
    left join TrackCompilation tc on t.id = tc.track_id
    left join compilation c on c.id = tc.compilation_id
    where tc.compilation_id is null
    ;""").fetchall()
print(sel)

sel = connection.execute("""select m.name from musician m
    join MusicianAlbum ma on m.id = ma.musician_id
    join album a on a.id = ma.album_id
    join track t on a.id = t.album_id
    where t.duration = (select min(duration) from track)
    ;""").fetchall()
print(sel)

sel = connection.execute("""select distinct a.name from album as a
    left join track as t on t.album_id = a.id
    where t.album_id in (select album_id from track
    group by album_id
    having count(id) = (select count(id) from track
    group by album_id
    order by count
    limit 1))
    order by a.name;""").fetchall()
print(sel)
