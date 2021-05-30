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

# Consulta 5

# Los establecimientos ordenados por nombre de parroquia que tengan más
# de 20 profesores y la cadena "Permanente" en tipo de educación.

establecimientos_permanente = session.query(Establecimiento).join(Parroquia) \
    .filter(Establecimiento.num_docentes > 20, Establecimiento.tipo_educacion \
    == "Permanente").order_by(Parroquia.nombre).all()

print("-------------- CONSULTA 5 ESTABLECIMIENTOS ------------------ ")
for p in establecimientos_permanente: 
    print(p) 

# Todos los establecimientos ordenados por sostenimiento y tengan código de
# distrito 11D02.

establecimientos = session.query(Establecimiento) \
    .filter(Establecimiento.cod_distrito == "11D02").order_by \
    (Establecimiento.sostenimiento).all()

print("-------------- CONSULTA 5 ESTABLECIMIENTOS ------------------ ")
for c in establecimientos: 
    print(c) 