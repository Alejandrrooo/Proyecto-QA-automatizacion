import sender_stand_request
import data

# Crea un nuevo usuario utilizando la función post_new_user y devuelve el token de autenticación de la respuesta
def get_new_user_token(first_name):
    user_body = get_user_body(first_name)
    response = sender_stand_request.post_new_user(user_body)
    return response.json()["authToken"]

def get_user_body(first_name):
    current_body = data.user_body.copy()
    current_body["firstName"] = first_name
    return current_body

# Función para las pruebas positivas
def positive_assert(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Función para las pruebas negativas
def negative_assert_code_400(kit_body, auth_token):
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

# 1ero El número permitido de caracteres (1) / Código de respuesta: 201
def test_create_kit_1_letter_in_name_get_success_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = data.kit_1_letter
    positive_assert(kit_body, auth_token)

# 2ndo El número permitido de caracteres (511) / Código de respuesta: 201
def test_create_kit_511_letter_in_name_get_success_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = data.kit_511_letter
    positive_assert(kit_body, auth_token)

# 3ero El número de caracteres es menor que la cantidad permitida (0) / Código de respuesta: 400
def test_create_kit_0_letter_in_name_get_error_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = data.kit_0_letter
    negative_assert_code_400(kit_body, auth_token)

# 4to El número de caracteres es mayor que la cantidad permitida (512) / Código de respuesta: 400
def test_create_kit_512_letter_in_name_get_error_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = data.kit_512_letter
    negative_assert_code_400(kit_body, auth_token)

# 5to Se permiten caracteres especiales / Código de respuesta: 201
def test_create_kit_special_caracter_in_name_get_succes_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = data.kit_special_caracter
    positive_assert(kit_body, auth_token)

# 6to Se permiten espacios / Código de respuesta: 201
def test_create_kit_with_spaces_in_name_get_succes_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = data.kit_with_spaces
    positive_assert(kit_body, auth_token)

# 7mo Se permiten números / Código de respuesta: 201
def test_create_kit_numbers_in_name_get_succes_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = data.kit_numbers
    positive_assert(kit_body, auth_token)

# 8vo El parámetro no se pasa en la solicitud / Código de respuesta: 400
def test_create_kit_no_parameter_get_error_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = data.kit_no_parameter
    negative_assert_code_400(kit_body, auth_token)

# 9no Se ha pasado un tipo de parámetro diferente (número) / Código de respuesta: 400
def test_create_kit_type_number_get_error_response():
    auth_token = get_new_user_token("Andrea")
    kit_body = data.kit_type_number
    negative_assert_code_400(auth_token, kit_body)
