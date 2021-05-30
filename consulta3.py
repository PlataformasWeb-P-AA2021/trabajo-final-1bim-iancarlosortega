from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Se importa la clase(s) del archivo genera_tablas
from genera_tablas import Establecimiento, Parroquia

# Se importa información del archivo configuracion
from configuracion import cadena_base_datos

# Se genera enlace al gestor de base de datos
# Para el ejemplo se usa la base de datos SQLite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Consulta 3

# Los cantones que tiene establecimientos con 0 número de profesores

parroquias_profesores = session.query(Parroquia).join(Establecimiento).filter \
    (Establecimiento.num_docentes == 0).all()

print("-------------- CONSULTA 3 PARROQUIAS ------------------ ")
for p in parroquias_profesores: 
    print(p) 

# Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes 
# mayores o iguales a 21

establecimientos_catacocha = session.query(Establecimiento).join(Parroquia) \
    .filter(Parroquia.nombre == "CATACOCHA", Establecimiento.num_estudiantes \
    >= 21 ).all()

print("-------------- CONSULTA 3 CANTONES ------------------ ")
for c in establecimientos_catacocha: 
    print(c) 