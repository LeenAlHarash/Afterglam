Feature: Formulaires déjà pris en charge

  Scenario: Formulaire déjà assigné à un autre admin
    Given un administrateur existe et est connecté
    And un formulaire existe avec l'id 3 et un autre administrateur est déjà assigné
    When j'essaie de m'assigner le formulaire avec l'id 3
    Then je ne peux pas m'assigner ce formulaire
    And un message d'erreur "Formulaire déjà pris en charge" est affiché

  Scenario: Filtrage des formulaires disponibles
    Given un administrateur existe et est connecté
    And plusieurs formulaires existent, certains assignés et certains non assignés
    When je filtre la liste des formulaires avec "disponibles"
    Then seuls les formulaires non assignés sont affichés
