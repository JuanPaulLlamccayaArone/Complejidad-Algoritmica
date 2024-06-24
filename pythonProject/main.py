import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import PhotoImage
from tkinter import Toplevel
import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import dijkstra as algtm


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("UPCRutas")
        self.root.geometry("500x500")
        self.origen_options = []
        self.destino_options = []
        
        self.data_path = 'datos_courier_lima_reducido.csv'
        self.df = self.read_csv_file()

        # Cargar el logo con una ruta absoluta o relativa correcta
        script_dir = os.path.dirname(os.path.abspath(__file__))  # Ruta del script
        logo_path = os.path.join(script_dir, "logo.png")

        try:
            self.logo = PhotoImage(file=logo_path)
            # reduce size of image
            self.logo = self.logo.subsample(2)
        except tk.TclError:
            messagebox.showerror("Error", f"No se pudo cargar la imagen {logo_path}")
            self.logo = None

        self.create_form1()

    def read_csv_file(self):
        file = pd.read_csv(self.data_path)
        for _, row in file.iterrows():
            punto_partida = row['Punto_Partida']
            punto_llegada = row['Punto_Llegada']
            if punto_partida not in self.origen_options:
                self.origen_options.append(punto_partida)
            if punto_llegada not in self.destino_options:
                self.destino_options.append(punto_llegada)
        return file

    def create_form1(self):
        self.clear_frame()

        # Formulario 1: Ingreso de Nombre y Apellido
        if self.logo:
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
        if self.logo:
            self.label_logo = tk.Label(self.root, image=self.logo)
            self.label_logo.pack(pady=10)

        self.label_title = tk.Label(self.root, text=f"Hola {self.name} {self.lastname} Escoge la opción",
                                    font=("Arial", 10))
        self.label_title.pack(pady=5)

        self.label_origen = tk.Label(self.root, text="Ingrese Punto de Origen")
        self.label_origen.pack(pady=5)

        self.origen = ttk.Combobox(self.root, values=self.origen_options)
        self.origen.pack(pady=5)

        self.label_destino = tk.Label(self.root, text="Ingrese el punto de destino")
        self.label_destino.pack(pady=5)

        self.destino = ttk.Combobox(self.root, values=self.destino_options)
        self.destino.pack(pady=5)

        self.btn_buscar = tk.Button(self.root, text="Buscar", command=self.validate_form2)
        self.btn_buscar.pack(pady=20)

        self.btn_visualizar_mapa = tk.Button(self.root, text="Visualizar Mapa", command=self.show_map)
        self.btn_visualizar_mapa.pack(pady=5)

    def create_form3(self):
        self.clear_frame()

        # Formulario 3: Selección de Criterio
        if self.logo:
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

        self.visualizacion = tk.Label(self.root, text="", bg="grey", width=30, height=2)
        self.visualizacion.pack(pady=5)

        self.btn_visualizar = tk.Button(self.root, text="Buscar", command=self.buscar_ruta_optima)
        self.btn_visualizar.pack(pady=20)

    def validate_form1(self):
        self.name = self.entry_name.get().strip()
        self.lastname = self.entry_lastname.get().strip()
        if self.name.isalpha() and self.lastname.isalpha():
            self.create_form2()
        else:
            messagebox.showerror("Error", "El nombre y apellido deben contener solo caracteres.")

    def validate_form2(self):
        self.origen_val = self.origen.get()
        self.destino_val = self.destino.get()
        if self.origen_val and self.destino_val and self.origen_val != self.destino_val:
            self.create_form3()
        else:
            messagebox.showerror("Error", "Seleccione puntos de origen y destino diferentes.")

    def buscar_ruta_optima(self):
        variable = self.criterio.get()
        self.root.geometry("500x800")
        print(variable)
        opcion = ""
        if variable == "Distancia":
            opcion = "Distancia (km)"
        elif variable == "Precio":
            opcion = "Precio (S/)"
        elif variable == "Tiempo":
            opcion = "Tiempo (min)"
        
        olva = "Olva Courier"
        serpost = "Serpost"
        dhl = "DHL Express Perú"

        origen = self.origen_val
        destino = self.destino_val

        # Calcular la ruta óptima para cada courier
        ruta_olva, peso_olva = self.calculate_shortest_path(origen, destino, opcion, olva)
        ruta_serpost, peso_serpost = self.calculate_shortest_path(origen, destino, opcion, serpost)
        ruta_dhl, peso_dhl = self.calculate_shortest_path(origen, destino, opcion, dhl)

        # Imprimir la ruta óptima y el peso óptimo de cada courier
        print(f"Ruta óptima de {olva} es: {ruta_olva}, Peso óptimo: {peso_olva}")
        print(f"Ruta óptima de {serpost} es: {ruta_serpost}, Peso óptimo: {peso_serpost}")
        print(f"Ruta óptima de {dhl} es: {ruta_dhl}, Peso óptimo: {peso_dhl}")

        # Escoger la ruta óptima, comparando sus pesos
        if peso_olva < peso_serpost and peso_olva < peso_dhl:
            ruta_optima = ruta_olva
            peso_optimo = peso_olva
            empresa = olva
        elif peso_serpost < peso_olva and peso_serpost < peso_dhl:
            ruta_optima = ruta_serpost
            peso_optimo = peso_serpost
            empresa = serpost
        else:
            ruta_optima = ruta_dhl
            peso_optimo = peso_dhl
            empresa = dhl
        self.mostrar_grafo(ruta_optima, peso_optimo, empresa, opcion)

    def show_map(self):
        if self.df.empty:
            messagebox.showerror("Error", "No se pueden cargar los datos del mapa.")
            return

        # Cargar los datos y crear el grafo
        G = nx.Graph()
        for distrito in self.df['Punto_Partida'].unique():
            G.add_node(distrito)

        for _, row in self.df.iterrows():
            G.add_edge(row['Punto_Partida'], row['Punto_Llegada'], distance=row['Distancia (km)'])

        # Crear la visualización
        pos = nx.spring_layout(G, k=2, iterations=100)
        fig, ax = plt.subplots()
        nx.draw(G, pos, with_labels=True, node_size=100, node_color='skyblue', font_size=8, edge_color='gray',
                width=0.5, ax=ax)
        labels = nx.get_edge_attributes(G, 'distance')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)
        ax.set_title('Grafo reducido de rutas de courieres en Lima')

        # Mostrar la visualización en una ventana de Tkinter con soporte de zoom
        window = Toplevel(self.root)
        window.title("Mapa de Grafos")

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(canvas, window)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def calculate_shortest_path(self, origen, destino, opcion, empresa):
        # Crear el grafo
        grafo = algtm.ClassDijkstra()
        for _, row in self.df.iterrows():
            courier = row['Empresa_Courier']
            if courier != empresa:
                continue
            grafo.agregar_vertice(row['Punto_Partida'])
            grafo.agregar_vertice(row['Punto_Llegada'])
            grafo.agregar_arista(row['Punto_Partida'], row['Punto_Llegada'], row[opcion])

        # Calcular la ruta más corta usando el algoritmo de Dijkstra
        ruta, peso = grafo.dijkstra(origen, destino)
        return ruta, peso

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_grafo(self, ruta_optima, peso_optimo, empresa, opcion):
        G = nx.DiGraph()
        for origen, destino, peso in ruta_optima:
            G.add_edge(origen, destino, weight=peso)

        pos = nx.spring_layout(G, k=1)
        fig, ax = plt.subplots()
        nx.draw(G, pos, with_labels=True, node_size=300, node_color='lightgreen', font_size=8, edge_color='gray',
                width=1.5, ax=ax)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)
        ax.set_title(empresa + ' - Ruta óptima (' + opcion + ') \n Peso óptimo: ' + str(peso_optimo))

        # Mostrar la visualización en la ventana principal de Tkinter
        for widget in self.visualizacion.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.visualizacion)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


root = tk.Tk()
app = App(root)
root.mainloop()
