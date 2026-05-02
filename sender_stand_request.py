import requests
import configuration
import data

# Función para crear un nuevo usuario y obtener el token
def get_new_user_token():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                             json=data.user_body,
                             headers=data.headers)
    return response.json()["authToken"]

# Función para crear el kit 
def post_new_client_kit(kit_body, auth_token):
    current_headers = data.headers.copy()
    current_headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=current_headers)