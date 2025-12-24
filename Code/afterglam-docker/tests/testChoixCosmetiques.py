import requests, pytest
from pytest_bdd import scenarios, given, when, then, parsers

BASE_URL = "https://635278be-0b1a-4a06-b89b-3327535aea13.mock.pstmn.io"

scenarios("../features/scenario_choixCosmetiques.feature")

# Scénario 1 : Afficher la liste des cosmétiques disponibles
@given(parsers.parse("un client sur la page du formulaire"))
def client_sur_page_formulaire():
    pass

@when(parsers.parse("le client clique sur le bouton « Choisir les produits »"))
def client_clique_choisir_produits():
    pass

@then(parsers.parse("il peut voir la liste des cosmétiques disponible à donner"))
def client_voit_liste_cosmetiques():
    response = requests.get(f"{BASE_URL}/cosmetiques")
    assert response.status_code == 200
    data = response.json()
    for item in data:
        assert "id" in item
        assert "nom" in item

# Scénario 2 : Confirmation des cosmétiques choisi
@given(parsers.parse("un client sur la liste des cosmétiques disponible à donner"))
def client_sur_liste_cosmetiques():
    response = requests.get(f"{BASE_URL}/cosmetiques")
    assert response.status_code == 200

@when(parsers.parse("le client choisi les cosmétiques et clique sur « Confirmer »"))
def client_confirme_choix():
    # Liste des cosmétiques choisi
    selected_cosmetics = [1, 2, 3]
    response = requests.post(
        f"{BASE_URL}/cosmetique/choixDesCosmetiques",
        json={"cosmetiques_ids": selected_cosmetics}
    )
    assert response.status_code == 200
    return response

@then(parsers.parse("le code de réponse devrait être 200"))
def verification_code_reponse():
    pass # code de réponse déjà vérifier dans le test précédent

@then(parsers.parse("il est redirigé au formulaire avec les cosmétiques choisis"))
def verification_redirection_formulaire():
    pass