
/* Symmetric Pairs */
SELECT DISTINCT f1.X, f1.Y
FROM Functions f1 JOIN Functions f2 ON f1.X = f2.Y AND f1.Y = f2.X
WHERE f1.X <= f1.Y
GROUP BY f1.X, f1.Y
HAVING COUNT(*) > 1 OR f1.X < f1.Y
ORDER BY f1.X;

/* Placements */
SELECT s.NAME 
FROM STUDENTS s JOIN PACKAGES p ON s.ID = p.ID
JOIN FRIENDS f ON s.ID = f.ID 
JOIN PACKAGES pf ON pf.ID = f.FRIEND_ID WHERE pf.SALARY > p.SALARY ORDER BY pf.SALARY

/* Occupations */

WITH rownumbers AS(
    SELECT NAME, OCCUPATION, ROW_NUMBER() OVER (PARTITION BY OCCUPATION ORDER BY NAME) AS ROW_NUMS FROM OCCUPATIONS)
    
SELECT 
    MAX(CASE WHEN OCCUPATION = 'DOCTOR' THEN NAME END) AS DOCTOR,
    MAX(CASE WHEN OCCUPATION = 'PROFESSOR' THEN NAME END) AS PROFESSOR,
    MAX(CASE WHEN OCCUPATION = 'SINGER' THEN NAME END) AS SINGER,
    MAX(CASE WHEN OCCUPATION = 'ACTOR' THEN NAME END) AS ACTOR
FROM rownumbers GROUP BY ROW_NUMS ORDER BY ROW_NUMS 


/* Interviews */
SELECT con.contest_id, con.hacker_id, con.name, 
SUM(total_submissions) AS ts, 
SUM(total_accepted_submissions) AS tas, 
SUM(total_views) AS tv, 
SUM(total_unique_views) AS tuv 
FROM contests con 
JOIN colleges col ON con.contest_id = col.contest_id 
JOIN challenges cha ON col.college_id = cha.college_id 
LEFT JOIN 
(SELECT challenge_id, SUM(total_views) AS total_views, SUM(total_unique_views) AS total_unique_views FROM view_stats GROUP BY challenge_id ) vs 
ON cha.challenge_id = vs.challenge_id 
LEFT JOIN 
(SELECT challenge_id, SUM(total_submissions) AS total_submissions, SUM(total_accepted_submissions) AS total_accepted_submissions FROM submission_stats GROUP BY challenge_id ) ss 
ON cha.challenge_id = ss.challenge_id 
GROUP BY con.contest_id, con.hacker_id, con.name 
HAVING ts + tas + tv + tuv > 0 
ORDER BY contest_id;




WITH PROJECTGROUPS AS(
SELECT TASK_ID, START_DATE, END_DATE,
 ABS(ROW_NUMBER() OVER (ORDER BY START_DATE) - DATEDIFF(START_DATE, '2015-10-01'))) AS DAYS FROM PROJECTS
