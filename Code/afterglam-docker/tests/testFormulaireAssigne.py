import requests
from pytest_bdd import scenarios, given, when, then, parsers

BASE_URL = "https://635278be-0b1a-4a06-b89b-3327535aea13.mock.pstmn.io"
scenarios("../features/scenario_formulaireAssigne.feature")

# =========================================================
# Scénario 1 : Formulaire déjà assigné à un autre admin
# =========================================================

@given("un administrateur existe et est connecté")
def admin_connecte():
    courriel = "leen.alharash@afterglam.com"
    response = requests.get(f"{BASE_URL}/admin?courriel={courriel}")
    assert response.status_code == 200
    return response.json()

@given(parsers.parse("un formulaire existe avec l'id {form_id:d} et un autre administrateur est déjà assigné"))
def formulaire_already_assigned(form_id):
    return {"id": form_id, "admin_id": "someone"}

@when(parsers.parse("j'essaie de m'assigner le formulaire avec l'id {form_id:d}"))
def essayer_assigner(form_id, request):
    response = requests.post(f"{BASE_URL}/form/{form_id}/assign?admin=4") 
    request._assign_response = response
    return response

@then("je ne peux pas m'assigner ce formulaire")
def cannot_assign_formulaire(request):
    resp = request._assign_response
    assert resp.status_code == 409
    data = resp.json()
    assert data.get("statut") == "error"

@then(parsers.parse('un message d\'erreur "{msg}" est affiché'))
def error_message(request, msg):
    resp = request._assign_response
    data = resp.json()
    assert data.get("message") == msg

# =========================================================
# Scénario 2 : Filtrage des formulaires disponibles
# =========================================================

@given("plusieurs formulaires existent, certains assignés et certains non assignés")
def multiple_formulaires():
    # Postman endpoint: GET /forms
    response = requests.get(f"{BASE_URL}/forms")
    assert response.status_code == 200
    return response.json()

@when('je filtre la liste des formulaires avec "disponibles"')
def filtrer_formulaires_disponibles(request):
    response = requests.get(f"{BASE_URL}/forms?filter=disponible")
    request._filter_response = response
    return response

@then("seuls les formulaires non assignés sont affichés")
def check_only_available(request):
    resp = request._filter_response
    data = resp.json()["data"]
    for formulaire in data:
        assert formulaire["assigned_admin"] is None
