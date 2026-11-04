select city.name as 'By', city.Population as 'Folketall', country.Name as 'Land', country.Continent as 'Kontinent'
from city
join country on city.CountryCode = country.Code
where CountryCode = 'ITA'
order by city.Population asc;
