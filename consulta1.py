from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Se importa la clase(s) del archivo genera_tablas
from genera_tablas import Establecimiento, Provincia, Parroquia, Canton

# Se importa información del archivo configuracion
from configuracion import cadena_base_datos

# Se genera enlace al gestor de base de datos
# Para el ejemplo se usa la base de datos SQLite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()

# Consulta 1

# Todos los establecimientos de la provincia de Loja.

establecimientos_provincias = session.query(Establecimiento) \
    .join(Parroquia, Canton, Provincia) \
    .filter(Provincia.nombre == "LOJA").all()

print("-------------- CONSULTA 1 PROVINCIAS ------------------ ")
for e_p in establecimientos_provincias: 
    print(e_p) 

# Todos los establecimientos del canton de Loja.

establecimientos_cantones = session.query(Establecimiento) \
    .join(Parroquia, Canton, Provincia) \
    .filter(Canton.nombre == "LOJA").all()

print("-------------- CONSULTA 1 CANTONES ------------------ ")
for e_c in establecimientos_cantones: 
    print(e_c) 