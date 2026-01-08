/*
Enter your query here.
https://www.hackerrank.com/challenges/weather-observation-station-11/problem?isFullScreen=true
*/
SELECT DISTINCT CITY
From STATION
WHERE (LOWER(CITY) NOT LIKE 'a%' AND LOWER(CITY) NOT LIKE 'e%' AND LOWER(CITY) NOT LIKE 'i%' AND LOWER(CITY) NOT LIKE 'o%' AND LOWER(CITY) NOT LIKE 'u%') OR (LOWER(CITY) NOT LIKE '%a' AND LOWER(CITY) NOT LIKE '%e' AND LOWER(CITY) NOT LIKE '%i' AND LOWER(CITY) NOT LIKE '%o' AND LOWER(CITY) NOT LIKE '%u')
