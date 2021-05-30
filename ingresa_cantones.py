from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Se importa la clase(s) del archivo genera_tablas
from genera_tablas import Canton

# Se importa información del archivo configuracion
from configuracion import cadena_base_datos

# Se genera enlace al gestor de base de datos
# Para el ejemplo se usa la base de datos SQLite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# leer el archivo de establecimientos

archivo = open("data/Listado-Instituciones-Educativas.csv", "r", \
    encoding="utf-8")

leer_archivo = archivo.readlines()

# Eliminar el encabezado del CSV
leer_archivo.pop(0)

# Variables auxiliares
cadena_aux = ""
array_aux = []

# Limpieza del archivo para insertar los cantones
for canton in leer_archivo:

    # Separar el string en un arreglo
    canton_array = canton.split("|")

    # Preparar un string con la informacion necesaria para el canton
    cadena_aux = "%s|%s|%s" % (canton_array[2], canton_array[4], \
        canton_array[5])

    # Agregar el string preparado a un arreglo auxiliar
    array_aux.append(cadena_aux)

# Eliminar los valores duplicados del arreglo
resultado_cantones = list(set(array_aux))

for canton in resultado_cantones:

    # Separar el string en un arreglo
    canton_array = canton.split("|")

    # Ingresar los datos del CSV en la base de datos en la entidad Canton
    c = Canton(id = canton_array[1], nombre = canton_array[2], \
        provincia_id = canton_array[0])
    session.add(c)

session.commit()