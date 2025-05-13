import pyodbc
import tkinter as tk
from tkinter import messagebox

# Conexión a SQL Server usando Autenticación de Windows
def get_connection():
    server = 'LAPTOP-M6RT9JJF\\SQLEXPRESS'
    database = 'Supermarket'
    conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    return pyodbc.connect(conn_str)

# Función para insertar un pedido
def insertar():
    id_cliente = entry_cliente.get()
    fecha = entry_fecha.get()

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Pedidos (ID_Cliente, Fecha) VALUES (?, ?)", (id_cliente, fecha))
        conn.commit()
        output.insert(tk.END, "Pedido insertado correctamente.\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        if 'conn' in locals() and conn.connected:
            conn.close()

# Consultar pedidos
def consultar():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Pedidos")
        rows = cursor.fetchall()
        output.delete(1.0, tk.END)
        for row in rows:
            output.insert(tk.END, f"{row}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        if 'conn' in locals() and conn.connected:
            conn.close()

# Actualizar pedido
def actualizar():
    id_pedido = entry_id.get()
    id_cliente = entry_cliente.get()
    fecha = entry_fecha.get()

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE Pedidos SET ID_Cliente = ?, Fecha = ? WHERE ID_Pedido = ?", (id_cliente, fecha, id_pedido))
        conn.commit()
        output.insert(tk.END, "Pedido actualizado.\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        if 'conn' in locals() and conn.connected:
            conn.close()

# Eliminar pedido
def eliminar():
    id_pedido = entry_id.get()

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Pedidos WHERE ID_Pedido = ?", (id_pedido,))
        conn.commit()
        output.insert(tk.END, "Pedido eliminado.\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        if 'conn' in locals() and conn.connected:
            conn.close()

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