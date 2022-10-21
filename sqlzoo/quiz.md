## SUM and COUNT Quiz

```
name        region      area    population  gdp
--------------------------------------------------------
Afghanistan South Asia  652225  26000000
Albania     Europe      28728   3200000     6656000000
Algeria     Middle East 2400000 32900000    75012000000
Andorra     Europe      468     64000
```

1. Select the statement that shows the sum of population of all countries in 'Europe'

```sql
SELECT SUM(population)
FROM bbc
WHERE region = 'Europe'
;
```

2. Select the statement that shows the number of countries with population smaller than 150000

```sql
SELECT COUNT(name)
FROM bbc
WHERE population < 150000
;
```

4. Select the result that would be obtained from the following code:

```sql
SELECT region, SUM(area)
  FROM bbc
 WHERE SUM(area) > 15000000
 GROUP BY region
```

5. Select the statement that shows the average population of 'Poland', 'Germany' and 'Denmark'

```sql
SELECT AVG(population)
  FROM bbc
 WHERE name IN ('Poland', 'Germany', 'Denmark');
```

6. Select the statement that shows the medium population density of each region

```sql
SELECT region,AVG()
  FROM bbc
GROUP BY region
```

7. Select the statement that shows the name and population density of the country with the largest population

```sql
SELECT name, population/area AS density
  FROM bbc
 WHERE population = (
    SELECT MAX(population)
    FROM bbc
 );
```

8. Pick the result that would be obtained from the following code:

```sql
SELECT region, SUM(area)
  FROM bbc
 GROUP BY region
HAVING SUM(area) <= 20000000
```
