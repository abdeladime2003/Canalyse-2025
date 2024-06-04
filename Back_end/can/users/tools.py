from .models import Client
from django.db import IntegrityError
import re

def create_user_with_validation(first_name, last_name, birthday, email, password, phone, country, residence_location):
    errors = []
    # Validation de l'email
    bool_email, email_errors = _is_valid_email(email)
    if not bool_email:
        errors.extend(email_errors)

    # Validation du mot de passe
    bool_password, password_errors = _is_valid_password(password)
    if not bool_password:
        errors.extend(password_errors)

    if not errors:
        try:
            user = Client.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                birth_day=birthday,
                email=email,
                password=password,
                phone=phone,
                country=country,
                residence_location=residence_location
            )
            return user, None
        except IntegrityError as e:
            if 'unique constraint' in str(e).lower():
                if Client.objects.filter(email=email).exists():
                    errors.append("Cet email est déjà utilisé.")
                if Client.objects.filter(first_name=first_name, last_name=last_name).exists():
                    errors.append("Ce nom d'utilisateur est déjà pris.")
            else:
                errors.append("Une erreur s'est produite lors de la création de l'utilisateur.")

    return None, errors

def _is_valid_password(password):
    errors = []

    if len(password) < 8:
        errors.append("Le mot de passe doit contenir au moins 8 caractères.")
    if not re.search(r'\d', password):
        errors.append("Le mot de passe doit contenir au moins un chiffre.")
    if not re.search(r'[A-Z]', password):
        errors.append("Le mot de passe doit contenir au moins une lettre majuscule.")
    if not re.search(r'[a-z]', password):
        errors.append("Le mot de passe doit contenir au moins une lettre minuscule.")

    return not errors, errors

def _is_valid_email(email):
    errors = []
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        errors.append("L'adresse email n'est pas valide.")
    return not errors, errors
