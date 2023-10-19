INSERT INTO genre (type) VALUES
('Action'),
('Comédie'),
('Science-fiction'),
('Drame'),
('Horreur'),
('Romance'),
('Aventure'),
('Documentaire'),
('Fantaisie'),
('Mystère');

INSERT INTO note (evaluation, commentaire) VALUES
(4.5, 'Excellent film !'),
(3.0, 'Un bon livre.'),
(2.5, 'J''ai vu la vidéo, c''était correct.'),
(4.0, 'Très bon acteur.'),
(3.5, 'Une aventure captivante.'),
(1.5, 'Ce film était effrayant.'),
(4.0, 'Une belle histoire d''amour.'),
(4.5, 'Un documentaire informatif.'),
(2.0, 'Pas vraiment fan de ce film.'),
(3.5, 'Un mystère intrigant.');

INSERT INTO langue (audio, sous_titre, ecriture) VALUES
('Anglais', 'Français', 'Anglais'),
('Anglais', 'Espagnol', 'Espagnol'),
('Français', 'Anglais', 'Anglais'),
('Espagnol', 'Espagnol', 'Espagnol'),
('Anglais', 'Anglais', 'Anglais');

INSERT INTO film (titre, genre_id, note_id, sortie, langue_id, description) VALUES
('Les Misérables', 1, 1, '2020-05-15', 1, 'Une adaptation du célèbre roman de Victor Hugo.'),
('Inception', 3, 2, '2010-07-16', 1, 'Un film de science-fiction captivant réalisé par Christopher Nolan.'),
('La La Land', 6, 7, '2016-12-09', 2, 'Une comédie musicale romantique.'),
('Le Seigneur des Anneaux : La Communauté de l''Anneau', 9, 3, '2001-12-19', 1, 'Un film d''aventure épique basé sur le roman de J.R.R. Tolkien.'),
('Shining', 4, 5, '1980-05-23', 1, 'Un film d''horreur de Stanley Kubrick basé sur le roman de Stephen King.');

INSERT INTO video (titre, genre_id, note_id, sortie, langue_id, description) VALUES
('Le Roi Lion', 7, 1, '2019-07-19', 1, 'Un film d''animation classique de Disney.'),
('Jurassic Park', 1, 2, '1993-06-11', 1, 'Un film de dinosaures passionnant réalisé par Steven Spielberg.'),
('Le Loup de Wall Street', 6, 8, '2013-12-25', 3, 'Un film basé sur les mémoires de Jordan Belfort.'),
('Gladiator', 9, 7, '2000-05-05', 1, 'Un épique film historique réalisé par Ridley Scott.'),
('Pirates des Caraïbes : La Malédiction du Black Pearl', 7, 3, '2003-07-09', 4, 'Un film d''aventure avec Johnny Depp dans le rôle de Jack Sparrow.');

INSERT INTO musique (titre, genre_id, note_id, sortie, langue_id, description) VALUES
('Bohemian Rhapsody', 8, 2, '1975-10-31', 1, 'Une chanson emblématique de Queen.'),
('Imagine', 6, 7, '1971-10-11', 1, 'Une chanson intemporelle de John Lennon.'),
('Billie Jean', 5, 4, '1983-01-02', 2, 'Un hit de Michael Jackson.'),
('Hotel California', 3, 6, '1976-12-08', 5, 'Un classique des Eagles.'),
('Smells Like Teen Spirit', 1, 10, '1991-09-10', 1, 'Une chanson emblématique de Nirvana.');

INSERT INTO livre (titre, genre_id, note_id, sortie, langue_id, description) VALUES
('Le Seigneur des Anneaux', 9, 1, '1954-07-29', 1, 'La trilogie épique de J.R.R. Tolkien.'),
('Harry Potter à l''École des Sorciers', 6, 5, '1997-06-26', 1, 'Le premier livre de la série Harry Potter de J.K. Rowling.'),
('1984', 4, 3, '1949-06-08', 1, 'Un roman dystopique de George Orwell.'),
('Le Petit Prince', 6, 6, '1943-04-06', 1, 'Un conte philosophique d''Antoine de Saint-Exupéry.'),
('Orgueil et Préjugés', 10, 8, '1813-01-28', 1, 'Un classique de Jane Austen.');

INSERT INTO assignation (personne_id, media_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

INSERT INTO personne (nom, prenom, role) VALUES
('Smith', 'John', 'Acteur'),
('Johnson', 'Emily', 'Auteur'),
('Brown', 'Michael', 'Réalisateur'),
('Davis', 'Emma', 'Chanteur'),
('Wilson', 'Sophia', 'Acteur'),
('Martinez', 'Daniel', 'Chanteur'),
('Jones', 'Olivia', 'Réalisateur'),
('Garcia', 'Liam', 'Acteur'),
('Miller', 'Ava', 'Auteur'),
('Taylor', 'Noah', 'Réalisateur');