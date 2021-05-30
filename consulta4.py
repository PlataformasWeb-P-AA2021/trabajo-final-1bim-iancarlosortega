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

# Consulta 4

# Los establecimientos ordenados por número de estudiantes; que tengan más de
# 100 profesores.

establecimientos_estudiantes = session.query(Establecimiento).filter \
    (Establecimiento.num_docentes > 100).order_by \
    (Establecimiento.num_estudiantes).all()

print("-------------- CONSULTA 4 ESTABLECIMIENTOS ------------------ ")
for p in establecimientos_estudiantes: 
    print(p) 

# Los establecimientos ordenados por número de profesores; que tengan más de
# 100 profesores.

establecimientos_docentes = session.query(Establecimiento).filter \
    (Establecimiento.num_docentes > 100).order_by \
    (Establecimiento.num_docentes).all()

print("-------------- CONSULTA 4 ESTABLECIMIENTOS ------------------ ")
for c in establecimientos_docentes: 
    print(c) 