SELECT 
    utbildningsnamn,
    utbildningsområde,
    --"yh-poäng",
    beslut,
    "utbildningsanordnare administrativ enhet"
    --kommun
FROM table_exer4
WHERE utbildningsnamn LIKE '%Data%';

-- a) Find out how many data engineer programs have been applied and which schools have applied them along
SELECT 
    utbildningsnamn,
    utbildningsområde,
    --"yh-poäng",
    beslut,
    "utbildningsanordnare administrativ enhet",
    kommun
FROM table_exer4
WHERE utbildningsnamn = 'Data Engineer';

--b) Find out number of data engineer programs that got approved.

SELECT 
    COUNT(*) as number_of_approved
FROM table_exer4
WHERE utbildningsnamn = 'Data Engineer' AND beslut= 'Beviljad';

-- c) Count number of approved programs in each of the education categories (utbildningsområde)
SELECT 
    utbildningsområde,
    count(*)
FROM table_exer4
WHERE beslut = 'Beviljad'
GROUP BY utbildningsområde, beslut;

-- --d) Count nubmer of approved programs for each municipality (kommun).
-- SELECT 
--     kommun,
--     count(*)
-- FROM table_exer4
-- WHERE beslut = 'Beviljad'
-- GROUP BY kommun, beslut
-- ORDER BY count DESC;

-- --e) Calculate the percentage of approved programs within each education category.
SELECT 
    utbildningsområde,
    COUNT(CASE WHEN beslut = 'Beviljad' THEN 1 END) AS num_approved,
    COUNT(CASE WHEN beslut = 'Avslag' THEN 1 END) AS num_rejected,
    ROUND(100 * COUNT(CASE WHEN beslut = 'Beviljad' THEN 1 END) / (COUNT(CASE WHEN beslut = 'Beviljad' THEN 1 END) + COUNT(CASE WHEN beslut = 'Avslag' THEN 1 END)), 2) AS percentage_approved
FROM table_exer4
GROUP BY utbildningsområde
ORDER BY percentage_approved;