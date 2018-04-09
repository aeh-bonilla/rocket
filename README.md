# rocket
Ejemplo de API utilizando framework Django 1.10.4 y python 2.7

Esta aplicación consta de los siguientes archivos:

__init__.py : archivo de inicialización de la aplicación

models.py: Archivo en donde se declara el modelo Tasks que la entidad donde se almacenara la información de las tareas dentro de la db.

settings.py: Archivo de configuración de la aplicación, aquí se declara las cadenas de conexión a la base de datos, las clases de 
middleware en caso de que la app lo requiera e información sobre la localización de los archivos estáticos y templates que pudieran utilizarse.

urls.py: En este archivo se declaran las urls a las que se debe acceder para utilizar las diversas funcionalidades de la aplicación. Para nuestro caso se declaran las URL donde se consumirán los servicios para:

- Inicializar lista de tareas.
- Agregar tarea
- Actualizar tarea
- Eliminar tarea
- Recuperar lista de tareas por status
- Recuperar lista de tareas por descripción

views.py: Es en este archivo en donde se codifica la implementación de las diferentes funcionalidades que posee la app.
wsgi.py: Que es nos servirá como interfase para el despliegue de la aplicación.
test.py: En este archivo se encuentra la definición de pruebas automatizadas simples para el test de los servicios que agregan, eliminan y actualizan una tarea.

Modo de Empleo:

Creación de la base de datos y usuario:
Para poder ejecutar la aplicación primero será necesario crear la base de datos rocket_db dentro de la instancia de base de datos Postgres que tengamos instalada dentro de nuestro equipo,
para hacer estos accederemos con el usuario postgres y ejecutaremos los siguientes comandos:

create database rocket_db;
create user usr_rocket;
alter user usr_rocket with encrypted password 'St7Spev*';
grant all privileges on database rocket_db to usr_rocket;
alter user usr_rocket createdb;

Descarga del código fuente del proyecto y ejecución:

Para descargar el código de la app en nuestro equipo deberemos ejecutamos el comando 'git clone https://github.com/aeh-bonilla/rocket.git', 
ahora que el código ha sido descargado nos colocaremos en la carpeta raíz del proyecto, para eso ejecutamos el comando:

$ cd rocket

Una vez dentro de la raíz del proyecto ejecutamos el siguiente comando Para identificar los modelos que deben ser trasladados a la base de datos como entidades

$ python manage.py makemigrations rocket

Posteriormente ejecutaremos el comando que se muestra a continuación para asentar los cambios dentro de la base de datos

$ python manage.py migrate rocket

Ya que se tienen los objetos necesarios dentro de la base de datos, ejecutaremos la aplicación con el siguiente comando

$ python manage.py runserver 0.0.0.0:8000

Una vez que el servidor está en ejecución abriremos una segunda consola para ejecutar las pruebas de la aplicación.

Para probar los servicios add_task, delete_task y update_task se debe ejecutar el comando:

$ python manage.py test
