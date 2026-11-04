-- 4.1
select Name, District, Population, CountryCode
from city
where CountryCode = 'JPN';

-- 4.2 Vi må skrive ''
select Name, Population
from country
where Continent = 'South America';

-- 4.3
select Name, SurfaceArea
from country
where SurfaceArea < 1000;

-- inkl 1000 kvm
select Name, SurfaceArea
from country
where SurfaceArea <= 1000;

-- 5.3
select Name, Population, CountryCode
from city
where Population > 500000
  and (CountryCode = 'BRA'
    or CountryCode = 'ARG')
order by Population asc;


-- Byer i Norge, samt hele navnet Norway
select ci.Name, co.Name
from city as ci
         join country as co on CountryCode = co.Code
where CountryCode = 'NOR';

select Name
from country
where Name like 'Br%';

-- 10.1
select Name, Population
from city
where CountryCode = 'ITA';

-- 10.4
select Name, HeadOfState
from country
where HeadOfState = '';

select Name
from country
where Name like 'D%';