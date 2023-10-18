CREATE TABLE employe(
	id_emp INT NOT NULL,
  	nom VARCHAR(30) NOT NULL,
  	prenom VARCHAR(30) NOT NULL,
  	sexe CHAR(1) NOT NULL,
  	service VARCHAR(30),
  	salaire INT,
  	dtContrat DATE,
  	PRIMARY KEY(id_emp)
);