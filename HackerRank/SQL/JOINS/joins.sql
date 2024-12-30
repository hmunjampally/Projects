
/* POPULATION CENSUS*/
SELECT SUM(city.POPULATION) FROM CITY city JOIN COUNTRY c ON city.COUNTRYCODE = c.CODE WHERE c.CONTINENT = 'ASIA'

SELECT h.HACKER_ID, h.NAME FROM HACKERS_TABLE h JOIN SUBMISSION_TABLE s ON h.HACKER_ID = s.HACKER_ID



/*Harrty potter wand*/
SELECT w.ID, wp.AGE, w.COINS_NEEDED, w.POWER 
FROM WANDS w JOIN WANDS_PROPERTY wp ON w.CODE = wp.CODE 
WHERE wp.IS_EVIL=0 AND 
w.COINS_NEEDED = (SELECT MIN(w1.COINS_NEEDED) FROM WANDS w1 JOIN WANDS_PROPERTY wp1 ON w1.CODE = wp1.CODE 
WHERE wp1.IS_EVIL = 0 AND w1.POWER = w.POWER AND wp1.AGE = wp.AGE) ORDER BY w.POWER DESC, wp.AGE DESC


/* THE REPORT */
SELECT CASE
            WHEN g.GRADE >= 8 THEN s.NAME
            ELSE "NULL"
        END, g.GRADE, s.MARKS
FROM GRADES G JOIN STUDENTS s ON s.MARKS BETWEEN g.MIN_MARK AND g.MAX_MARK 
ORDER BY g.GRADE DESC, 
CASE WHEN g.GRADE >= 8 THEN s.NAME ELSE s.MARKS END ASC



/* TOP COMPETITORS */

SELECT h.HACKER_ID, h.NAME FROM HACKERS h JOIN SUBMISSIONS s ON h.HACKER_ID = s.HACKER_ID 
JOIN CHALLENGES c ON s.CHALLENGE_ID = c.CHALLENGE_ID 
JOIN DIFFICULTY d ON d.DIFFICULTY_LEVEL = c.DIFFICULTY_LEVEL
    WHERE s.SCORE = d.SCORE 
    GROUP BY h.HACKER_ID, h.NAME 
    HAVING COUNT(DISTINCT s.CHALLENGE_ID) > 1 
    ORDER BY COUNT(DISTINCT s.CHALLENGE_ID) DESC, h.HACKER_ID ASC


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


/* Contest Leaderboard */

SELECT h.HACKER_ID, h.NAME, SUM(max_scores.max_score) AS TOTAL FROM 
    Hackers h JOIN (SELECT hacker_id, challenge_id, MAX(score) AS max_score
    FROM Submissions GROUP BY hacker_id, challenge_id) AS max_scores ON h.hacker_id = max_scores.hacker_id
    GROUP BY h.HACKER_ID, h.NAME HAVING TOTAL>0 ORDER BY TOTAL DESC, h.HACKER_ID ASC