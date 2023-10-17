create table employe(
	id_emp int not null,
  	nom varchar(30) not null,
  	prenom varchar(30) not null,
  	sexe char(1) not null,
  	service varchar(30),
  	salaire int,
  	dtContrat date,
  	primary key(id_emp)
);