<h1>Proyecto 6 - Introducción a la automatización de pruebas</h1>
<h2>Descripción del Proyecto</h2>
<h4>El proyecto tiene como objetivo automatizar y agilizar el proceso de pruebas que se realizan en el campo "name". Este campo es variable en el número de caracteres y puede contener tanto caracteres numéricos como especiales. Al garantizar la calidad de este proceso, se busca asegurar que la introducción de datos por parte del usuario se realice de manera adecuada y sin errores.

Las pruebas cubren una amplia gama de casos, tanto positivos como negativos. En los casos positivos, se espera una creación exitosa del usuario, mientras que en los casos negativos se anticipan errores debido a entradas no válidas. Al automatizar estas pruebas, se optimiza el tiempo y se minimizan los errores humanos, lo que contribuye a la fiabilidad y estabilidad del sistema.

Este proyecto se basa en la documentación proporcionada por apiDoc para definir las especificaciones de la funcionalidad y garantizar su coherencia con los requisitos del sistema.</h4>

<h2>Cómo usar</h2>
<h4>Antes de ejecutar las pruebas, asegúrate de tener instalados los siguientes paquetes de Python:
<ul>
    <li>pytest</li>
    <li>requests </li>
</ul>
Para ejecutar las pruebas: 
<ul> 
    <li> Primero actualiza la constante que contiene la URL que se encuentra en el archivo configuration.py 
    </li>
    <li> Después usa la terminal y ejecuta el comando "pytest" seguido del nombre del archivo que contiene las pruebas.</li>
</ul>
</h4>

<h2>Estructura del proyecto</h2>
<ul>
    <li>configuration.py: Contiene las constantes de configuración, como la URL del servicio y las rutas de las API.</li>
    <li>data.py: Almacena los datos de prueba, como los encabezados y los cuerpos de solicitud.</li>
    <li>sender_stand_request.py: Contiene las funciones para enviar solicitudes HTTP a la API.</li>
    <li>create_kit_name_kit_test.py: Pruebas automatizadas para la funcionalidad de creación de kits de usuarios, verificando el campo "name".</li>
    <li>README.md: Proporciona información general sobre el proyecto y cómo configurarlo.</li>
    <li>.gitignore: Archivo de configuración para excluir archivos y directorios del control de versiones.</li>
</ul>

<h2>Solicitudes necesarias antes de realizar la lista de comprobación</h2>
<table>
  <tr>
    <th>Descripción</th>
    <th>Solicitud</th>
  </tr>
  <tr>
    <td>Crea un nuevo usuario utilizando la función post_new_user y devuelve el token de autenticación de la respuesta</td>
    <td>def get_new_user_token(first_name):
user_body = get_user_body(first_name)
response = sender_stand_request.post_new_user(user_body)
return response.json()[“authToken”]
<td>def get_user_body(first_name):
current_body = data.user_body.copy()
current_body[“firstName”] = first_name
return current_body</td>
  </tr>
  <tr>
    <td>Crea un nuevo diccionario del cuerpo de kit con el campo name</td>
    <td>def get_kit_body(name):
kit_body = {“name”: name}
return kit_body</td>
  </tr>
    <tr>
    <td>Función para las pruebas positivas</td>
    <td>def positive_assert(kit_body, auth_token):
response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
assert response.status_code == 201
assert response.json()[“name”] == kit_body[“name”]</td>
  </tr>
    <tr>
    <td>Función para las pruebas negativas</td>
    <td>def negative_assert_code_400(kit_body, auth_token):
response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
assert response.status_code == 400</td>
  </tr>

</table>

<h2>Listas de comprobación</h2>
<table>
  <tr>
    <th>№</th>
    <th>Descripción</th>
    <th>RE</th>
  </tr>
  <tr>
    <td>1</td>
    <td>El número permitido de caracteres (1)</td>
    <td>Código de respuesta: 201</td>
  </tr>
  <tr>
    <td>2</td>
    <td>El número permitido de caracteres (511)</td>
    <td>Código de respuesta: 201</td>
  </tr>
  <tr>
    <td>3</td>
    <td>El número de caracteres es menor que la cantidad permitida (0)</td>
    <td>Código de respuesta: 400</td>
  </tr>
    <tr>
    <td>4</td>
    <td>El número de caracteres es mayor que la cantidad permitida (512)</td>
    <td>Código de respuesta: 400</td>
  </tr>
    <tr>
    <td>5</td>
    <td>Se permiten caracteres especiales</td>
    <td>Código de respuesta: 201</td>
  </tr>
    <tr>
    <td>6</td>
    <td>Se permiten espacios</td>
    <td>Código de respuesta: 201</td>
  </tr>
    <tr>
    <td>7</td>
    <td>Se permiten números</td>
    <td>Código de respuesta: 201</td>
  </tr>
    <tr>
    <td>8</td>
    <td>El parámetro no se pasa en la solicitud</td>
    <td>Código de respuesta: 400</td>
  </tr>
      <tr>
    <td>9</td>
    <td>Se ha pasado un tipo de parámetro diferente (número)</td>
    <td>Código de respuesta: 400</td>
  </tr>
</table>