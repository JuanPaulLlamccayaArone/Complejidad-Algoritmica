import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("UPCRutas")
        self.root.geometry("600x550")

        # Cargar el logo
        self.logo = PhotoImage(file="logo.png")
        # Cambiar tamaño del logo
        self.logo = self.logo.subsample(3, 3)

        self.create_form1()

    def create_form1(self):
        self.clear_frame()

        # Formulario 1: Ingreso de Nombre y Apellido
        self.label_logo = tk.Label(self.root, image=self.logo)
        self.label_logo.pack(pady=10)

        self.label_title = tk.Label(self.root, text="UPCRutas", font=("Arial", 18))
        self.label_title.pack(pady=5)

        self.label_name = tk.Label(self.root, text="Ingresa tu nombre")
        self.label_name.pack(pady=5)

        self.entry_name = tk.Entry(self.root)
        self.entry_name.pack(pady=5)

        self.label_lastname = tk.Label(self.root, text="Ingresa tu apellido")
        self.label_lastname.pack(pady=5)

        self.entry_lastname = tk.Entry(self.root)
        self.entry_lastname.pack(pady=5)

        self.btn_ingresar = tk.Button(self.root, text="Ingresar", command=self.validate_form1)
        self.btn_ingresar.pack(pady=20)

    def create_form2(self):
        self.clear_frame()

        # Formulario 2: Selección de Origen y Destino
        self.label_logo = tk.Label(self.root, image=self.logo)
        self.label_logo.pack(pady=10)

        self.label_title = tk.Label(self.root,
                                    text=f"Hola {self.name} {self.lastname} ::::::::::::::::::: Escoge la opción",
                                    font=("Arial", 10))
        self.label_title.pack(pady=5)

        self.label_origen = tk.Label(self.root, text="Ingrese Punto de Origen")
        self.label_origen.pack(pady=5)

        self.origen = ttk.Combobox(self.root, values=origen_options)
        self.origen.pack(pady=5)

        self.label_destino = tk.Label(self.root, text="Ingrese el punto de destino")
        self.label_destino.pack(pady=5)

        self.destino = ttk.Combobox(self.root, values=destino_options)
        self.destino.pack(pady=5)

        self.btn_buscar = tk.Button(self.root, text="Buscar", command=self.validate_form2)
        self.btn_buscar.pack(pady=20)

    def create_form3(self):
        self.clear_frame()

        # Formulario 3: Selección de Criterio
        self.label_logo = tk.Label(self.root, image=self.logo)
        self.label_logo.pack(pady=10)

        self.label_title = tk.Label(self.root, text=f"Hola {self.name} {self.lastname} Escoge la opción",
                                    font=("Arial", 10))
        self.label_title.pack(pady=5)

        self.label_criterio = tk.Label(self.root, text="Escoja")
        self.label_criterio.pack(pady=5)

        self.criterio = ttk.Combobox(self.root, values=["Distancia", "Precio", "Tiempo"])
        self.criterio.pack(pady=5)

        self.label_vista = tk.Label(self.root, text="Visualización")
        self.label_vista.pack(pady=5)

        self.grafo = PhotoImage(file="grafo-reducido.png")
        # Cambiar tamaño del logo
        self.grafo = self.grafo.subsample(7, 7)
        self.label_grafo = tk.Label(self.root, image=self.grafo)
        self.label_grafo.pack(pady=5)

        self.btn_visualizar = tk.Button(self.root, text="Buscar", command=self.show_visualizacion)
        self.btn_visualizar.pack(pady=10)

    def validate_form1(self):
        self.name = self.entry_name.get().strip()
        self.lastname = self.entry_lastname.get().strip()
        if self.name.isalpha() and self.lastname.isalpha():
            self.create_form2()
        else:
            messagebox.showerror("Error", "El nombre y apellido deben contener solo caracteres.")

    def validate_form2(self):
        origen = self.origen.get()
        destino = self.destino.get()
        if origen and destino and origen != destino:
            self.create_form3()
        else:
            messagebox.showerror("Error", "Seleccione puntos de origen y destino diferentes.")

    def show_visualizacion(self):
        # Lógica para mostrar resultados basada en el criterio seleccionado.
        self.visualizacion.config(text=f"Mostrando resultado basado en {self.criterio.get()}")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()


origen_options = [
    "Carabayllo", "San Juan de Miraflores", "Puente Piedra", "Miraflores", "Callao",
    "San Borja", "La Molina", "Chorrillos", "Surquillo", "Pueblo Libre", "Cieneguilla",
    "Villa María del Triunfo", "Comas", "Rímac", "Ancón", "Santa Anita",
    "San Juan de Lurigancho", "La Victoria", "San Martín de Porres", "Ate", "San Luis",
    "Lurín", "Barranco", "San Miguel", "Santiago de Surco", "San Isidro",
    "Chaclacayo", "Breña", "Cercado de Lima"
]

destino_options = [
    "Lince", "Santiago de Surco", "Jesús María", "Villa El Salvador", "San Isidro",
    "Magdalena del Mar", "Ate", "Barranco", "San Miguel", "San Luis", "Lurín",
    "Independencia", "Breña", "Santa María del Mar", "El Agustino", "Los Olivos",
    "Cercado de Lima", "Pucusana", "San Borja", "San Juan de Miraflores",
    "Pachacamac", "Miraflores", "Magdalena del Mar", "La Molina", "Callao",
    "Jesús María", "La Victoria"
]

root = tk.Tk()
app = App(root)
root.mainloop()