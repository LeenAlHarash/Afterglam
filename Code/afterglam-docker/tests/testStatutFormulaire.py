import requests
from pytest_bdd import scenarios, given, when, then, parsers

BASE_URL = "https://635278be-0b1a-4a06-b89b-3327535aea13.mock.pstmn.io"
scenarios("../features/scenario_statutFormulaire.feature")


@given("un administrateur existe et est connecté")
def admin_connecte():
    courriel = "leen.alharash@afterglam.com"
    response = requests.get(f"{BASE_URL}/admin?courriel={courriel}")
    assert response.status_code == 200
    return response.json()


@given(parsers.parse("un formulaire existe avec l'id {form_id:d} et le statut \"{statut}\""))
def formulaire_with_status(form_id, statut):
    return {"id": form_id, "statut": statut}


# =========================================================
# SCENARIO 1: Changement de statut et enregistrement
# =========================================================
@when(parsers.parse("je change le statut du formulaire avec l'id \"{form_id}\" à \"{new_statut}\""))
def change_form_status_save(form_id, new_statut, request):
    response = requests.post(f"{BASE_URL}/form/{form_id}?statut={new_statut}")
    request._save_response = response
    return response

@when('je clique sur "Enregistrer"')
def save_status(request):
    pass

@then(parsers.parse("la réponse de l'enregistrement doit avoir le code de statut {code:d}"))
def check_status_code_save(request, code):
    resp = request._save_response
    assert resp.status_code == code

@then("la modification du statut est sauvegardée")
def status_saved(request):
    resp = request._save_response
    data = resp.json()
    assert data.get("statut") == "PEND"

@then(parsers.parse('un message de succès "{msg}" est affiché'))
def success_message(request, msg):
    resp = request._save_response
    data = resp.json()
    if "message" in data:
        assert data.get("message") == msg


# =========================================================
# SCENARIO 2: Annulation des modifications de statut
# =========================================================
@when("j'annule les modifications")
def cancel_status(request):
    response = requests.get(f"{BASE_URL}/form/annuler")
    request._cancel_response = response
    return response


@then(parsers.parse("la réponse de l'annulation doit avoir le code de statut {code:d}"))
def check_status_code_cancel(request, code):
    resp = request._cancel_response
    assert resp.status_code == code


@then(parsers.parse('le statut du formulaire reste "{statut}"'))
def status_not_changed(request, statut):
    resp = request._cancel_response
    data = resp.json()
    assert data.get("message") == "Votre demande du changement de statut a été annuler"
    assert data.get("statut", statut) == statut
