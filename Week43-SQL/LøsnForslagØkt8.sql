USE world;

-- Oppgave 1
select sum(SurfaceArea) as Areal
from country
where Continent = 'Asia';

-- Oppgave 2
SELECT avg(Population) AS Snitt
FROM city
WHERE CountryCode = 'DNK';

-- Oppgave 3
SELECT MIN(LifeExpectancy) AS lowest_life_expectancy,
       MAX(LifeExpectancy) AS highest_life_expectancy
FROM country;

-- Oppgave 4
SELECT Region, COUNT(*) AS country_count
FROM country
GROUP BY Region;

-- Oppgave 5
SELECT Region, COUNT(*) AS country_count
FROM country
GROUP BY Region
HAVING COUNT(*) >= 10;

-- Oppgave 6
SELECT Region, COUNT(*) AS country_count
FROM country
WHERE Continent = 'Africa'
GROUP BY Region;

-- Oppgave 7
SELECT co.Name, countrylanguage.Language
FROM country co
INNER JOIN countrylanguage ON co.Code = countrylanguage.CountryCode
WHERE co.Code = 'CAN';

-- Oppgave 8
SELECT co.Name, countrylanguage.Language
FROM country co
INNER JOIN countrylanguage ON co.Code = countrylanguage.CountryCode
WHERE co.Code = 'CAN' AND
    countrylanguage.IsOfficial = 'T';

-- Oppgave 9
SELECT co.Name, countrylanguage.Language
FROM country co
LEFT JOIN countrylanguage ON co.Code = countrylanguage.CountryCode;

-- Oppgave 10
SELECT co.Name, countrylanguage.Language
FROM country co
LEFT JOIN countrylanguage ON co.Code = countrylanguage.CountryCode
WHERE countrylanguage.CountryCode IS NULL;

-- Oppgave 11
SELECT country.Name, countrylanguage.Language
FROM country
JOIN countrylanguage ON country.Code = countrylanguage.CountryCode;

-- Oppgave 12
SELECT country.Code, country.Name,
COUNT(cl.Language) AS language_count
FROM country
LEFT JOIN countrylanguage AS cl ON
country.Code = cl.CountryCode
GROUP BY country.Code, country.Name;

-- Oppgave 13
SELECT SUM(Population) AS Folketall
FROM city
WHERE CountryCode = 'ATA';

SELECT COALESCE(SUM(Population), 0) AS Folketall
FROM city
WHERE CountryCode = 'ATA';

-- Oppgave 14
SELECT AVG(SurfaceArea)
FROM country;

SELECT Name, SurfaceArea
FROM country
WHERE SurfaceArea > (
    SELECT AVG(SurfaceArea)
    FROM country
)
ORDER BY SurfaceArea ASC;
