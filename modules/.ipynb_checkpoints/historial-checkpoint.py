"""
Historial de partidas

- Mostrar en formato tabla la ultimas 20 partidas 
- Mejores Jugadores/peores en gráfico de barras
- Gráfico de pastele para ganados/perdidos
"""
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
from .configuraciones import estadisticas

# Menú para historial 
def historial():
    while True:
        print("Historial")
        print("\n1. Últimas 20 Partidas\n2. Rendimiento Jugadores\n3. Porcentaje de Partidas Ganadas o Perdidas\n4. Regresar\n")
        opcion=input("Selecciona una opción númerica: ")
        
        if opcion == '1':
            ultimas_partidas()
        elif opcion == '2':
            rendimiento_jugadores()           
        elif opcion == '3':
            graf_partidas()
        elif opcion == '4':
            break
        else:
            print("Selecciona una opción entre 1-3: ")

            
# Últimas partidas            
def ultimas_partidas():
    print("\n   Últimas partidas")
    display(pd.read_excel(estadisticas).tail(20))


# Rendimiento_jugadores
def rendimiento_jugadores():
    df = pd.read_excel(estadisticas)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 3))

    # mejores jugadores
    df[df['Resultado'] == 'Ganado']['Nombre'].value_counts().plot.bar(
        ax=ax1,
        title="★★★",
        color="white",
        edgecolor="gold"
    )
    ax1.set_ylabel("Victorias")
    ax1.set_xlabel("Jugadores con más partidas ganadas")
    ax1.tick_params(axis='x', rotation=45)

    # Peores jugadores
    df[df['Resultado'] == 'Perdido']['Nombre'].value_counts().plot.bar(
        ax=ax2,
        title="✗✗✗",
        color="white",
        edgecolor="red"
    )
    ax2.set_ylabel("Derrotas")
    ax2.set_xlabel("Jugadores con más partidas perdidas")
    ax2.tick_params(axis='x', rotation=45)
   
    fig.suptitle("Rendimiento de Jugadores", fontsize=14)
    plt.subplots_adjust(top=0.75) 
    plt.show()



# Gráficos 
def graf_partidas():
    df = pd.read_excel(estadisticas)
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 3))

    # generales    
    resultado_generales = df['Resultado'].value_counts().plot.pie(
        ax=ax1,
        title="Partidas Generales",
        shadow=True,
        colors=["mediumseagreen", "whitesmoke"],
        autopct='%d'
    )
    ax1.set_ylabel('')
    
    # solitarios
    resultado_solitarios = df[df['Modo']=="Solitario"]['Resultado'].value_counts().plot.pie(
        ax=ax2,
        title="Partidas Solitarias",
        shadow=True,
        colors=["mediumseagreen", "whitesmoke"],
        autopct='%d'
    )
    ax2.set_ylabel('')

    # dobles
    resultado_dobles = df[df['Modo']=="Doble"]['Resultado'].value_counts().plot.pie(
        ax=ax3,
        title="Partidas Dobles",
        shadow=True,
        colors=["mediumseagreen", "whitesmoke"],
        autopct='%d'
    )
    ax3.set_ylabel('')
    
    fig.suptitle("Porcentaje de Partidas Ganadas o Perdidas", fontsize=14)
    plt.subplots_adjust(top=0.75) 
    plt.show()