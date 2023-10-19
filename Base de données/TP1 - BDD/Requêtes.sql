# Sélectionner toutes les informations sur un film.
SELECT
    f.id AS film_id,
    f.titre AS titre_film,
    g.type AS genre,
    n.evaluation AS evaluation_moyenne,
    n.commentaire AS commentaire,
    l.audio AS langue_audio,
    l.sous_titre AS langue_sous_titre,
    l.ecriture AS langue_ecriture,
    f.sortie AS date_sortie,
    f.description AS description_film,
    GROUP_CONCAT(CONCAT(p.prenom, ' ', p.nom, ' (', p.role, ')') SEPARATOR ', ') AS equipe
FROM
    film f
JOIN
    genre g ON f.genre_id = g.id
JOIN
    note n ON f.note_id = n.id
JOIN
    langue l ON f.langue_id = l.id
LEFT JOIN
    assignation a ON f.id = a.media_id
LEFT JOIN
    personne p ON a.personne_id = p.id
WHERE
    f.id = VOTRE_ID_FILM;


# Donner le nombre total d oeuvre par type de média
SELECT
    'Film' AS media_type,
    COUNT(*) AS total
FROM
    film
UNION ALL
SELECT
    'Vidéo' AS media_type,
    COUNT(*) AS total
FROM
    video
UNION ALL
SELECT
    'Musique' AS media_type,
    COUNT(*) AS total
FROM
    musique
UNION ALL
SELECT
    'Livre' AS media_type,
    COUNT(*) AS total
FROM
    livre;


# La note de chaque oeuvre et la moyenne des notes attribuées par type de média
-- Obtenir la note de chaque œuvre
SELECT
    'Film' AS media_type,
    film.titre AS media_titre,
    film.description AS media_description,
    note.evaluation AS media_note
FROM
    film
INNER JOIN note ON film.note_id = note.id
UNION ALL
SELECT
    'Vidéo' AS media_type,
    video.titre AS media_titre,
    video.description AS media_description,
    note.evaluation AS media_note
FROM
    video
INNER JOIN note ON video.note_id = note.id
UNION ALL
SELECT
    'Musique' AS media_type,
    musique.titre AS media_titre,
    musique.description AS media_description,
    note.evaluation AS media_note
FROM
    musique
INNER JOIN note ON musique.note_id = note.id
UNION ALL
SELECT
    'Livre' AS media_type,
    livre.titre AS media_titre,
    livre.description AS media_description,
    note.evaluation AS media_note
FROM
    livre
INNER JOIN note ON livre.note_id = note.id;

-- Obtenir la moyenne des notes par type de média
SELECT
    media_type,
    AVG(media_note) AS moyenne_notes
FROM (
    SELECT
        'Film' AS media_type,
        note.evaluation AS media_note
    FROM
        film
        INNER JOIN note ON film.note_id = note.id
    UNION ALL
    SELECT
        'Vidéo' AS media_type,
        note.evaluation AS media_note
    FROM
        video
        INNER JOIN note ON video.note_id = note.id
    UNION ALL
    SELECT
        'Musique' AS media_type,
        note.evaluation AS media_note
    FROM
        musique
        INNER JOIN note ON musique.note_id = note.id
    UNION ALL
    SELECT
        'Livre' AS media_type,
        note.evaluation AS media_note
    FROM
        livre
        INNER JOIN note ON livre.note_id = note.id
) AS media_notes
GROUP BY media_type;
