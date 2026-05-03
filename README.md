# Proyecto de Pruebas Automatizadas: API Urban Grocers (Kits)

Este proyecto contiene un grupo de pruebas automatizadas escritas en **Python** para validar la creación de "Kits" en la API de Urban Grocers. El objetivo es asegurar que el sistema acepte nombres válidos y rechace aquellos que no cumplen con las reglas de negocio.

## Descripción del Proyecto
El proyecto automatiza una lista de comprobación de 9 casos de prueba. Estos casos verifican:
- Límites de caracteres (mínimos y máximos).
- Uso de caracteres especiales y espacios.
- Validación de tipos de datos (strings vs números).
- Comportamiento ante parámetros ausentes.



## Tecnologías y Librerías
- **Lenguaje:** Python 3.x
- **Librerías:** 
  - `requests`: Para realizar las peticiones HTTP a la API.
  - `pytest`: Para ejecutar y organizar las pruebas.

## Estructura de Archivos
- `configuration.py`: Contiene las URLs base y los endpoints (rutas).
- `data.py`: Diccionarios con los cuerpos de las solicitudes (headers, user_body, kit_body).
- `sender_stand_request.py`: Funciones para enviar solicitudes POST de usuario y kits.
- `create_kit_name_kit_test.py`: El archivo principal con las pruebas lógicas (`asserts`).
- `.gitignore`: Archivos que Git debe ignorar (como carpetas de caché).

## Documentación utilizada
Para este proyecto se utilizó la documentación de la API de **Urban Grocers**:
[Enlace a la documentación](https://cnt-e12800ea-a1eb-4d1c-a387-6fdba31a39aa.containerhub.tripleten-services.com/docs/)

## Instrucciones para ejecutar las pruebas

### 1. Requisitos previos
Es necesario tener instalado Python y las librerías mencionadas. Puedes instalarlas con:
```bash
pip install requests pytest