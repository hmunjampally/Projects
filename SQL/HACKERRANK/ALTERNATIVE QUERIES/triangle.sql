
/* TRINANGLE DESCENDING ORDER*/
WITH RECURSIVE Pattern AS (
    SELECT 20 AS row_num  -- Start with the maximum number of rows
    UNION ALL
    SELECT row_num - 1
    FROM Pattern
    WHERE row_num > 1
)
SELECT REPEAT('* ', row_num) AS pattern_row
FROM Pattern
ORDER BY row_num DESC;

/* TRINANGLE ASCENDING ORDER*/
WITH RECURSIVE Pattern AS (
    SELECT 1 AS row_num  -- Start with the maximum number of rows
    UNION ALL
    SELECT row_num + 1
    FROM Pattern
    WHERE row_num < 20
)
SELECT REPEAT('* ', row_num) AS pattern_row
FROM Pattern
ORDER BY row_num ASC;


/* PRIME NUMBERS */

WITH RECURSIVE NUMBERS AS (
    SELECT 2 AS nums UNION ALL SELECT nums+1 FROM NUMBERS WHERE nums < 1000),
PrimeCandidates AS (
SELECT nums FROM NUMBERS n1 WHERE NOT EXISTS (
SELECT 1 FROM NUMBERS n2 
WHERE n2.nums < n1.nums AND n2.nums > 1 AND n1.nums % n2.nums = 0))
SELECT GROUP_CONCAT(nums ORDER BY nums SEPARATOR '&') AS primes FROM PrimeCandidates ORDER BY nums

