INSERT INTO Admin (id, nom, prenom, telephone, courriel, mdp) VALUES
(1, 'AlHarash', 'Leen', '514-999-0000', 'leen.alharash@afterglam.com', SHA2('admin1', 256)),
(2, 'Hanfaoui', 'Mary', '438-123-4567', 'mary.hanfaoui@afterglam.com', SHA2('admin2', 256)),
(3, 'Roy', 'Alexandre', '438-444-5555', 'alex.roy@afterglam.com', SHA2('admin3', 256)),
(4, 'Lavoie', 'Camille', '514-333-2222', 'camille.lavoie@afterglam.com', SHA2('admin4', 256));

INSERT INTO MaisonFuneraille (id, nom, telephone, adresse, code_postal) VALUES
(1, 'Maison Paix Éternelle', '514-555-1234', '123 Rue Ottawa, Montréal, QC', 'H2M 1L9'),
(2, 'Salon Mémoire et Sérénité', '438-222-5678', '250 Rue Sherbrooke, Montréal, QC', 'H3C 4L5'),
(3, 'Maison Lumière du Souvenir', '514-789-6543', '89 Av. Papineau, Laval, QC', 'H7M 2J3');

INSERT INTO Cosmetique (id, nom) VALUES
(1, 'Fond de teint'),
(2, 'Mascara'),
(3, 'Rouge à lèvres'),
(4, 'Poudre'),
(5, 'Eyeliner'),
(6, 'Blush'),
(7, 'Crayon à sourcils'),
(8, 'Gloss'),
(9, 'Ombre à paupières'),
(10, 'Fixateur de maquillage');

INSERT INTO Client (id, nom, prenom, telephone, courriel, adresse, code_postal) VALUES
(1, 'Lévesque', 'Sophie', '514-111-2222', 'sophie.levesque@email.com', '101 Rue Bleue, Montréal', 'H3Z 2Z7'),
(2, 'Nguyen', 'Marc', '438-333-4444', 'marc.nguyen@email.com', '22 Boul. St-Laurent, Laval', 'H7P 3A6'),
(3, 'Dubois', 'Élise', '514-777-8888', 'elise.dubois@email.com', '45 Av. des Pins, Longueuil', 'J4K 5G2'),
(4, 'Tremblay', 'Jean', '514-444-2222', 'jean.tremblay@email.com', '77 Rue St-Hubert, Montréal', 'H2J 3K9'),
(5, 'Benali', 'Nora', '438-555-1212', 'nora.benali@email.com', '12 Av. Cartier, Laval', 'H7W 1K3'),
(6, 'Gagnon', 'Lucie', '514-222-9090', 'lucie.gagnon@email.com', '201 Rue St-Denis, Longueuil', 'J4H 2N6');

INSERT INTO Form (id, date_creation, statut, date_collecte, client_id, admin_id, maison_id) VALUES
(1, '2025-09-10 10:00:00', 'OPEN',  '2025-09-12 14:00:00', 1, 2, 1),
(2, '2025-09-11 11:30:00', 'PEND',  '2025-09-13 15:00:00', 2, 1, 1),
(3, '2025-09-12 09:15:00', 'CLOSE', '2025-09-14 10:00:00', 3, 2, 1),
(4, '2025-09-13 14:45:00', 'OPEN',  '2025-09-15 09:00:00', 4, 3, 2),
(5, '2025-09-14 16:20:00', 'PEND',  '2025-09-16 13:30:00', 5, 4, 3),
(6, '2025-09-15 18:10:00', 'CLOSE', '2025-09-17 11:00:00', 6, 3, 2);

INSERT INTO FormCosmetique (form_id, cosmetique_id) VALUES
(1, 1),
(1, 2),
(2, 3),
(2, 4),
(3, 5),
(3, 6),
(4, 1),
(4, 3),
(5, 2),
(5, 6),
(6, 4),
(6, 5);

-- Lier le id du form au form_id de la table Client, pour ce faire il faut désactiver sql safe updates et le réactiver
SET SQL_SAFE_UPDATES = 0;
UPDATE Client SET form_id = id;
SET SQL_SAFE_UPDATES = 1;