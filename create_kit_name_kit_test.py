import sender_stand_request
import data


def positive_assert(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]


def negative_assert_code_400(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 400


# Pruebas de la Lista de Comprobación

# Prueba 1: 1 carácter
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert({"name": "a"})


# Prueba 2: 511 caracteres (valor proporcionado)
def test_create_kit_511_letter_in_name_get_success_response():
    name_511 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    positive_assert({"name": name_511})


# Prueba 3: 0 caracteres (vacío)
def test_create_kit_empty_name_get_error_response():
    negative_assert_code_400({"name": ""})


# Prueba 4: 512 caracteres (valor proporcionado)
def test_create_kit_512_letter_in_name_get_error_response():
    name_512 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    negative_assert_code_400({"name": name_512})


# Prueba 5: Caracteres especiales
def test_create_kit_special_symbol_in_name_get_success_response():
    positive_assert({"name": '"№%@,'})


# Prueba 6: Espacios
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert({"name": " A Aaa "})


# Prueba 7: Números
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert({"name": "123"})


# Prueba 8: Parámetro ausente
def test_create_kit_no_name_get_error_response():
    negative_assert_code_400({})


# Prueba 9: Tipo de dato incorrecto (número)
def test_create_kit_int_name_get_error_response():
    negative_assert_code_400({"name": 123})