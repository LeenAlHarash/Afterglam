Feature: Consultation des formulaires

  Scenario: Afficher les détails d’un formulaire existant
    Given un administrateur existe et est connecté
    And un formulaire existe avec l’id 5
    When je clique sur le formulaire avec l’id "5"
    Then la réponse doit avoir le code de statut 200
    And la réponse doit inclure les détails du formulaire avec l'id 5

  Scenario: Afficher le champ de statut d’un formulaire
    Given un administrateur existe et est connecté
    And un formulaire existe avec l’id 5 et le statut "PEND"
    When je sélectionne le formulaire avec l’id "5"
    Then la réponse doit avoir le code de statut 200
    And la réponse doit inclure un champ de statut avec la valeur "PEND"
