"""
Configuraciones 

- Creación de carperta y archivo para estadísticas
    'historial_juego' para almacenar las estadisticas de resultado
- Niveles de dificultad fácil 20, medio 12 y difícil 5  
- Rango del número a adivinar (1-1000)

"""

import os 
import openpyxl
from pathlib import Path


# Creación de carpeta y archivo estadístico 
folder = "c:\\EjerciciosPython" if os.name == 'nt' else os.path.expanduser("~/EjerciciosPython")
estadisticas = os.path.join(folder, "estadisticas.xlsx") 
os.makedirs(folder, exist_ok=True)

# Crear archivo
if not os.path.exists(estadisticas):
    excel_document = openpyxl.Workbook()
    hoja = excel_document.active
    hoja.title = "Estadísticas"
    hoja.append(["Fecha", "Nombre", "Modo", "Dificultad", "Intentos", "Resultado"])
    excel_document.save(estadisticas)

# Niveles de dificultad
dificultad = {
    '1': {'nivel': 'Fácil', 'intentos': 20},
    '2': {'nivel': 'Medio', 'intentos': 12},    
    '3': {'nivel': 'Difícil', 'intentos': 5}    
}

# Rango para adivinar
num_min = 1
num_max = 1000