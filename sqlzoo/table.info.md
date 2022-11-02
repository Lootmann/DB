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

## JOIN

```
game
  id: 1001
  mdate: 8 June 2012
  stadium: National Stadium
  team1: POL
  team2: GRE

goal
  matchid: 1001
  teamid: POL
  player: name
  gtime: 17

eteam
  id: POL
  teamname: poland
  coach: name
```

## 6.More JOIN

```sql
movie
  id
  title
  yr
  director
  budget
  gross

actor
  id
  name

casting
  movieid
  actorid
  ord
```

## 7. Using NULL

```sql
teacher
  id
  dept(dept.id)
  name
  phone
  mobile

dept
  id
  name
```

## NSS_Tutorial

```
               ukprn 10003861
         institution Leeds Metropolitan University
             subject (E) Mass Communications and Documentation
               level First degree
            question Q15
 A_STRONGLY_DISAGREE 1
          A_DISAGREE 8
           A_NEUTRAL 8
             A_AGREE 61
    A_STRONGLY_AGREE 22
                A_NA 0
              CI_MIN 74
               score 83
              CI_MAX 89
            response 148
              sample 197

```
