# Using NULL

## 1

```sql
SELECT name
FROM teacher
JOIN dept ON teacher.dept=dept.id;
```

## 2

```sql
SELECT teacher.name, dept.name
FROM teacher
INNER JOIN dept ON (teacher.dept=dept.id)
WHERE teacher.dept IS NOT NULL;
```

## 3

```sql
select teacher.name, dept.name
from teacher
LEFT JOIN dept ON teacher.dept=dept.id;
```

## 4

```sql
select teacher.name, dept.name
from dept
LEFT JOIN teacher ON teacher.dept=dept.id;
```

## 5

```sql
select teacher.name, COALESCE(teacher.mobile, '07986 444 2266')
from teacher;
```

## 6

```sql
select teacher.name, COALESCE(dept.name, 'None')
from teacher
LEFT JOIN dept ON teacher.dept=dept.id;
```

## 7

```sql
SELECT COUNT(teacher.name), COUNT(teacher.mobile)
FROM teacher;
```

## 8

```sql
SELECT dept.name, COUNT(*)
FROM teacher
RIGHT JOIN dept ON teacher.dept=dept.id
GROUP BY dept.name;
```

## 9

```sql
SELECT
  teacher.name,
  CASE WHEN dept.id = 1 OR dept.id = 2
       THEN 'Sci'
       ELSE 'Art'
  END
FROM teacher
LEFT JOIN dept ON teacher.dept=dept.id;
```

## 10

```sql
SELECT
  teacher.name,
  CASE WHEN dept.id = 1 OR dept.id = 2 THEN 'Sci'
       WHEN dept.id = 3 THEN 'Art'
       ELSE 'None'
  END
FROM teacher
LEFT JOIN dept ON teacher.dept=dept.id;
```
