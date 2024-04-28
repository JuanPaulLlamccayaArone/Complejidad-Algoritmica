import pandas as pd
import numpy as np
import os

# Lista de distritos de Lima
distritos_limena = [
    'Ancón', 'Ate', 'Barranco', 'Breña', 'Carabayllo', 'Cercado de Lima', 'Chaclacayo', 'Chorrillos', 
    'Cieneguilla', 'Comas', 'El Agustino', 'Independencia', 'Jesús María', 'La Molina', 'La Victoria', 
    'Lince', 'Los Olivos', 'Lurigancho', 'Lurín', 'Magdalena del Mar', 'Miraflores', 'Pachacámac', 'Pucusana',
    'Pueblo Libre', 'Puente Piedra', 'Punta Hermosa', 'Punta Negra', 'Rímac', 'San Bartolo', 'San Borja',
    'San Isidro', 'San Juan de Lurigancho', 'San Juan de Miraflores', 'San Luis', 'San Martín de Porres', 
    'San Miguel', 'Santa Anita', 'Santa María del Mar', 'Santa Rosa', 'Santiago de Surco', 'Surquillo',
    'Villa El Salvador', 'Villa María del Triunfo', 'Callao', 'Ventanilla', 'Carmen de la Legua Reynoso',
    'Bellavista', 'La Perla', 'Mi Perú', 'La Punta'
]


empresas_courier = ['Olva Courier', 'Serpost', 'DHL Express Perú']

data = []

for i in range(1500):
    id_envio = '1D' + str(i + 1)
    punto_partida = np.random.choice(distritos_limena)
    punto_llegada = np.random.choice(distritos_limena)
    distancia_base = round(np.random.uniform(5, 30), 2)  
    for empresa in empresas_courier:
        precio_base = np.random.randint(8, 21)  
        tiempo_base = np.random.randint(15, 121)  
        precio = precio_base + np.random.randint(1, 8)  
        tiempo = tiempo_base + np.random.randint(2, 8)  
        data.append([id_envio, punto_partida, punto_llegada, distancia_base, tiempo, precio, empresa])


df = pd.DataFrame(data, columns=['ID', 'Punto_Partida', 'Punto_Llegada', 'Distancia (km)', 'Tiempo (min)', 'Precio (S/)', 'Empresa_Courier'])


ruta_escritorio = os.path.join(os.path.expanduser('~'), 'Desktop')

df.to_csv(os.path.join(ruta_escritorio, 'datos_courier_limena.csv'), index=False)

print("Archivo CSV generado y guardado en el escritorio.")

