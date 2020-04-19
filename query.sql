--Запит 1--

SELECT GamesGenres.genre, COUNT(GamesGenres.genre) AS GamesGenreCount
FROM Games
INNER JOIN GamesGenres
ON Games.gname = GamesGenres.gname
GROUP BY GamesGenres.genre
ORDER BY GamesGenreCount DESC;

--Запит 2--

SELECT GamesPlatforms.platform, round(count(*) / (SELECT count(*) FROM Games ), 2 ) as GamePercent
FROM GamesPlatforms
JOIN Games
ON Games.gname = GamesPlatforms.gname
GROUP BY platform
ORDER BY GamePercent DESC;

--Запит 3--

SElECT release_date, count(gname) AS GameRelease
FROM Games
GROUP BY release_date
ORDER BY release_date;