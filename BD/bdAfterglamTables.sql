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

-- Table RefreshToken
CREATE TABLE refresh_tokens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status VARCHAR(10) DEFAULT 'valid'
);


-- Table Admin
CREATE TABLE Admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    telephone VARCHAR(20) NOT NULL,
    courriel VARCHAR(80) NOT NULL,
    mdp VARBINARY(64) NOT NULL
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