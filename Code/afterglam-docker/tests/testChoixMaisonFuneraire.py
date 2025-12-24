import requests
from pytest_bdd import scenarios, given, when, then, parsers

BASE_URL = "https://635278be-0b1a-4a06-b89b-3327535aea13.mock.pstmn.io"

scenarios("../features/scenario_choixMaisonFuneraire.feature")

# Consulter l'adresse de la maison funéraire
@given(parsers.parse("un client sur la page du formulaire"))
def client_sur_page_formulaire():
    pass

@when(parsers.parse("le client sélectionne une maison funéraire"))
def client_selectionne_maison():
    pass

@then(parsers.parse("le code de réponse devrait être 200"))
def verification_code_reponse():
    pass # vérification du code de réponse est déjà vérifier à la prochaine étape

@then(parsers.parse("il peut voir les informations de celle-ci"))
def voir_adresse_maison():
    selected_maisonFuneraire = 2
    response = requests.get(f"{BASE_URL}/maisonFuneraire/choixMaisonFuneraire",
    json={"maison_funeraire_choisi": selected_maisonFuneraire})
    assert response.status_code == 200