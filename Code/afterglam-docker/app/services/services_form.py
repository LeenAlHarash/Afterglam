from typing import List, Optional

from app.db import afterglam
from app.data.data_form import get_all_forms, get_a_form, get_a_form_from_client, get_forms_from_client_nom, get_forms_from_admin, get_forms_from_admin_nom, get_forms_from_maison, get_forms_from_maison_nom, create_form_in_db, update_form_in_db, delete_form_in_db, get_forms_from_client_email
from app.interface.model_view.view_form import FormView
from app.data.model.model_form import Form
from app.utils.auth import format_date

def convert_forms_to_view(form: dict) -> FormView:
    if isinstance(form, dict):
        if "prenom" in form and "nom" in form :
            return FormView(
                id=form["id"],
                date_creation=format_date(form["date_creation"]),
                statut=form["statut"],
                date_collecte=format_date(form["date_collecte"]),
                client_id=form["client_id"],
                admin_id=form["admin_id"],
                maison_id=form["maison_id"],
                nom=form["nom"],
                prenom=form["prenom"]
            )
        elif "nom" in form:
            return FormView(
                id=form["id"],
                date_creation=format_date(form["date_creation"]),
                statut=form["statut"],
                date_collecte=format_date(form["date_collecte"]),
                client_id=form["client_id"],
                admin_id=form["admin_id"],
                maison_id=form["maison_id"],
                nom=form["nom"],
                prenom="None"
            )
        else:
            return FormView(
                id=form["id"],
                date_creation=format_date(form["date_creation"]),
                statut=form["statut"],
                date_collecte=format_date(form["date_collecte"]),
                client_id=form["client_id"],
                admin_id=form["admin_id"],
                maison_id=form["maison_id"],
                nom="None",
                prenom="None"
            )
    else:
        return FormView(
            id=form.id,
            date_creation=format_date(form.date_creation),
            statut=form.statut,
            date_collecte=format_date(form.date_collecte),
            client_id=form.client_id,
            admin_id=form.admin_id,
            maison_id=form.maison_id,
            nom="None",
            prenom="None"
        )

def list_forms() -> List[FormView]:
    forms = get_all_forms()
    return [convert_forms_to_view(f) for f in forms]

# Get form by ID
def get_form_by_id(form_id: int) -> Optional[FormView]:
    form = get_a_form(form_id)
    if form:
        return convert_forms_to_view(form)
    return None


# Get forms by client ID
def get_form_by_client_id(client_id: int) -> List[FormView]:
    forms = get_a_form_from_client(client_id)
    if forms:
        return [convert_forms_to_view(c) for c in forms]
    return None

# Get client name by form ID
def get_client_name_by_form_id(client_id: int) -> Optional[str]:
    forms = get_forms_from_client_nom(client_id)
    if forms:
        return [convert_forms_to_view(c) for c in forms]
    return None

# Get forms by client email, basically the client can see the forms they submitted by typing their email in
def get_form_by_client_email(client_email: str) -> List[FormView]:
    forms = get_forms_from_client_email(client_email)
    if forms:
        return [convert_forms_to_view(c) for c in forms]
    return None

# Get forms by admin ID
def get_form_by_admin_id(admin_id: int) -> List[FormView]:
    forms = get_forms_from_admin(admin_id)
    if forms:
        return [convert_forms_to_view(c) for c in forms]
    return None

# Get admin name by form ID
def get_admin_name_by_form_id(admin_id: int) -> Optional[str]:
    forms = get_forms_from_admin_nom(admin_id)
    if forms:
        return [convert_forms_to_view(c) for c in forms]
    return None


# Get forms by maison ID
def get_form_by_maison_id(maison_id: int) -> List[FormView]:
    forms = get_forms_from_maison(maison_id)
    if forms:
        return [convert_forms_to_view(c) for c in forms]
    return None

# Get maison name by form ID
def get_maison_name_by_form_id(maison_id: int) -> Optional[str]:
    forms = get_forms_from_maison_nom(maison_id)
    if forms:
        return [convert_forms_to_view(c) for c in forms]
    return None

def create_form_db(form: Form) -> FormView:
    form = create_form_in_db(form)
    if form:
        return convert_forms_to_view(form)
    return None

def update_form_db(form_id: int, form: FormView) -> Optional[FormView]:
    form = update_form_in_db(form_id, form)
    if form:
        return convert_forms_to_view(form)
    return None

def delete_form_db(form_id: int) -> bool:
    form = delete_form_in_db(form_id)
    if form:
        return True
    return False