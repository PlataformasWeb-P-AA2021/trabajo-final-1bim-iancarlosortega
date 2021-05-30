from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

# Se importa información del archivo configuracion
from configuracion import cadena_base_datos

# Se genera en enlace al gestor de base de datos
# Para el ejemplo se usa la base de datos SQLite
engine = create_engine(cadena_base_datos)

Base = declarative_base()

# Se crea la entidad Provincia con sus respectivos atributos
class Provincia(Base):
    # Nombre de la tabla
    __tablename__ = 'provincia'
    # Llave primaria de la tabla provincia
    id = Column(Integer, primary_key=True)
    # Atributo de la tabla
    nombre = Column(String(50))
    # Relacion con la entidad canton mediante 'provincia'
    cantones = relationship("Canton", back_populates="provincia")

    def __repr__(self):
        return "Provincia:\nNombre = %s\n"% (
                          self.nombre)

# Se crea la entidad Canton con sus respectivos atributos
class Canton(Base):
    # Nombre de la tabla
    __tablename__ = 'canton'
    # Llave primaria de la tabla canton
    id = Column(Integer, primary_key=True)
    # Atributo de la tabla
    nombre = Column(String(50))
    # Llave foranea con la entidad provincia haciendo referencia a su ID
    provincia_id = Column(Integer, ForeignKey('provincia.id'))
    # Relacion con la entidad provincia mediante 'cantones'
    provincia  = relationship("Provincia", back_populates = "cantones")
    # Relacion con la entidad parroquia mediante 'canton'
    parroquias = relationship("Parroquia", back_populates = "canton")

    def __repr__(self):
        return "Canton:\nNombre = %s - Id provincia = %s\n"% (
                          self.nombre, 
                          self.provincia_id)

# Se crea la entidad Parroquia con sus respectivos atributos
class Parroquia(Base):
    # Nombre de la tabla
    __tablename__ = 'parroquia'
    # Llave primaria de la tabla parroquia
    id = Column(Integer, primary_key=True)
    # Atributo de la tabla
    nombre = Column(String(50))
    # Llave foranea con la entidad canton haciendo referencia a su ID
    canton_id = Column(Integer, ForeignKey('canton.id'))
    # Relacion con la entidad canton mediante 'parroquias'
    canton = relationship("Canton", back_populates="parroquias")
    # Relacion con la entidad establecimientos mediante 'parroquia'
    establecimientos = relationship("Establecimiento", \
         back_populates="parroquia")

    def __repr__(self):
        return "Parroquia:\nNombre = %s - Id canton = %s\n"% (
                          self.nombre, 
                          self.canton_id)

# Se crea la entidad Establecimiento con sus respectivos atributos
class Establecimiento(Base):
    # Nombre de la tabla
    __tablename__ = 'establecimiento'
    # Llave primaria de la tabla establecimiento
    id = Column(Integer, primary_key=True)
    # Atributos de la tabla
    nombre = Column(String(50))
    cod_amie = Column(String(50))
    cod_distrito = Column(String(50))
    sostenimiento = Column(String(50))
    tipo_educacion = Column(String(50))
    modalidad = Column(String(50))
    jornada = Column(String(50))
    acceso = Column(String(50))
    num_estudiantes = Column(Integer)
    num_docentes = Column(Integer)
    # Llave foranea con la entidad parroquia haciendo referencia a su ID
    parroquia_id = Column(Integer, ForeignKey('parroquia.id'))
    # Relacion con la entidad parroquia mediante 'establecimientos'
    parroquia = relationship("Parroquia", back_populates="establecimientos")

    def __repr__(self):
        return "Establecimiento:\nNombre = %s - Código AMIE = %s - "\
            "Id parroquia = %s - Código distrito = %s - Sostenimiento = %s - "\
            "Tipo de Educación = %s - Modalidad = %s - Jornada = %s - "\
            "Acceso = %s - Número de estudiantes = %s - "\
            "Número de docentes = %s\n" % (
                          self.nombre, 
                          self.cod_amie, 
                          self.parroquia_id, 
                          self.cod_distrito, 
                          self.sostenimiento, 
                          self.tipo_educacion, 
                          self.modalidad, 
                          self.jornada, 
                          self.acceso, 
                          self.num_estudiantes, 
                          self.num_docentes)

Base.metadata.create_all(engine)
