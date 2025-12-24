Feature: Connexion de l’administrateur

  Scenario: Connexion réussie avec identifiants valides
    Given un administrateur existe avec le courriel "leen.alharash@afterglam.com"
    When je tente de me connecter avec le courriel "leen.alharash@afterglam.com" et le mot de passe "admin1"
    Then la réponse doit avoir le code de statut 200
    And l’administrateur est redirigé vers le tableau de bord

  Scenario: Connexion échouée avec mot de passe incorrect
    Given un administrateur existe avec le courriel "leen.alharash@afterglam.com"
    When je tente de me connecter avec le courriel "leen.alharash@afterglam.com" et le mot de passe "ECHANGEAUXDONNEES"
    Then la réponse doit avoir le code de statut 401
    And le corps de la réponse doit contenir le message d’erreur "Identifiants invalides"

  Scenario: Déconnexion de l’administrateur
    Given un administrateur est actuellement connecté
    When il clique sur "Se déconnecter"
    Then la réponse doit avoir le code de statut 200
    And la session est terminée et l’administrateur est redirigé vers la page de connexion