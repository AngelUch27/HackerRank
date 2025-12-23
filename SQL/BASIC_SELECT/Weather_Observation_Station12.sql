/*
Enter your query here.\
https://www.hackerrank.com/challenges/weather-observation-station-12/problem?isFullScreen=true
*/
SELECT DISTINCT CITY
FROM STATION
WHERE (LOWER(CITY) NOT LIKE 'a%' AND LOWER(CITY) NOT LIKE 'e%' AND LOWER(CITY) NOT LIKE 'i%' AND LOWER(CITY) NOT LIKE 'o%' AND LOWER(CITY) NOT LIKE 'u%') AND  (LOWER(CITY) NOT LIKE '%a' AND LOWER(CITY) NOT LIKE '%e' AND LOWER(CITY) NOT LIKE '%i' AND LOWER(CITY) NOT LIKE '%o' AND LOWER(CITY) NOT LIKE '%u')
