CREATE TABLE `personne` (
  `id` integer PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nom` varchar(64) NOT NULL,
  `prenom` varchar(64) NOT NULL,
  `role` varchar(64) NOT NULL COMMENT 'Chanteur, auteur, réalisateur ou acteur.'
);

CREATE TABLE `genre` (
  `id` integer PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `type` varchar(64) NOT NULL
);

CREATE TABLE `note` (
  `id` integer PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `evaluation` double NOT NULL DEFAULT 0 COMMENT 'Une note de 0 jusqu\'à 5.',
  `commentaire` text DEFAULT NULL COMMENT 'Contient un commentaire par rapport au média.'
);

CREATE TABLE `langue` (
  `id` integer PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `audio` varchar(64) DEFAULT NULL,
  `sous_titre` varchar(64) DEFAULT NULL,
  `ecriture` varchar(64) DEFAULT NULL
);

CREATE TABLE `assignation` (
  `personne_id` integer NOT NULL COMMENT 'Référence à une personne.',
  `media_id` integer NOT NULL COMMENT 'Référence à un média.',
  PRIMARY KEY (`personne_id`, `media_id`)
);

CREATE TABLE `film` (
  `id` integer PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `titre` varchar(128) NOT NULL,
  `genre_id` integer NOT NULL COMMENT 'Référence au genre.',
  `note_id` integer NOT NULL COMMENT 'Référence à la note.',
  `sortie` date NOT NULL,
  `langue_id` integer NOT NULL COMMENT 'Référence à la langue.',
  `description` text DEFAULT NULL
);

CREATE TABLE `video` (
  `id` integer PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `titre` varchar(128) NOT NULL,
  `genre_id` integer NOT NULL COMMENT 'Référence au genre.',
  `note_id` integer NOT NULL COMMENT 'Référence à la note.',
  `sortie` date NOT NULL,
  `langue_id` integer NOT NULL COMMENT 'Référence à la langue.',
  `description` text DEFAULT NULL
);

CREATE TABLE `musique` (
  `id` integer PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `titre` varchar(128) NOT NULL,
  `genre_id` integer NOT NULL COMMENT 'Référence au genre.',
  `note_id` integer NOT NULL COMMENT 'Référence à la note.',
  `sortie` date NOT NULL,
  `langue_id` integer NOT NULL COMMENT 'Référence à la langue.',
  `description` text DEFAULT NULL
);

CREATE TABLE `livre` (
  `id` integer PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `titre` varchar(128) NOT NULL,
  `genre_id` integer NOT NULL COMMENT 'Référence au genre.',
  `note_id` integer NOT NULL COMMENT 'Référence à la note.',
  `sortie` date NOT NULL,
  `langue_id` integer NOT NULL COMMENT 'Référence à la langue.',
  `description` text DEFAULT NULL
);

ALTER TABLE `personne` COMMENT = 'Contient l\'ensemble des personnes.';

ALTER TABLE `genre` COMMENT = 'Contient l\'ensemble des genres sur chaque média.';

ALTER TABLE `note` COMMENT = 'Contient l\'ensemble des commentaires et des évaluations sur chaque média.';

ALTER TABLE `langue` COMMENT = 'Contient les langues employées par les médias.';

ALTER TABLE `assignation` COMMENT = 'Permet de lier chaque personne à chaque film.';

ALTER TABLE `film` COMMENT = 'Référence chaque film.';

ALTER TABLE `video` COMMENT = 'Référence chaque vidéo.';

ALTER TABLE `musique` COMMENT = 'Référence chaque musique.';

ALTER TABLE `livre` COMMENT = 'Référence chaque livre.';

ALTER TABLE `personne` ADD FOREIGN KEY (`id`) REFERENCES `assignation` (`personne_id`) ON DELETE CASCADE;

ALTER TABLE `assignation` ADD FOREIGN KEY (`media_id`) REFERENCES `video` (`id`) ON DELETE CASCADE;

ALTER TABLE `assignation` ADD FOREIGN KEY (`media_id`) REFERENCES `film` (`id`) ON DELETE CASCADE;

ALTER TABLE `assignation` ADD FOREIGN KEY (`media_id`) REFERENCES `musique` (`id`) ON DELETE CASCADE;

ALTER TABLE `assignation` ADD FOREIGN KEY (`media_id`) REFERENCES `livre` (`id`) ON DELETE CASCADE;

ALTER TABLE `video` ADD FOREIGN KEY (`genre_id`) REFERENCES `genre` (`id`) ON DELETE CASCADE;

ALTER TABLE `film` ADD FOREIGN KEY (`genre_id`) REFERENCES `genre` (`id`) ON DELETE CASCADE;

ALTER TABLE `musique` ADD FOREIGN KEY (`genre_id`) REFERENCES `genre` (`id`) ON DELETE CASCADE;

ALTER TABLE `livre` ADD FOREIGN KEY (`genre_id`) REFERENCES `genre` (`id`) ON DELETE CASCADE;

ALTER TABLE `video` ADD FOREIGN KEY (`note_id`) REFERENCES `note` (`id`) ON DELETE CASCADE;

ALTER TABLE `film` ADD FOREIGN KEY (`note_id`) REFERENCES `note` (`id`) ON DELETE CASCADE;

ALTER TABLE `musique` ADD FOREIGN KEY (`note_id`) REFERENCES `note` (`id`) ON DELETE CASCADE;

ALTER TABLE `livre` ADD FOREIGN KEY (`note_id`) REFERENCES `note` (`id`) ON DELETE CASCADE;

ALTER TABLE `video` ADD FOREIGN KEY (`langue_id`) REFERENCES `langue` (`id`) ON DELETE CASCADE;

ALTER TABLE `film` ADD FOREIGN KEY (`langue_id`) REFERENCES `langue` (`id`) ON DELETE CASCADE;

ALTER TABLE `musique` ADD FOREIGN KEY (`langue_id`) REFERENCES `langue` (`id`) ON DELETE CASCADE;

ALTER TABLE `livre` ADD FOREIGN KEY (`langue_id`) REFERENCES `langue` (`id`) ON DELETE CASCADE;
