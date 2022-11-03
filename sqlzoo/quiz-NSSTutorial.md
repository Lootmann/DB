# NSS Tutorial

```
Field               Type
ukprn               varchar(8)
institution         varchar(100)
subject             varchar(60)
level               varchar(50)
question            varchar(10)
A_STRONGLY_DISAGREE int(11)
A_DISAGREE          int(11)
A_NEUTRAL           int(11)
A_AGREE             int(11)
A_STRONGLY_AGREE    int(11)
A_NA                int(11)
CI_MIN              int(11)
score               int(11)
CI_MAX              int(11)
response            int(11)
sample              int(11)
aggregate           char(1)
```

## 1

```sql
SELECT A_STRONGLY_AGREE
  FROM nss
 WHERE question='Q01'
   AND institution='Edinburgh Napier University'
   AND subject='(8) Computer Science'
```

## 2

```sql
SELECT institution, subject
FROM nss
WHERE question='Q15' AND score >= 100;
```

## 3

```sql
SELECT institution,score
  FROM nss
 WHERE question='Q15'
   AND subject='(8) Computer Science'
   AND score <= 50
```

## 4

```sql
SELECT subject, SUM(response)
  FROM nss
 WHERE question='Q22'
   AND subject IN ('(8) Computer Science', '(H) Creative Arts and Design')
group by subject
```

## 5

```sql
SELECT
  subject,
  SUM(A_STRONGLY_AGREE * response / 100)
FROM nss
WHERE
    (question='Q22' AND subject='(8) Computer Science')
  OR
    (question='Q22' AND subject='(H) Creative Arts and Design')
GROUP BY subject
```
