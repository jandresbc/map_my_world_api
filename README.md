# Map my World API

## Descripción

Esta API permite gestionar ubicaciones y categorías, además de recomendar combinaciones de ubicación y categoría que no han sido revisadas recientemente.
La base de datos usada es Mysql 8.0.27 y la versión de python es = 3.11.1

## .env template
Asegurate que el proyecto tenga en su raiz un archivo con el nombre .env con la siguientes variables, las cuales son importantes para la ejecución del API.

1. DATABASE = 'nombre_de_la_basededatos'
2. HOST = "localhost"
3. USER = "usuario_mysql"
4. PASS = "password_usuario"
5. PORT = 3306 # Puerto de ejecución, por defecto Mysql trabaja en el puerto 3306
6. KEY = "algun_texto" # Ingresa un texto aleatorio para el key principal de la API.
7. SECRET = "llave_secreta" # Ingresa un texto como tu llave secreta para la API.

## Endpoints

### Auth
- **GET** `/api/v1/auth/`: Gestiona la seguridad del API basado en obtener un web token disponible por 1 hora.

### Ubicaciones
- **POST** `/api/v1/locations/`: Gestiona una nueva ubicación.

### Categorías
- **POST** `/api/v1/categories/`: Gestiona una nueva categoría.

### Recomendaciones
- **GET** `/api/v1/recommendations/`: Obtiene 10 combinaciones de ubicación y categoría que no han sido revisadas en los últimos 30 días o nunca hayan sido gestionadas.

la documentación general del API la puedes acceder desde https://URL_YOUR_PROJECT/docs

## Instalación y Ejecución

1. Clona el repositorio.
   https://github.com/jandresbc/map_my_world_api
2. Crea un entorno virtual y activalo.
   ```bash
   venv .venv
   .venv/Scrtips/activate # windows Powershell
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
4. Crea la estructura de las tablas en el motor de base de datos. Antes de este paso debes tener configurado el archivo .env con las variables necesarias de conexión a Mysql.
   ```bash
   python -m app.main # para crear los modelos en la base de datos.
   python -m app.main --mode drop_tables # para eliminar todos los modelos de la base de datos.
4. En un entorno local ejecuta el siguiente instrucción para correr el api.
   ```bash
   python function_app.py


### Despliegue

El API está configurada para desplegarse en una azure_functions. Desde tu proyecto de VSCode debes tener instalada la extensión oficial de Azure Functions y una cuenta en Azure. Con esto podrás crear una azure functions y dándole click en Deploy to function App podrás ejecutar el despliegue en Azure. Sin embargo el proyecto puede ejecutarse perfectamente dentro un entorno local con los pasos anteriores.

# Consideraciones

Asegurate antes de realizar el despliegue de tener una base de datos con los datos de conexión configurados en tu Azure function en sus variables de entorno, esto te permitirá desplegar tu funcion sin problemas.

## Descripción de los Directorios y Archivos

- **app/**: Contiene la lógica principal de la aplicación.
  - **main.py**: Punto de entrada de la aplicación, define la instancia de FastAPI y la configuración de enrutamiento.
  - **routes/**: Define los routers y las rutas del proyecto.
    - **v1/**: Puede tener diferentes versiones de la API.
      - **users.py**: Rutas relacionadas con usuarios.
      - **locations.py**: Rutas relacionadas con ubicaciones.
  - **core/**: Contiene la configuración central y funciones de seguridad.
    - **config.py**: Archivo de configuración para la aplicación.
    - **jwt.py**: Funciones relacionadas con JWT.
  - **models/**: Define los modelos de base de datos.
    - **user.py**: Modelo de usuarios.
    - **locations.py**: Modelo de ubicaciones.
  - **schemas/**: Define los esquemas (pydantic) utilizados para la validación de datos.
    - **user.py**: Esquema para usuarios.
    - **locations.py**: Esquema para ubicaciones.
  - **cruds/**: Contiene las operaciones CRUD.
    - **user.py**: Operaciones CRUD para usuarios.
    - **recommendations.py**: Operaciones CRUD para recomendaciones.
  - **databases/**: Gestión de la base de datos.
    - **databases.py**: Definición base de la conexión a la base de datos.
  - **utils/**: Utilidades y funciones comunes.
    - **common.py**: Funciones comunes.
  - **tests/**: Contiene los tests del proyecto.
    - **test_user.py**: Tests para usuarios.
    - **test_item.py**: Tests para ítems.
    
- **.env**: Archivo para las variables de entorno.

- **.gitignore**: Define los archivos y directorios que Git debe ignorar.

- **README.md**: Documentación del proyecto.

- **requirements.txt**: Lista de dependencias del proyecto.

---