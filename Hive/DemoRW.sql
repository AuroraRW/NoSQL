---a All DVD titles, prices and genres
SELECT dvd_title, price, genre FROM DVDRW

---b All DVD titles and prices sorted by price in descending order
SELECT dvd_title, price FROM DVDRW
ORDER BY price DESC

---c DVD titles and prices for the genre Animation
SELECT dvd_title, price FROM dvdrw
WHERE genre="Animation"

---d All the genres for the DVDs, but only displayed once (not duplicated)
SELECT DISTINCT genre FROM dvdrw

---e The count of the number of genres, including the blank genres
SELECT count(genre) FROM dvdrw

---f The average price of DVDs for each genre
select avg(cast(substr(price,2) as decimal(12,2))) from dvdrw
GROUP BY genre

---g The average price of DVDs, where the average price for that genre is less than (or equal to) $20
SELECT avg(cast(substr(price,2) as decimal(12,2))), genre FROM dvdrw
GROUP BY genre
HAVING avg(cast(substr(price,2) as decimal(12,2))) <=20

---h The list of all DVD titles with all the actors’ names for each title
SELECT dvdrw.dvd_title, actorrw.actor FROM actorrw
INNER JOIN dvdactorrw ON actorrw.actor_id=dvdactorrw.actor_id
JOIN dvdrw ON dvdactorrw.dvdlist_id=dvdrw.id

---i The list of all DVD titles with all the actors’ names for each title where the actor's first name or last name contain "john"
SELECT actorrw.actor, dvdrw.dvd_title FROM actorrw
INNER JOIN dvdactorrw ON actorrw.actor_id=dvdactorrw.actor_id
JOIN dvdrw ON dvdactorrw.dvdlist_id=dvdrw.id
WHERE array_contains(split(actor,','),'john')

---j The list of last names of the actors, with no repeated last names.
SELECT lastname
FROM actorrw LATERAL VIEW explode(array(split(actor,"\,")[1])) actorname AS lastname

---k The list of DVD titles their release dates, where the release date is in the year 2000.
SELECT dvd_title, dvd_releasedate FROM dvdrw
WHERE split(split(dvd_releasedate," ")[0],"/")[2]='2000'

---l combine Action/Adventure and Action/Comedy into one category called Action. 
select genrenumber, genre from(
    select count(1) AS genrenumber, "Action" AS genre 
    From dvdrw
    where (genre = "Action/Adventure" or genre="Comedy")
    union all
    select count(1) AS genrenumber, genre From dvdrw
    group by genre
    having genre != "Action/Adventure" and genre != "Comedy"
) temp sort by genre












