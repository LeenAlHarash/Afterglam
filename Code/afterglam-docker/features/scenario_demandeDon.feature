Feature: Effectuer une demande de don
    Scenario: Réception d'une notification de confirmation
        Given un client avec une adresse courriel valide
        When le client envoie une demande de don
        Then le code de réponse devrait être 200
        And le client reçoit une notification de confirmation par courriel

    Scenario: Réception des informations du formulaire
        Given un client avec une adresse courriel valide
        When le client envoie une demande de don
        Then le code de réponse devrait être 200
        And le client reçoit une notification de confirmation par courriel
        Then il peut voir la date de la collecte du don ainsi que son statut dans le courriel

    Scenario: Annulation de la demande de don
        Given un client avec une adresse courriel valide
        When le client clique sur le bouton « Annuler »
        Then il est redirigé à la page précédente
        And la demande de don est annulée