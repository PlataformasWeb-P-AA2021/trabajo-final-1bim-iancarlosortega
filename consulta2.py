from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Se importa la clase(s) del archivo genera_tablas
from genera_tablas import Establecimiento, Parroquia, Canton

# Se importa información del archivo configuracion
from configuracion import cadena_base_datos

# Se genera enlace al gestor de base de datos
# Para el ejemplo se usa la base de datos SQLite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Consulta 2

# Las parroquias que tienen establecimientos únicamente en la jornada Nocturna

parroquias_nocturnas = session.query(Parroquia).join(Establecimiento).filter \
    (Establecimiento.jornada == "Nocturna").all()

print("-------------- CONSULTA 2 PARROQUIAS ------------------ ")
for p in parroquias_nocturnas: 
    print(p) 

# Los cantones que tiene establecimientos como número de estudiantes tales 
# como: 448, 450, 451, 454, 458, 459

cantones_estudiantes = session.query(Canton).join(Parroquia, Establecimiento) \
    .filter(Establecimiento.num_estudiantes.in_ \
    ([448, 450, 451, 454, 458, 459])).all()

print("-------------- CONSULTA 2 CANTONES ------------------ ")
for c in cantones_estudiantes: 
    print(c) 