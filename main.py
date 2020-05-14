import cx_Oracle

username = "LAPLAS_DB"
password = "laplas228"
database = "localhost/xe"

connection = cx_Oracle.connect(username, password, database)

queryGenres = """
    SELECT GamesGenres.genre, COUNT(GamesGenres.genre) AS GamesGenreCount
    FROM Games
    INNER JOIN GamesGenres
    ON Games.gname = GamesGenres.gname
    GROUP BY GamesGenres.genre
    ORDER BY GamesGenreCount DESC
"""

queryPlatforms = """
    SELECT GamesPlatforms.platform, round(count(*) / (SELECT count(*) FROM Games ), 2 ) as GamePercent
    FROM GamesPlatforms
    JOIN Games
    ON Games.gname = GamesPlatforms.gname
    GROUP BY platform
    ORDER BY GamePercent DESC
"""

queryRelease = """
    SElECT release_date, count(gname) AS GameRelease
    FROM Games
    GROUP BY release_date
    ORDER BY release_date
"""

cursor = connection.cursor()

cursor.execute(queryGenres)

ResultGenres = cursor.fetchall()
print("Query 1\n")
print("{:20}|{}".format("GameGenres", "Total"))
print("--------------------------------------")
for row in ResultGenres:
    print("{:20}|{:5}".format(row[0], row[1]))
print("\n")

cursor.execute(queryPlatforms)

ResultPlatforms = cursor.fetchall()
print("Query 2\n")
print("{:<30}|{}".format('GamePlatforms', 'Percent'))
print("--------------------------------------")
for row in ResultPlatforms:
    print("{:<30}|{}".format(*row))


cursor.execute(queryRelease)

ResultRelease = cursor.fetchall()
print("Query 3\n")
print("{:<16}|{}".format('Release_date', 'GameRelease'))
print("--------------------------------------")
for row in ResultRelease:
    print("{:<16}|{}".format(*row))

cursor.close()
connection.close()
