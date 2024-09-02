SELECT owners.name
     , owners.username
     , owners.email
     , owners.id
FROM owners
ORDER BY owners.id

SELECT pets.owner_id AS pets_owner_id
     , pets.name     AS pets_name
     , pets.species  AS pets_species
     , pets.id       AS pets_id
FROM pets
WHERE pets.owner_id IN (1, 2)


--

SELECT pets.name
     , pets.species
     , pets.owner_id
     , pets.id
FROM pets
ORDER BY pets.id;

SELECT owners.id       AS owners_id
     , owners.name     AS owners_name
     , owners.username AS owners_username
     , owners.email    AS owners_email
FROM owners
WHERE owners.id IN (1, 2);

SELECT pets.name
     , pets.species
--      , pets.owner_id
--      , pets.id
     , owners_1.name AS name_1
     , owners_1.username
     , owners_1.email
--      , owners_1.id   AS id_1
FROM pets
     LEFT OUTER JOIN owners AS owners_1
         ON owners_1.id = pets.owner_id
ORDER BY pets.id;
