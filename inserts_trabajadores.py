import csv
import mysql.connector
import fechas as f

# abrir conexion a bd
bd_conn = mysql.connector.connect(
    host='localhost',
    user='jorge',
    password='alumno2021',
    database='Tienda'
)

cursor = bd_conn.cursor()
sentencia = 'insert into Trabajadores(pk_dni, nombre, apellidos, sueldo, uk_nss, fecha_nacimiento, fecha_contratacion) values (%s,%s,%s,%s,%s,%s,%s)'
# abrir y leer fichero
size_csv=0
with open('csv/trabajadores.csv') as file:
    reader_csv = csv.reader(file)
    header = []
    header = next(reader_csv)
    print(header)
    for row in reader_csv:
        row.append(f.getFechaNacimiento())
        row.append(f.getFechaAlta())
        cursor.execute(sentencia, row)
        size_csv = size_csv+1
bd_conn.commit()
print(size_csv, 'records inserted')