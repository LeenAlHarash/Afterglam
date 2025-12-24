Feature: Sélectionner la date de collecte du don
    Scenario: Afficher les dates du mois
        Given un client sur la page du formulaire
        When le client clique sur l'icône du calendrier
        Then le code de réponse devrait être 200
        And une fenêtre s'affiche avec toutes les dates du mois 10

    Scenario: Apparition de la fenêtre de choix du temps
        Given un client sur la page du formulaire
        When le client sélectionne une date
        Then le code de réponse devrait être 200
        And une fenêtre s'affiche pour choisir les temps disponibles