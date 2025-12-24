Feature: Choisir les cosmétiques à donner
    Scenario: Afficher la liste des cosmétiques disponibles
        Given un client sur la page du formulaire
        When le client clique sur le bouton « Choisir les produits »
        Then il peut voir la liste des cosmétiques disponible à donner

    Scenario: Confirmation des cosmétiques choisi
        Given un client sur la liste des cosmétiques disponible à donner
        When le client choisi les cosmétiques et clique sur « Confirmer »
        Then le code de réponse devrait être 200
        And il est redirigé au formulaire avec les cosmétiques choisis