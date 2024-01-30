DROP TABLE mokytojai

CREATE TABLE mokytojai (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL,
  specialybe VARCHAR(255) NOT NULL,
  nuo_kada_dirba_metais INTEGER
);


INSERT INTO mokytojai (id, vardas, pavarde, specialybe, nuo_kada_dirba_metais)
VALUES (1, 'Petras', 'Petraitis', 'Matematika', 2013),
       (2, 'Ona', 'Onaitė', 'Fizika', 2012),
       (3, 'Marius', 'Marijus', 'Biologija', 2015),
       (4, 'Rasa', 'Rasaitė', 'Anglų kalba', 2011),
       (5, 'Aurimas', 'Aurimaitis', 'Lietuvių kalba', 2018),
       (6, 'Gintare', 'Gintarėlė', 'Istorija', 2020);

SELECT * FROM mokytojai WHERE specialybe = 'Matematika'; 
SELECT * FROM mokytojai WHERE (2024 - nuo_kada_dirba_metais) > 8 AND (2024 - nuo_kada_dirba_metais) > 9;
UPDATE mokytojai SET pavarde = 'Žolienė' WHERE pavarde = 'Rasaitė' AND vardas = 'Rasa';
DELETE FROM mokytojai WHERE id = 4;
