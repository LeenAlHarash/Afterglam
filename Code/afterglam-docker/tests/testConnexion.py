import requests, pytest
from pytest_bdd import scenarios, given, when, then, parsers

BASE_URL = "https://635278be-0b1a-4a06-b89b-3327535aea13.mock.pstmn.io"

scenarios("../features/scenario_connexion.feature")

# =========================================================
# Scénario 1 : Connexion réussie avec identifiants valides
# =========================================================

@given(parsers.parse('un administrateur existe avec le courriel "leen.alharash@afterglam.com"'))
def admin_existe():
    response = requests.get(f"{BASE_URL}/admin?courriel=leen.alharash@afterglam.com")
    assert response.status_code == 200

@when(parsers.parse('je tente de me connecter avec le courriel "leen.alharash@afterglam.com" et le mot de passe "admin1"'))
def tentative_connexion():
    response = requests.post(f"{BASE_URL}/auth/connexion?courriel=leen.alharash@afterglam.com&mdp=admin1")
    assert response.status_code == 200

@then("la réponse doit avoir le code de statut 200")
def code_200_generic():
    pass # vérification du code de réponse est vérifier à l'étape précédente

@then("l’administrateur est redirigé vers le tableau de bord")
def redirection_dashboard():
    pass

# =========================================================
# Scénario 2 : Connexion échouée avec mot de passe incorrect
# =========================================================

@given(parsers.parse('un administrateur existe avec le courriel "leen.alharash@afterglam.com"'))
def admin_existe():
    response = requests.get(f"{BASE_URL}/admin?courriel=leen.alharash@afterglam.com")
    assert response.status_code == 200

@when(parsers.parse('je tente de me connecter avec le courriel "leen.alharash@afterglam.com" et le mot de passe "ECHANGEAUXDONNEES"'))
def tentative_connexion_incorrect(request):
    response = requests.post(f"{BASE_URL}/auth/connexionErreur?courriel=leen.alharash@afterglam.com&mdp=ECHANGEAUXDONNEES")
    assert response.status_code == 401

@then("la réponse doit avoir le code de statut 401")
def code_401(request):
    pass # code de vérification déjà vérifié à l'étape précédente

@then(parsers.parse('le corps de la réponse doit contenir le message d’erreur "Identifiants invalides"'))
def message_erreur():
    response = requests.post(f"{BASE_URL}/auth/connexionErreur?courriel=leen.alharash@afterglam.com&mdp=ECHANGEAUXDONNEES")
    data = response.json() # on stocke la réponse json dans variable data
    assert data.get("error") == "Identifiants invalides" # on compare le message d'erreur à partir de la réponse de la requête à celui qu'on veut

# =========================================================
# Scénario 3 : Déconnexion de l’administrateur
# =========================================================

@given("un administrateur est actuellement connecté")
def admin_connecte(request):
    adminConnecter = requests.Session() # cherche la session de l'utilisation
    response = adminConnecter.post(f"{BASE_URL}/auth/connexion?courriel=leen.alharash@afterglam.com&mdp=admin1")
    assert response.status_code == 200

@when('il clique sur "Se déconnecter"')
def admin_deconnexion():
    response = requests.post(f"{BASE_URL}/auth/deconnexion?courriel=leen.alharash@afterglam.com")
    assert response.status_code == 200

@then("la session est terminée et l’administrateur est redirigé vers la page de connexion")
def redirection_login():
    pass
