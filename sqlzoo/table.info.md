# Tutorial

## Grammer

```sql
-- WHERE and GROUP BY.
-- The WHERE filter takes place before the aggregating function.
SELECT continent, COUNT(name)
  FROM world
 WHERE population>200000000
 GROUP BY continent
```

```sql
-- GROUP BY and HAVING.
-- The HAVING clause is tested after the GROUP BY.
-- You can test the aggregated values with a HAVING clause.
SELECT continent, SUM(population)
  FROM world
 GROUP BY continent
HAVING SUM(population)>500000000
```

## 1. SELECT basics

## 2. SELECT from worlds

Table : **world**

```sql
name        varchar(50)
continent   varchar(60)
area        decimal(10,0)
population  decimal(11,0)
gdp         decimal(14,0)
capital     varchar(60)
tld         varchar(5)
flag        varchar(255)
```

## 3. SELECT from Nobel Tutorial

```sql
yr
subject
winner
```

## 4. SELECT within SELECT Tutorial

```sql:world
name       varchar(50)
continent  varchar(60)
area       Decimal
population Decimal
gdp        Decimal
```

## 5. SUM and COUNT

```sql
name
continent
area
population
gdp
```
