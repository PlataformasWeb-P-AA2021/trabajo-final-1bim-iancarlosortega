from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Se importa la clase(s) del archivo genera_tablas
from genera_tablas import Establecimiento

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

for establecimiento in leer_archivo:

    # Separar el string en un arreglo
    establecimiento_array = establecimiento.split("|")

    # Ingresar los datos del CSV en la base de datos en la entidad 
    # establecimiento
    e = Establecimiento(nombre = establecimiento_array[1], 
                    cod_amie = establecimiento_array[0], 
                    cod_distrito = establecimiento_array[8],
                    sostenimiento = establecimiento_array[9],
                    tipo_educacion = establecimiento_array[10],
                    modalidad = establecimiento_array[11],
                    jornada = establecimiento_array[12],
                    acceso = establecimiento_array[13],
                    num_estudiantes = establecimiento_array[14],
                    num_docentes = establecimiento_array[15],
                    parroquia_id = establecimiento_array[6])
    session.add(e)

session.commit()