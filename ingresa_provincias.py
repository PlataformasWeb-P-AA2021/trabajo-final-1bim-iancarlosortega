from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Se importa la clase(s) del archivo genera_tablas
from genera_tablas import Provincia

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

# Limpieza del archivo para insertar las provincias
for provincia in leer_archivo:

    # Separar el string en un arreglo
    provincia_array = provincia.split("|")

    # Preparar un string con la informacion necesaria para la 
    # provincia
    cadena_aux = "%s|%s" % (provincia_array[2], provincia_array[3])

    # Agregar el string preparado a un arreglo auxiliar
    array_aux.append(cadena_aux)

# Eliminar los valores duplicados del arreglo
resultado_provincias = list(set(array_aux))

for provincia in resultado_provincias:

    # Separar el string en un arreglo
    provincia_array = provincia.split("|")

    # Ingresar los datos del CSV en la base de datos en la entidad Provincia
    p = Provincia(id = provincia_array[0], nombre = provincia_array[1])
    session.add(p)

session.commit()