import requests
from pytest_bdd import scenarios, given, when, then, parsers

BASE_URL = "https://635278be-0b1a-4a06-b89b-3327535aea13.mock.pstmn.io"
scenarios("../features/scenario_formulaire.feature")

# =========================================================
# Scénario 1 : Afficher les détails d’un formulaire existant
# =========================================================

@given("un administrateur existe et est connecté")
def admin_connecte():
    courriel = "leen.alharash@afterglam.com"
    response = requests.get(f"{BASE_URL}/admin?courriel={courriel}")
    assert response.status_code == 200, f"Admin introuvable ou non connecté (code {response.status_code})"
    return response.json()

@given(parsers.parse("un formulaire existe avec l’id {form_id:d}"))
def formulaire_existe(form_id):
    response = requests.get(f"{BASE_URL}/form/{form_id}")
    assert response.status_code == 200

@when(parsers.parse('je clique sur le formulaire avec l’id "{form_id}"'))
def cliquer_formulaire(form_id):
    response = requests.get(f"{BASE_URL}/form/{form_id}/details")
    assert response.status_code == 200
    return response

@then("la réponse doit avoir le code de statut 200")
def statut_200():
    pass  

@then(parsers.parse('la réponse doit inclure les détails du formulaire avec l\'id {form_id:d}'))
def verifier_details_formulaire(form_id):
    response = requests.get(f"{BASE_URL}/form/{form_id}/details")
    data = response.json()
    assert data.get("id") == form_id
    assert "date_creation" in data
    assert "statut" in data

# =========================================================
# Scénario 2 : Afficher le champ de statut d’un formulaire
# =========================================================

@given(parsers.parse('un formulaire existe avec l’id {form_id:d} et le statut "{statut}"'))
def formulaire_avec_statut(form_id, statut):
    response = requests.get(f"{BASE_URL}/form/{form_id}/details")
    assert response.status_code == 200
    data = response.json()
    assert data.get("statut") == statut

@when(parsers.parse('je sélectionne le formulaire avec l’id "{form_id}"'))
def selectionner_formulaire(form_id, request):
    response = requests.get(f"{BASE_URL}/form/{form_id}/details")
    assert response.status_code == 200
    request._formulaire_response = response.json()
    return response

@then(parsers.parse('la réponse doit inclure un champ de statut avec la valeur "{statut}"'))
def verifier_statut_formulaire(request, statut):
    data = request._formulaire_response
    assert data.get("statut") == statut
