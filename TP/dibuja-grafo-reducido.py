import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('datos_courier_lima_reducido.csv')

G = nx.Graph()
# Nodos
for distrito in df['Punto_Partida'].unique():
    G.add_node(distrito)

# Aristas
for _, row in df.iterrows():
    G.add_edge(row['Punto_Partida'], row['Punto_Llegada'], distance=row['Distancia (km)'])

# Grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=300, node_color='skyblue', font_size=10, edge_color='gray', width=0.5)
labels = nx.get_edge_attributes(G, 'distance')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) 
plt.title('Grafo reducido de rutas de courieres en Lima')
plt.show()
