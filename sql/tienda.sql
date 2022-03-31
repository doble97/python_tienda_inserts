drop DATABASE if EXISTS `Tienda`;
CREATE DATABASE Tienda;
USE Tienda;
CREATE TABLE Proveedores(
    pk_nif varchar(9) PRIMARY KEY,
    ceo VARCHAR(50) NOT NULL,
    nombre_empresa varchar(50)
);
CREATE TABLE Trabajadores(
    pk_dni varchar(9) PRIMARY KEY,
    fecha_contratacion date not null,
    uk_nss varchar(12) not null UNIQUE,
    fecha_nacimiento date,
    nombre varchar(50) not null,
    sueldo numeric(6,2) not null DEFAULT '965.00'
);
CREATE TABLE Clientes(
    pk_id int auto_increment PRIMARY KEY,
    nombre varchar(50)
);

CREATE TABLE Productos(
    pk_id int auto_increment PRIMARY KEY,
    stock int DEFAULT 99,
    nombre varchar(30) not null,
    precio numeric(5,2) not null
);
CREATE TABLE Compras(
    pk_codigo int auto_increment PRIMARY KEY,
    precio double not null,
    fk_cliente int,
    CONSTRAINT FK_CLIENTES_COMPRAS FOREIGN KEY (fk_cliente) REFERENCES Clientes(pk_id)
);
CREATE TABLE GestionPedidos(
    dni_trabajador varchar(9),
    nif_proveedor varchar(9),
    id_producto int,
    uk_codigo int auto_increment UNIQUE,
    PRIMARY KEY(dni_trabajador, nif_proveedor, id_producto),
    FOREIGN KEY(dni_trabajador) REFERENCES Trabajadores(pk_dni),
    FOREIGN KEY(nif_proveedor) REFERENCES Proveedores(pk_nif),
    FOREIGN KEY(id_producto) REFERENCES Productos(pk_id)

);

CREATE TABLE TrabajadoresJefes(
    pk_dni_trabajador varchar(9) PRIMARY KEY,
    fk_dni_jefe varchar(9),
    FOREIGN KEY(fk_dni_jefe) REFERENCES Trabajadores(pk_dni),
    FOREIGN KEY(pk_dni_trabajador) REFERENCES Trabajadores(pk_dni)
);

CREATE TABLE Ventas(
    dni_trabajador varchar(9),
    id_cliente int,
    pk_id int PRIMARY KEY,
    fecha_compra date not null,
    fecha_max_devolucion date,
    FOREIGN KEY(dni_trabajador) REFERENCES Trabajadores(pk_dni),
    FOREIGN KEY(id_cliente) REFERENCES Clientes(pk_id),
    CONSTRAINT FK_COMPRAS_VENTAS FOREIGN KEY(pk_id) REFERENCES Compras(pk_codigo)
);

CREATE TABLE ClientesProductos(
    id_cliente int,
    id_producto int,
    FOREIGN KEY (id_cliente) REFERENCES Clientes(pk_id),
    FOREIGN KEY(id_producto) REFERENCES Productos(pk_id),
    PRIMARY KEY (id_cliente, id_producto)
);
-- 9

CREATE TABLE Camisetas(
    pk_id int PRIMARY KEY,
    tela varchar(15) not null,
    FOREIGN KEY(pk_id) REFERENCES Productos(pk_id)
);

CREATE TABLE Pantalones(
    pk_id int PRIMARY KEY,
    tela varchar(15) not null,
    FOREIGN KEY(pk_id) REFERENCES Productos(pk_id)
);
CREATE TABLE Accesorios(
    pk_id int PRIMARY KEY,
    material varchar(20) not null,
    talla varchar(8) not null DEFAULT 'Unica',
    FOREIGN KEY(pk_id) REFERENCES Productos(pk_id)
);

CREATE TABLE ProductosCompras(
    id_producto int,
    cod_compra int,
    FOREIGN KEY(id_producto) REFERENCES Productos(pk_id),
    CONSTRAINT FK_COMPRAS_PRODUCTOSCOMPRAS FOREIGN KEY(cod_compra) REFERENCES Compras(pk_codigo),
    PRIMARY KEY(id_producto, cod_compra)
);
-- borrar ClientesProductos
drop table ClientesProductos;

-- alter table
alter table ProductosCompras drop constraint FK_COMPRAS_PRODUCTOSCOMPRAS;
alter table Ventas drop constraint FK_COMPRAS_VENTAS;
alter table Ventas modify column pk_id int auto_increment;
drop table Compras;
alter table Ventas add cod_producto int;
alter table Ventas add CONSTRAINT FK_PRODUCTOS_VENTAS FOREIGN KEY(cod_producto) REFERENCES Productos(pk_id);
-- relacion productoscompras con ventas
alter table ProductosCompras add CONSTRAINT FK_VENTAS_PRODUCTOSCOMPRAS FOREIGN KEY(cod_compra) REFERENCES Ventas(pk_id);

-- 
alter table Clientes add apellidos varchar(60);
alter table Clientes add f_alta date;
alter table Clientes add f_nac date;
alter table Clientes add dni varchar(9) UNIQUE;
-- Cambiando tabla Trabajadores
alter table Trabajadores add apellidos varchar(100);
alter table Trabajadores modify column sueldo decimal(6,2) default 1000.00;