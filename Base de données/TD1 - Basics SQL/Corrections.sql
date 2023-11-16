DROP TABLE employe;
DROP TABLE region;
DROP TABLE dept;

-- ===================
-- 2. Créer la table EMPLOYE
-- ===================
CREATE TABLE employe (
 id_emp			INTEGER			NOT NULL	PRIMARY KEY,
 nom			VARCHAR(30)		NOT NULL,
 prenom			VARCHAR(30)		NOT NULL,
 sexe			CHAR(1)			NOT NULL,
 service		VARCHAR(30)		NULL,
 salaire		INTEGER			NULL,
 dateContrat	DATE			NULL);
 

-- ===================
-- 3. Insérer des données dans la table EMPLOYE
-- ===================
-- Oracle / PostgreSQL
INSERT INTO employe VALUES (1, 'Dupont', 'Robert', 'M', 'Marketing', 20000, to_date('21-03-2010','dd-mm-yyyy'));
INSERT INTO employe VALUES (2, 'Dupont', 'Aline', 'F', 'Communication', 8500, to_date('11-11-2013','dd-mm-yyyy'));
INSERT INTO employe VALUES (3, 'Durand', 'Laurence', 'F', 'Marketing', 14000, to_date('02-01-1996','dd-mm-yyyy'));
INSERT INTO employe VALUES (4, 'Lejeune', 'Sylvie', 'F', 'Marketing', 21500, to_date('02-09-2018','dd-mm-yyyy'));
INSERT INTO employe VALUES (5, 'Lefort', 'Max', 'M', NULL, 12000, to_date('11-09-2005','dd-mm-yyyy'));

-- MySQL / SQL Server / SQLite
INSERT INTO employe VALUES (1, 'Dupont', 'Robert', 'M', 'Marketing', 20000, '2010-03-21');
INSERT INTO employe VALUES (2, 'Dupont', 'Aline', 'F', 'Communication', 8500, '2013-11-11');
INSERT INTO employe VALUES (3, 'Durand', 'Laurence', 'F', 'Marketing', 14000, '1996-01-02');
INSERT INTO employe VALUES (4, 'Lejeune', 'Sylvie', 'F', 'Marketing', 21500, '2018-09-02');
INSERT INTO employe VALUES (5, 'Lefort', 'Max', 'M', NULL, 12000, '2005-09-11');


-- ===================
-- 4. Ecrire les requêtes qui répondent aux questions suivantes
-- ===================
-- 1. Sélectionnez le nom et le prénom de l'employé masculin qui gagne plus de 15000.
SELECT nom, prenom
  FROM employe
 WHERE sexe = 'M' AND salaire > 15000;

-- 2. Sélectionnez le prénom des 3 employés qui gagnent le moins
SELECT prenom, salaire
  FROM employe
 ORDER BY salaire ASC
 FETCH FIRST 3 ROWS ONLY;
 -- LIMIT 1;

-- 3. Sélectionnez le plus petit salaire aliasé en salaireMin
SELECT min(salaire) salaireMin
  FROM employe
 ORDER BY salaire

-- 4. Sélectionnez les 4 noms différents des employés, triés par nom ascendant
SELECT DISTINCT(nom)
  FROM employe
 ORDER BY nom;

-- 5. Sélectionnez le salaire de l'employé qui n'a pas de service
SELECT salaire
  FROM employe
 WHERE service IS NULL;

-- 6. Sélectionnez les noms et prénoms des employés triés par ancienneté, du plus ancien au plus récemment embauché
SELECT nom, prenom
  FROM employe
 ORDER BY dateContrat ASC;

-- 7. Sélectionnez les noms et prénoms des employées du service Marketing, triés par nom, puis par prénom
SELECT nom, prenom
  FROM employe
 WHERE service = 'Marketing'
 ORDER BY 1, 2;

-- 8. Sélectionnez le prénom et le nom de l'employé féminin dont le prénom commence par un S
SELECT prenom, nom, sexe
  FROM employe
 WHERE sexe = 'F'
   AND prenom like 'S%';

-- 9. Sélectionnez le service de l'employé qui gagne 8500
SELECT service
  FROM employe
 WHERE salaire = 8500;

-- 10. Sélectionnez la moyenne des salaires par service
SELECT service, AVG(salaire)
  FROM employe
 GROUP BY service;

-- 11. Sélectionnez les services dont la moyenne des salaires est supérieure à 15000
SELECT service, AVG(salaire)
  FROM employe
 GROUP BY service
HAVING AVG(salaire) > 15000;

-- 12. Mettez à jour la table en augmentant de 10% tous les salaires des employés dont l’ancienneté est supérieure à 12 ans
UPDATE employe
   SET salaire = salaire * 1.05
 WHERE dateContrat <= current_date - (365*12);
 

-- ===================
-- 5. Ajouter les tables REGION et DEPT
-- ===================
CREATE TABLE region (
 id_reg			INTEGER			NOT NULL	PRIMARY KEY,
 region			VARCHAR(30)		NOT NULL
);

CREATE TABLE dept (
 id_dept		INTEGER			NOT NULL	PRIMARY KEY,
 dept			VARCHAR(30)		NOT NULL,
 id_reg			INTEGER			NOT NULL,
 CONSTRAINT FK_dept_reg FOREIGN KEY (id_reg) REFERENCES region(id_reg)
);


-- ===================
-- 6. Ajouter la contrainte correspondant au fait qu’un employé ne peut habiter que dans un seul département
-- ===================
ALTER TABLE employe ADD id_dept INTEGER;
ALTER TABLE employe ADD CONSTRAINT fk_emp_dept FOREIGN KEY (id_dept) REFERENCES dept(id_dept);


-- ===================
-- 7. Insérer les données de la région "IDF" uniquement (id_reg = 7), avec ses départements (75, 77, 91, 92, 93, 94, 95)
-- ===================
INSERT INTO region VALUES (7, 'IDF');

INSERT INTO dept VALUES (75, 'Paris', 7);
INSERT INTO dept VALUES (77, 'Seine-et-Marne', 7);
INSERT INTO dept VALUES (78, 'Yvelines', 7);
INSERT INTO dept VALUES (91, 'Essonne', 7);
INSERT INTO dept VALUES (92, 'Hauts-de-Seine', 7);
INSERT INTO dept VALUES (93, 'Seine-Saint-Denis', 7);
INSERT INTO dept VALUES (94, 'Val-de-Marne', 7);
INSERT INTO dept VALUES (95, 'Val-d''oise', 7);


-- ===================
-- 8. Insérer les données de la région "IDF" uniquement (id_reg = 7), avec ses départements (75, 77, 91, 92, 93, 94, 95)
-- ===================
UPDATE employe SET id_dept = 75 WHERE id_emp = 1;
UPDATE employe SET id_dept = 77 WHERE id_emp IN (2,5);
UPDATE employe SET id_dept = 94 WHERE id_emp = 3;


-- ===================
-- 9. Ecrivez les requêtes SQL qui répondent aux questions suivantes :
-- ===================
-- 1. Sélectionnez le nom, le prénom de chaque employé, avec le nom du département et de la région où ils habitent
SELECT nom, prenom, dept, region
  FROM employe e, dept d, region r
 WHERE e.id_dept = d.id_dept
   AND d.id_reg  = r.id_reg;

-- 2. Sélectionnez par département le nombre total d’employés qui y habitent
SELECT dept, count(*)
  FROM employe e, dept d
 WHERE e.id_dept = d.id_dept
 GROUP BY dept;

-- 3. Calculer la moyenne des salaires par service, dans chaque département
SELECT dept, service, AVG(salaire)
  FROM employe e, dept d
 WHERE e.id_dept = d.id_dept
 GROUP BY dept, service;

-- 4. Sélectionnez les départements pour lesquels le meilleur salaire dépasse 15000
SELECT dept, max(salaire)
  FROM employe e, dept d
 WHERE e.id_dept = d.id_dept
 GROUP BY dept
HAVING max(salaire)>=15000;


-- ===================
-- 10. Jointures
-- ===================
-- INNER JOIN
SELECT *
  FROM employe e INNER JOIN dept d ON e.id_dept = d.id_dept;

-- CROSS JOIN
SELECT *
  FROM employe CROSS JOIN dept;

-- LEFT JOIN
SELECT *
  FROM employe e LEFT JOIN dept d ON e.id_dept = d.id_dept;

-- RIGHT JOIN
SELECT *
  FROM employe e RIGHT JOIN dept d ON e.id_dept = d.id_dept;

-- FULL JOIN
SELECT *
  FROM employe e FULL JOIN dept d ON e.id_dept = d.id_dept;

-- SELF JOIN
SELECT e1.id_emp, e1.nom, e1.prenom, e1.salaire, e2.id_emp, e2.nom, e2.prenom, e2.salaire
  FROM employe e1, employe e2
 WHERE e1.salaire > e2.salaire;

-- UNION
SELECT nom, prenom, salaire, id_dept FROM employe WHERE salaire > 12000
UNION
SELECT nom, prenom, salaire, id_dept FROM employe WHERE id_dept = 77;

-- UNION ALL
SELECT nom, prenom, salaire, id_dept FROM employe WHERE salaire > 12000
UNION ALL
SELECT nom, prenom, salaire, id_dept FROM employe WHERE id_dept = 77;

-- INTERSECT
SELECT nom, prenom, salaire, id_dept FROM employe WHERE salaire > 12000
INTERSECT
SELECT nom, prenom, salaire, id_dept FROM employe WHERE id_dept = 77;

-- MINUS
SELECT nom, prenom, salaire, id_dept FROM employe WHERE salaire > 12000
MINUS
SELECT nom, prenom, salaire, id_dept FROM employe WHERE id_dept = 77;
