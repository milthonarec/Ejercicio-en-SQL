-- Crear la base de datos
CREATE DATABASE Supermarket;
GO

-- Usar la base de datos
USE Supermarket;
GO

-- Crear la tabla Pedidos
CREATE TABLE Pedidos (
    ID_Pedido INT IDENTITY(1,1) PRIMARY KEY,
    ID_Cliente INT NOT NULL,
    Fecha DATE NOT NULL
);
GO
