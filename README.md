# AE1_M7_grupal
M7 AE1 grupal

Grupo 1

Creamos el modelo de productos, y formulario de registro de productos. Y los templates asociados formulario de registro, catálogo de productos,
lista de productos(tabla). 

Modificamos el admin importando la libreria django-admin-interface. Le incluimos el logo y modificamos las vistas de los productos con filtros en el admin.
Para agregar las imagenes importamos la libreria pillow.

Pasos para instalacion repositorio:
***********************************

- Clonar el repositorio
- Crear el entorno virtual
- Instalar el archivo de requirements.txt
- Hacer las migraciones, makemigrations y luego migrate.
- Crear el superusuario o proceder a cargar el archivo de datos que usamos el que nombramos data.json
- Aplicar el comando migrate.
- Y por ultimo correr el servidor con python manage.py runserver.

NOTA: Se nos presentó un problema al intentar cargar los datos de las base de datos en otro equipo (error: contenttypes). Lo solucionamos ingresando a la shell
de django, y ejecutando:

from django.contrib.contenttypes.models import ContentType
ContentType.objects.all().delete()
quit()
