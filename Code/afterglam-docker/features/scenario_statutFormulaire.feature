Feature: Gestion du statut d’un formulaire

  Scenario: Changement de statut et enregistrement réussi
    Given un administrateur existe et est connecté
    And un formulaire existe avec l'id 2 et le statut "PEND"
    When je change le statut du formulaire avec l'id "2" à "CLOSE"
    And je clique sur "Enregistrer"
    Then la réponse de l'enregistrement doit avoir le code de statut 201
    And la modification du statut est sauvegardée
    And un message de succès "Statut mis à jour avec succès" est affiché

  Scenario: Annulation des modifications de statut
    Given un administrateur existe et est connecté
    And un formulaire existe avec l'id 2 et le statut "PEND"
    When je change le statut du formulaire avec l'id "2" à "CLOSE"
    And j'annule les modifications
    Then la réponse de l'annulation doit avoir le code de statut 200
    And le statut du formulaire reste "PEND"
