from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Se importa la clase(s) del archivo genera_tablas
from genera_tablas import Parroquia

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

# Limpieza del archivo para insertar las parroquias
for parroquia in leer_archivo:

    # Separar el string en un arreglo
    parroquia_array = parroquia.split("|")

    # Preparar un string con la informacion necesaria para la 
    # parroquia
    cadena_aux = "%s|%s|%s" % (parroquia_array[4], parroquia_array[6], \
        parroquia_array[7])

    # Agregar el string preparado a un arreglo auxiliar
    array_aux.append(cadena_aux)

# Eliminar los valores duplicados del arreglo
resultado_parroquias = list(set(array_aux))

for parroquia in resultado_parroquias:

    # Separar el string en un arreglo
    parroquia_array = parroquia.split("|")

    # Ingresar los datos del CSV en la base de datos en la entidad Parroquia
    p = Parroquia(id = parroquia_array[1], nombre = parroquia_array[2], \
        canton_id = parroquia_array[0])
    session.add(p)

session.commit()