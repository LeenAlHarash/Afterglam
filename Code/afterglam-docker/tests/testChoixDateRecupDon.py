import requests
from pytest_bdd import scenarios, given, when, then, parsers

BASE_URL = "https://635278be-0b1a-4a06-b89b-3327535aea13.mock.pstmn.io"

scenarios("../features/scenario_choixDateRecupDon.feature")

# Scénario 1 : Afficher les dates du mois
@given(parsers.parse("un client sur la page du formulaire"))
def client_sur_page_formulaire():
    pass

@when(parsers.parse("le client clique sur l'icône du calendrier"))
def client_clique_icone_calendrier():
    pass

@then(parsers.parse("le code de réponse devrait être 200"))
def verification_code_reponse():
    pass # vérification du code de réponse est déjà vérifier à la prochaine étape

@then(parsers.parse("une fenêtre s'affiche avec toutes les dates du mois 10"))
def client_sur_liste_cosmetiques():
    response = requests.get(f"{BASE_URL}/dates")
    assert response.status_code == 200

# Scénario 2 : Apparition de la fenêtre de choix du temps
@given(parsers.parse("un client sur la page du formulaire"))
def client_sur_page_formulaire():
    pass

@when(parsers.parse("le client sélectionne une date"))
def client_selectionne_date():
    selected_date = "2025-10-31"
    response = requests.get(f"{BASE_URL}/dates/dateChoisi",
        json={"date_choisi": selected_date})
    assert response.status_code == 200

@then(parsers.parse("le code de réponse devrait être 200"))
def verification_code_reponse():
    pass # code de réponse déjà vérifier dans le test précédent

@then(parsers.parse("une fenêtre s'affiche pour choisir les temps disponibles"))
def verification_affichage_temps():
    response = requests.get(f"{BASE_URL}/date/dateChoisi/temps") # show all times possible
    assert response.status_code == 200