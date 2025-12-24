Feature: Sélectionner la maison funéraire
    Scenario: Consulter l'adresse de la maison funéraire
        Given un client sur la page du formulaire
        When le client sélectionne une maison funéraire
        Then le code de réponse devrait être 200
        And il peut voir les informations de celle-ci