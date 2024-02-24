SELECT name FROM records WHERE supervisor="Oliver Warbucks";

SELECT * FROM records WHERE name=supervisor;

SELECT name FROM records WHERE salary>50000;

SELECT b.day, b.time FROM records AS a, meetings AS b 
        WHERE a.supervisor="Oliver Warbucks" AND a.division=b.division;

SELECT a.name FROM records AS a, records AS b 
        WHERE a.supervisor=b.name AND a.division!=b.division;
    
SELECT b.name FROM records AS a, records AS b 
        WHERE a.supervisor=b.name AND a.name!=a.supervisor AND b.name!=b.supervisor GROUP BY b.name;

SELECT b.name, SUM(a.salary) FROM records AS a, records AS b 
        WHERE a.supervisor=b.name GROUP BY b.name;

SELECT COUNT(DISTINCT b.day) FROM records AS a, meetings AS b 
        WHERE a.division=b.division GROUP BY b.day HAVING COUNT(a.name)<5;

SELECT a.division, a.name, b.name FROM records AS a, records AS b 
        WHERE a.division=b.division AND a.name<b.name AND a.salary+b.salary<100000;