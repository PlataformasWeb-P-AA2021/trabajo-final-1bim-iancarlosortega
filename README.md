# Trabajo Final Primer Bimestre - Uso de SqlAlchemy

## **Problemática**

Dada la información de la carpeta ***data***, se tuvo que analizar el archivo que contenía informacion acerca establecimientos de las diferentes provincias del Ecuador. Una vez identificadas las entidades, se solicitaba generar las entidades haciendo uso del ORM **SqlAlquemy**. Con la creación de las entidades, ahora se necesita ingresar información en las mismas utilizando la data de los establecimientos, asignando los valores de acuerdo a la entidad correspondida. Finalmente con las tablas creadas y pobladas, se requería hacer una serie de consultas que se podrán observar en el apartado de **SOLUCIÓN**

## **Solución**

### **Analizar el contenido.**

Primeramente, para empezar con la solución del problema se analizó la data que consistía en un archivo CSV acerca de un listado de instituciones educativas, donde se determinó la existencia de 4 entidades y también los atributos de cada uno de las entidades.  
	
* **Provincia :** 
	* Código División Política Administrativa Provincia
	* Nombre de la provincia  
	
* **Cantón :** 
	* Código División Política Administrativa Cantón
	* Nombre del cantón
	
* **Parroquia :** 
	* Código División Política Administrativa Parroquia
	* Nombre de la parroquia  

* **Establecimiento :** 
	* Código AMIE
	* Nombre del establecimiento
	* Código del distrito
	* Sostenimiento
	* Tipo de educación
	* Modalidad
	* Jornada
	* Tipo de acceso
	* Número de estudiantes
	* Número de docentes

### **Generar las entidades.**

Para la generación de las entidades se utilizó SQLAlquemy, donde primero se importó todo lo necesario para poder utilizar las funcionalidades del mismo : 

`from sqlalchemy import create_engine`  
`from sqlalchemy.ext.declarative import declarative_base`  
`from sqlalchemy.orm import sessionmaker, relationship`    
`from sqlalchemy import Column, Integer, String, ForeignKey`  

Una vez importado todo lo necesario, se realizó la conexión con la base de datos que en este caso se utilizó **SQLite** :  

`# Se importa información del archivo configuracion`  
`from configuracion import cadena_base_datos`  
`# Se genera en enlace al gestor de base de datos`    
`engine = create_engine(cadena_base_datos)`  
`Base = declarative_base()` 

Con la conexión lista, se procedió a crear las entidades asignando el nombre de la tabla, la llave primaria, los atributos, las llaves foráneas y las relaciones como se muestra en el siguiente código de ejemplo :  

`class Canton(Base):`  
    `	# Nombre de la tabla`  
    `	__tablename__ = 'canton'`  
    `	# Llave primaria de la tabla canton`  
    `	id = Column(Integer, primary_key=True)`  
    `	# Atributo de la tabla`  
    `	nombre = Column(String(50))`  
    `	# Llave foranea con la entidad provincia haciendo referencia a su ID`  
    `	provincia_id = Column(Integer, ForeignKey('provincia.id'))`  
    `	# Relacion con la entidad provincia mediante 'cantones'`  
    `	provincia  = relationship("Provincia", back_populates = "cantones")`  
    `	# Relacion con la entidad parroquia mediante 'canton'`  
    `	parroquias = relationship("Parroquia", back_populates = "canton")`  
    `	def __repr__(self):`  
        `	return "Canton:\nNombre = %s - Id provincia = %s\n"% (`  
                          `	self.nombre, `  
                          `	self.provincia_id)`  

Para el resto de las entidades se siguió el mismo proceso, pero cambiando los atributos y relaciones de acuerdo a la entidad.

### **Ingresar la información en cada entidad creada.**

Para el ingreso de la información en cada entidad, al igual manera que en la creación de la entidad, primero se conectó a la base de datos y luego se realizó la lectura del archivo propuesto, utilizando la función **open()** propia de python y agregando el argumento "r" haciendo referencia que vamos utilizar el archivo para lectura(**r**ead). Además, del encoding "utf-8" para poder mostrar los caracteres especiales. 

`archivo = open("data/Listado-Instituciones-Educativas.csv", "r", encoding="utf-8")`  
`leer_archivo = archivo.readlines()`  

Dado a que el archivo venía con un encabezado se lo procedió a eliminar para que no interfiera en el ingreso de datos con la función **pop()**.  

`leer_archivo.pop(0)`  

Al momento de extraer la información necesaria para la entidad, existían datos repetidos por lo que primero se sacó los atributos asociados a la entidad y se colocó esos resultados dentro de un nuevo arreglo auxiliar, al cual utilizando la función **set()** se le eliminaron todos los datos repetidos.

`for provincia in leer_archivo:`  
    `provincia_array = provincia.split("|")`  
    `cadena_aux = "%s|%s" % (provincia_array[2], provincia_array[3])`  
    `array_aux.append(cadena_aux)`  
  
`resultado_provincias = list(set(array_aux))`  

Finalmente, teniendo como resultado un arreglo con todas las provincias sin ser repetidas, se procedió a ingresar los datos en la tabla utilizando **session.add()** y para confirmar la agregación de todos los datos : **session.commit()**  

`for provincia in resultado_provincias:`  
    `provincia_array = provincia.split("|")`  
    `p = Provincia(id = provincia_array[0], nombre = provincia_array[1])`  
    `session.add(p)`  
`session.commit()`  

Esta lógica se utilizó para las entidades de Provincia, Canton y Parroquia, ya que estas contaban con datos duplicados mientras que la entidad de Establecimiento no contaba con ningún dato duplicado por lo que no se necesito eliminar ninguna fila y únicamente ingresar los datos mediante un ciclo repetitivo **for**.  

### **Realizar consultas a las entidades creadas.**

* **Consulta 1 :**   
	* Todos los establecimientos de la provincia de Loja.  
	Debido a que esta consulta necesitaba la información de varias tablas se utilizó la función **join()** y para filtrar la información el método **filter()**  
	`establecimientos_provincias = session.query(Establecimiento) \`  
    `.join(Parroquia, Canton, Provincia) \`  
    `.filter(Provincia.nombre == "LOJA").all()`  

	* Todos los establecimientos del cantón de Loja.  
	Es el mismo proceso de la consulta anterior pero en esta consulta únicamente varía el filtro donde en lugar de ser "Provincia" pasa a ser "Canton".  
	`establecimientos_provincias = session.query(Establecimiento) \`  
    `.join(Parroquia, Canton, Provincia) \`  
    `.filter(Canton.nombre == "LOJA").all()`

* **Consulta 2 :**   
	* Las parroquias que tienen establecimientos únicamente en la jornada Nocturna.  
	Para esta consulta se utilizó **filter()** para especificar los establecimientos que únicamente tengan jornada Nocturna.  
	`parroquias_nocturnas = session.query(Parroquia).join(Establecimiento).filter \`  
    `(Establecimiento.jornada == "Nocturna").all()`  

	* Los cantones que tiene establecimientos como número de estudiantes tales como: 448, 450, 451, 454, 458, 459.  
	En el caso de esta consulta se utilizó el operador de **in_** ya que el valor tenía que estar dentro de una serie de números establecidos en un arreglo. Además del filtro para que el número de estudiantes este dentro de ese arreglo.  
	`cantones_estudiantes = session.query(Canton).join(Parroquia, Establecimiento) \`  
    `.filter(Establecimiento.num_estudiantes.in_ \`  
    `([448, 450, 451, 454, 458, 459])).all()`  

* **Consulta 3 :**   
	* Los cantones que tiene establecimientos con 0 número de profesores.  
	Para esta consulta únicamente se estableció el filtro en los establecimientos donde el número de docentes sea igual a 0.  
	`parroquias_profesores = session.query(Parroquia).join(Establecimiento).filter \`  
    `(Establecimiento.num_docentes == 0).all()`  

	* Los establecimientos que pertenecen a la parroquia Catacocha con estudiantes mayores o iguales a 21.  
	En esta consulta se establecieron 2 filtros estableciendo solo los establecimientos pertenecientes a "CATACOCHA" y también que el número de estudiantes de esos establecimientos sea mayor o igual a 21.  
	`establecimientos_catacocha = session.query(Establecimiento).join(Parroquia) \`  
    `.filter(Parroquia.nombre == "CATACOCHA", Establecimiento.num_estudiantes \`  
    `>= 21 ).all()`  

* **Consulta 4 :**   
	* Los establecimientos ordenados por número de estudiantes; que tengan más de 100 profesores.  
	Para esta consulta se realizó el filtro donde los establecimientos tengan un número de docentes mayor a 100 y que el resultado sea ordenado por el número de estudiantes, para lo cual se utilizó la función  **order_by**.   
	`establecimientos_estudiantes = session.query(Establecimiento).filter \`  
    `(Establecimiento.num_docentes > 100).order_by \`  
    `(Establecimiento.num_estudiantes).all()`  

	* Los establecimientos ordenados por número de profesores; que tengan más de 100 profesores.  
	Esta consulta es similar a la anterior con la única diferencia que los resultados son ordenados por el número de docentes.  
	`establecimientos_docentes = session.query(Establecimiento).filter \`  
    `(Establecimiento.num_docentes > 100).order_by \`  
    `(Establecimiento.num_docentes).all()`  

* **Consulta 5 :**   
	* Los establecimientos ordenados por nombre de parroquia que tengan más de 20 profesores y la cadena "Permanente" en tipo de educación.  
	Para esta consulta se realizaron 2 filtros, uno para el número de docentes mayor a 20 y otro para que el tipo de educación debe ser igual a "Permanente". Finalmente, los resultados obtenidos ordenarlos por el nombre de la parroquia utilizando el **order_by**.    
	`establecimientos_permanente = session.query(Establecimiento).join(Parroquia) \`  
    `.filter(Establecimiento.num_docentes > 20, Establecimiento.tipo_educacion \`  
    `== "Permanente").order_by(Parroquia.nombre).all()`  

	* Todos los establecimientos ordenados por sostenimiento y tengan código de distrito 11D02.  
	En esta última consulta se estableció el filtro donde el código del distrito debe ser igual a "11D02" y los resultados ordenados por el sostenimiento de los establecimientos..  
	`establecimientos = session.query(Establecimiento) \`  
    `.filter(Establecimiento.cod_distrito == "11D02").order_by \`  
    `(Establecimiento.sostenimiento).all()`  
