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
mycursor.execute("CREATE DATABASE mydatabase")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
  database = "mydatabase"
)


#######################################
#Mostrar bases de datos
#######################################
mycursor.execute("SHOW DATABASES")
#Imprimi
for x in mycursor:
  print(x)

#######################################
# Crear una tabla
#######################################
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#######################################
#Mostrar las tablas
#######################################
mycursor.execute("SHOW TABLES")

#Imprimir
for x in mycursor:
  print(x)

#######################################
# Popular la tabla
#######################################
# formato sql
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# variable para incresar en mysql
val = ("John", "Highway 21")
mycursor.execute(sql, val)

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
# formato sql
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# variables
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

#Hacer commit
mydb.commit()

#######################################
# Popular la tabla desde archivos .csv
#######################################
import pandas as pd
# leer el archivo
data = pd.csv('file.txt') # header, names

# para cada linea insertar en Mysql
for row in data.iterrows():
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    # variable para incresar en mysql
    val = row # los valores tienen que ser los que quieras inserar
    mycursor.execute(sql, val)

mydb.commit()

#######################################
# Usando sqlalchemy
#######################################
# pip install SQLAlchemy
# conda install -c anaconda sqlalchemy
import sqlalchemy

# conexion para sqlalchemy
# mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:root@localhost[8889]/')

# leer el csv
data = pd.csv('file.txt') # checar nombres de columnas igual a la tabla en MySQL
# inserar en la tabla
data.to_sql('customers', con = engine)
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
