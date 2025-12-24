import requests
from pytest_bdd import scenarios, given, when, then, parsers

BASE_URL = "https://635278be-0b1a-4a06-b89b-3327535aea13.mock.pstmn.io"

scenarios("../features/scenario_demandeDon.feature")

# Scénario 1 : Réception d'une notification de confirmation
@given(parsers.parse("un client avec une adresse courriel valide"))
def client_adresse_courriel_valide():
    response = requests.get(f"{BASE_URL}/client/courriel")
    assert response.status_code == 200

@when(parsers.parse("le client envoie une demande de don"))
def client_envoie_don():
    response = requests.post(f"{BASE_URL}/form")
    assert response.status_code == 200

@then(parsers.parse("le code de réponse devrait être 200"))
def verification_code_reponse():
    pass # vérification du code de réponse est déjà vérifier

@then(parsers.parse("le client reçoit une notification de confirmation par courriel"))
def client_recoit_notification():
    response = requests.get(f"{BASE_URL}/form/confirmationDon")
    assert response.status_code == 200

# Scénario 2 : Réception des informations du formulaire
@given(parsers.parse("un client avec une adresse courriel valide"))
def client_adresse_courriel_valide():
    response = requests.get(f"{BASE_URL}/client/courriel")
    assert response.status_code == 200

@when(parsers.parse("le client envoie une demande de don"))
def client_envoie_don():
    response = requests.post(f"{BASE_URL}/form")
    assert response.status_code == 200

@then(parsers.parse("le code de réponse devrait être 200"))
def verification_code_reponse():
    pass # vérification du code de réponse est déjà vérifier

@then(parsers.parse("le client reçoit une notification de confirmation par courriel"))
def client_recoit_notification():
    response = requests.get(f"{BASE_URL}/form/confirmationDon")
    assert response.status_code == 200

@then(parsers.parse("il peut voir la date de la collecte du don ainsi que son statut dans le courriel"))
def client_recoit_notification():
    response = requests.get(f"{BASE_URL}/form/confirmationDon/infosForm")
    assert response.status_code == 200

# Scénario 3 : Annulation de la demande de don
@given(parsers.parse("un client avec une adresse courriel valide"))
def client_adresse_courriel_valide():
    response = requests.get(f"{BASE_URL}/client/courriel")
    assert response.status_code == 200

@when(parsers.parse("le client clique sur le bouton « Annuler »"))
def client_clique_annuler():
    pass

@then(parsers.parse("il est redirigé à la page précédente"))
def verification_redirection_formulaire():
    pass

@then(parsers.parse("la demande de don est annulée"))
def demande_don_annuler():
    response = requests.get(f"{BASE_URL}/form/annuler") # return message that says demande de don est annuler
    assert response.status_code == 200