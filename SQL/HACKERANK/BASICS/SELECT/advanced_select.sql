

/* TABLE TRIANGLES */

SELECT CASE 
            WHEN A=B AND B=C THEN 'Equilateral' 
            WHEN A+B>C AND A+C>B AND B+C>A THEN 
                CASE 
                    WHEN A=B OR B=C OR A=C THEN 'Isosceles' 
                    ELSE 'Scalene' 
                END 
            ELSE 'Not A Triangle' 
        END 
FROM TRIANGLES;



/* TABLE OCCUPATION */
SELECT CONCAT(NAME, '(', LEFT(OCCUPATION,1), ')') FROM OCCUPATIONS ORDER BY NAME ASC;

SELECT CONCAT('There are a total of ', COUNT(*), ' ', LOWER(OCCUPATION), 's.') FROM OCCUPATIONS GROUP BY OCCUPATION ORDER BY COUNT(*) ASC;



/* TABLE BST */

SELECT N, CASE
            WHEN P IS NULL THEN 'Root'
            WHEN N IS NOT NULL AND N IN (SELECT  P FROM BST) THEN 'Inner'
            ELSE 'Leaf'
        END
FROM BST ORDER BY N ASC