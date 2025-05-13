-- Crear base de datos
CREATE DATABASE Supermarket;
GO

-- Usar la base de datos
USE Supermarket;
GO

-- Crear tabla de Clientes
CREATE TABLE Clientes (
    ID_Cliente INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100),
    Direccion NVARCHAR(200),
    Telefono NVARCHAR(20)
);
GO

-- Crear tabla de Productos
CREATE TABLE Productos (
    ID_Producto INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100),
    Precio DECIMAL(10,2),
    Stock INT
);
GO

-- Crear tabla de Pedidos
CREATE TABLE Pedidos (
    ID_Pedido INT PRIMARY KEY IDENTITY(1,1),
    ID_Cliente INT,
    Fecha DATETIME,
    FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente)
);
GO

-- Crear tabla DetallePedido
CREATE TABLE DetallePedido (
    ID_Detalle INT PRIMARY KEY IDENTITY(1,1),
    ID_Pedido INT,
    ID_Producto INT,
    Cantidad INT,
    FOREIGN KEY (ID_Pedido) REFERENCES Pedidos(ID_Pedido),
    FOREIGN KEY (ID_Producto) REFERENCES Productos(ID_Producto)
);
GO