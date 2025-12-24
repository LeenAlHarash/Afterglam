-- Création de la base de données
CREATE DATABASE IF NOT EXISTS afterglam;
USE afterglam;

-- Table Client
CREATE TABLE Client (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    telephone VARCHAR(20) NOT NULL,
    courriel VARCHAR(80) NOT NULL,
    adresse VARCHAR(100) NOT NULL,
    code_postal VARCHAR(10) NOT NULL,
    form_id INT NULL
);

-- Table Admin
CREATE TABLE Admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    telephone VARCHAR(20) NOT NULL,
    courriel VARCHAR(80) NOT NULL,
    mdp VARCHAR(72) NOT NULL
);

-- Table MaisonFuneraille
CREATE TABLE MaisonFuneraille (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    telephone VARCHAR(20) NOT NULL,
    adresse VARCHAR(100) NOT NULL,
    code_postal VARCHAR(10) NOT NULL
);

-- Table Form
CREATE TABLE Form (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date_creation DATETIME NOT NULL,
    statut ENUM('OPEN', 'CLOSE', 'PEND') NOT NULL,
    date_collecte DATETIME NOT NULL,
    client_id INT NULL,
    admin_id INT,
    maison_id INT,
    CONSTRAINT fk_client FOREIGN KEY (client_id) REFERENCES Client(id),
    CONSTRAINT fk_admin FOREIGN KEY (admin_id) REFERENCES Admin(id),
    CONSTRAINT fk_maison FOREIGN KEY (maison_id) REFERENCES MaisonFuneraille(id)
);

-- Table Cosmetique
CREATE TABLE Cosmetique (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL
);

-- Table FormCosmetique (table associative)
CREATE TABLE FormCosmetique (
    id INT AUTO_INCREMENT PRIMARY KEY,
    form_id INT NOT NULL,
    cosmetique_id INT NOT NULL,
    CONSTRAINT fk_form FOREIGN KEY (form_id) REFERENCES Form(id),
    CONSTRAINT fk_cosmetique FOREIGN KEY (cosmetique_id) REFERENCES Cosmetique(id)
);

ALTER TABLE Client
ADD CONSTRAINT fk_form_client FOREIGN KEY (form_id) REFERENCES Form(id);

-- Table RefreshToken
CREATE TABLE refresh_tokens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status VARCHAR(10) DEFAULT 'valid'
);

INSERT INTO Admin (id, nom, prenom, telephone, courriel, mdp) VALUES
(1, 'AlHarash', 'Leen', '514-999-0000', 'leen.alharash@afterglam.com', 'admin1'),
(2, 'Hanfaoui', 'Mary', '438-123-4567', 'mary.hanfaoui@afterglam.com', 'admin2'),
(3, 'Roy', 'Alexandre', '438-444-5555', 'alex.roy@afterglam.com', 'admin3'),
(4, 'Lavoie', 'Camille', '514-333-2222', 'camille.lavoie@afterglam.com', 'admin4');

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