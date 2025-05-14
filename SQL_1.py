import pyodbc
import tkinter as tk
from tkinter import messagebox

# Conexión a SQL Server usando Autenticación de Windows
def get_connection():
    server = 'LAPTOP-M6RT9JJF'
    database = 'Supermarket'
    conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    return pyodbc.connect(conn_str)

# Función para insertar un pedido
def insertar():
    ID_Cliente = entry_cliente.get()
    Fecha = entry_fecha.get()
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Pedidos (ID_Cliente, Fecha) VALUES (?, ?)", (ID_Cliente, Fecha))
            conn.commit()
            output.insert(tk.END, "Pedido insertado correctamente.\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Consultar pedidos
def consultar():
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Pedidos")
            rows = cursor.fetchall()
            output.delete(1.0, tk.END)
            for row in rows:
                output.insert(tk.END, f"{row}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Actualizar pedido
def actualizar():
    ID_Pedido = entry_id.get()
    ID_Cliente = entry_cliente.get()
    Fecha = entry_fecha.get()
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE Pedidos SET ID_Cliente = ?, Fecha = ? WHERE ID_Pedido = ?", (ID_Cliente, Fecha, ID_Pedido))
            conn.commit()
            output.insert(tk.END, "Pedido actualizado.\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Eliminar pedido
def eliminar():
    ID_Pedido = entry_id.get()
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Pedidos WHERE ID_Pedido = ?", (ID_Pedido,))
            conn.commit()
            output.insert(tk.END, "Pedido eliminado.\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Interfaz gráfica
root = tk.Tk()
root.title("Gestión de Pedidos - Supermarket")

tk.Label(root, text="ID Pedido:").grid(row=0, column=0)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1)

tk.Label(root, text="ID Cliente:").grid(row=1, column=0)
entry_cliente = tk.Entry(root)
entry_cliente.grid(row=1, column=1)

tk.Label(root, text="Fecha (YYYY-MM-DD):").grid(row=2, column=0)
entry_fecha = tk.Entry(root)
entry_fecha.grid(row=2, column=1)

tk.Button(root, text="Insertar", command=insertar).grid(row=3, column=0)
tk.Button(root, text="Consultar", command=consultar).grid(row=3, column=1)
tk.Button(root, text="Actualizar", command=actualizar).grid(row=4, column=0)
tk.Button(root, text="Eliminar", command=eliminar).grid(row=4, column=1)

output = tk.Text(root, height=10, width=50)
output.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
