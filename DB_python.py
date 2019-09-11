#######################################
#######################################
####### Python <3 Mysql
#######################################
#######################################
# Comandos utiles y basicos en python para conectarse con Mysql


#######################################
import mysql.connector
#######################################
# conda install -c anaconda mysql-connector-python
# pip install mysql-connector-python

#######################################
# Establecer la concexion
#######################################
mydb = mysql.connector.connect(
  host="localhost", # o IP
  user="root",
  passwd="root",
  port = '8889' #3306
  #database = "DB"
)

mycursor = mydb.cursor()

#######################################
# metodo execute para ejecutar acciones dentro de mysql
#######################################
#mycursor.execute("CREATE DATABASE TraitsQTLs_Genetica")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database = "TraitsQTLs_Genetica",
  port = '8889'
)

mycursor = mydb.cursor()

#######################################
#Mostrar bases de datos
#######################################
mycursor.execute("SHOW TABLES")
#Imprimi
for x in mycursor:
  print(x)

#######################################
# Crear una tabla
#######################################
sqlDatosGenerales = "CREATE TABLE DatosGenerales ( \
  persona_id INT AUTO_INCREMENT PRIMARY KEY, \
  nombre VARCHAR(255), \
  sexo CHAR(1),\
  edad INT(2), \
  estado  VARCHAR(10)\
  )"

mycursor.execute(sqlDatosGenerales)


sqlMediciones = "CREATE TABLE Mediciones ( \
  medicion_id INT AUTO_INCREMENT PRIMARY KEY, \
  tipo VARCHAR(16), \
  medida FLOAT, \
  persona_id INT, \
  CONSTRAINT persona_fk \
  FOREIGN KEY (persona_id) \
     REFERENCES DatosGenerales(persona_id) \
  )"

mycursor.execute(sqlMediciones)
#mycursor.execute("Drop Table Mediciones")

#######################################
#Mostrar las tablas
#######################################
mycursor.execute("SHOW TABLES")

#Imprimir
for x in mycursor:
  print(x)

#######################################
# Poblar la tabla
#######################################
#######################################
# DatosGenerales
#######################################
# formato sql
sql = "INSERT INTO DatosGenerales (nombre, sexo, edad, estado) VALUES (%s, %s, %s, %s)"
# variable para incresar en mysql
val = ("Mario Santana", "M","35","CDMX")
mycursor.execute(sql, val)

sql2 = "SELECT * FROM DatosGenerales"

#######################################
# Mediciones
#######################################
sqlmed = "INSERT INTO Mediciones (tipo,medida,persona_id) VALUES (%s,%s,%s)"
mycursor.execute(sqlmed, val)

#######################################
# Super importante hacer COMMIT!!!!!!!!
#######################################
#Importate hacer commit
mydb.commit()

#######################################
# Contar cuantos commit se hicieron con rowcount
#######################################
print(mycursor.rowcount, "record inserted.")

#######################################
# Popular la tabla con más de un valor
#######################################
# libreria para checar nan
import math

# Valor de la altura para cada individuo
val = []
altura = data.iloc[0,4]
val = [["altura",altura,1]]

# Valores de la frente para cada individuo
medic_frente = list(data.iloc[0,5:10])
for i in medic_frente:
    if math.isnan(i):
        print ("No hay medicion de frente")
    else:
        val.append(["frente",i,1])

# Valores del brazo para cada individuo
medic_brazo = data.iloc[0,11:16]
for i in medic_brazo:
        if math.isnan(i):
            print ("No hay medicion de brazo")
        else:
            val.append(["brazo",i,1])

# Lenguaje SQL para insertar datos en la tabla de Mediciones
sqlmed ="INSERT INTO Mediciones (tipo,medida,persona_id) VALUES (%s, %s, %s)"
if len(val) <= 1:
    mycursor.execute(sqlmed, val[0])
else:
    mycursor.executemany(sqlmed, val)

#Hacer commit
mydb.commit()

#######################################
# Popular la tabla desde archivos .csv
#######################################
import pandas as pd
# leer el archivo
data = pd.read_csv('Mediciones2.csv') # header, names

d = data.iloc[1:,:]

# para cada linea insertar en Mysql

val = []
# Lenguaje SQL para insertar datos en la tabla de customers
sql = "INSERT INTO DatosGenerales (nombre, sexo, edad, estado) VALUES (%s, %s, %s, %s)"
# Lenguaje SQL para insertar datos en la tabla de Mediciones
sqlmed ="INSERT INTO Mediciones (tipo,medida,persona_id) VALUES (%s, %s, %s)"

for row in d.iterrows():
    # variable para incresar en mysql
    val_cus = list(row[1][0:4]) # los valores tienen que ser los que quieras inserar
    mycursor.execute(sql, val_cus) #Importar valores en customers
    # Valor de la altura para cada individuo
    altura = row[1][4]
    val = [["altura",altura,row[0]+1]] # le sumo 1 porque ya existe Mario
    # Valores de la frente para cada individuo
    medic_frente = list(row[1][5:10])
    for i in medic_frente:
        if math.isnan(i):
            print ("No hay medicion de frente")
        else:
            val.append(["frente",i,row[0]+1])
    #print(val)
    # Valores del brazo para cada individuo
    medic_brazo = list(row[1][11:16])
    for ii in medic_brazo:
        if math.isnan(ii):
            print ("No hay medicion de brazo")
        else:
            val.append(["brazo",ii,row[0]+1])
    #print(val)
    if len(val) == 1:
        mycursor.execute(sqlmed, val[0])
    else:
        mycursor.executemany(sqlmed, val)



#Hacer commit
mydb.commit()


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database = "TraitsQTLs_Genetica",
  port = '8889'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * from DatosGenerales")
#mycursor.execute("SELECT tipo from Mediciones")
datosgenerales = mycursor.fetchall()
#mycursor.execute("SHOW columns from DatosGenerales")

mycursor.execute("SELECT medida from Mediciones \
WHERE tipo ='altura'")
mediciones = mycursor.fetchall()

mycursor.execute("SELECT medida from Mediciones \
INNER JOIN DatosGenerales on DatosGenerales.persona_id=Mediciones.persona_id \
WHERE tipo ='altura'\
AND DatosGenerales.sexo = 'H'\
")
mediciones = mycursor.fetchall()

m = list()
for i in mediciones:
    m.append(i[0])


#######################################
# Usando sqlalchemy
#######################################
# pip install SQLAlchemy
# conda install -c anaconda sqlalchemy
import sqlalchemy

# conexion para sqlalchemy
# mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:root@localhost[8889]/TraitsQTLs_Genetica')

# leer el csv
data = pd.csv('file.txt') # checar nombres de columnas igual a la tabla en MySQL
# inserar en la tabla
data.to_sql('DatosGenerales', con = engine)
#######################################


#######################################
# Ingresar la tabla directo a MySQL
#######################################
## SQL
#LOAD DATA LOCAL INFILE '/file.csv'
#INTO TABLE customers
#FIELDS TERMINATED BY ','
#LINES TERMINATED BY '\n'
#IGNORE 1 ROWS # header
#(name,address)
#;
sql = "LOAD DATA LOCAL INFILE 'file.csv' \
INTO TABLE customers \
FIELDS TERMINATED BY ',' \
LINES TERMINATED BY '\n' \
IGNORE 1 ROWS # header\
(name,address)"

mycursor.execute(sql)


#######################################
# regresar valores
#######################################
#Para regresar los valores
mycursor.execute("SELECT * FROM customers")

#Guardar los valores
myresult = mycursor.fetchall()

for x in myresult:
  print(x)



### Usando sqlalchemy
# Para leer tablas
df = pd.read_sql_table('customers',engine) # mydb ?
# se le puede pasar queries
df = pd.read_sql_query("select name from customers",engine)
