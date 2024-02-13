-- list rows without a name value
SELECT score, name != NULL FROM second_table ORDER BY score DESC;
