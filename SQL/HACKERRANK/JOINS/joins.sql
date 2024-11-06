
/* POPULATION CENSUS*/
SELECT SUM(city.POPULATION) FROM CITY city JOIN COUNTRY c ON city.COUNTRYCODE = c.CODE WHERE c.CONTINENT = 'ASIA'

SELECT h.HACKER_ID, h.NAME FROM HACKERS_TABLE h JOIN SUBMISSION_TABLE s ON h.HACKER_ID = s.HACKER_ID



/*Harrty potter wand*/
SELECT w.ID, wp.AGE, w.COINS_NEEDED, w.POWER 
FROM WANDS w JOIN WANDS_PROPERTY wp ON w.CODE = wp.CODE 
WHERE wp.IS_EVIL=0 AND 
w.COINS_NEEDED = (SELECT MIN(w1.COINS_NEEDED) FROM WANDS w1 JOIN WANDS_PROPERTY wp1 ON w1.CODE = wp1.CODE 
WHERE wp1.IS_EVIL = 0 AND w1.POWER = w.POWER AND wp1.AGE = wp.AGE) ORDER BY w.POWER DESC, wp.AGE DESC



/*Hackers and challenges*/
WITH ChallengeCounts AS (
    SELECT h.HACKER_ID, h.NAME, COUNT(c.CHALLENGE_ID) AS total_challenges
    FROM HACKERS h
    JOIN CHALLENGES c ON h.HACKER_ID = c.HACKER_ID
    GROUP BY h.HACKER_ID, h.NAME
),
MaxChallenges AS (
    SELECT MAX(total_challenges) AS max_challenges
    FROM ChallengeCounts
),
FilteredResults AS (
    SELECT *
    FROM ChallengeCounts
    WHERE total_challenges = (SELECT max_challenges FROM MaxChallenges)
       OR total_challenges IN (
            SELECT total_challenges
            FROM ChallengeCounts
            GROUP BY total_challenges
            HAVING COUNT(*) = 1
       )
)
SELECT HACKER_ID, NAME, total_challenges
FROM FilteredResults
ORDER BY total_challenges DESC, HACKER_ID;
