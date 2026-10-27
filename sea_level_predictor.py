import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Importar los datos de epa-sea-level.csv
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Crear el diagrama de dispersión (Scatter Plot)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.7)

    # 3. Primera línea de mejor ajuste (usando todos los datos desde 1880 hasta 2050)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series([i for i in range(1880, 2051)])
    sea_levels_extended = res_all.intercept + res_all.slope * years_extended
    ax.plot(years_extended, sea_levels_extended, 'r', label='First Line of Best Fit')

    # 4. Segunda línea de mejor ajuste (usando datos del 2000 en adelante hasta 2050)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series([i for i in range(2000, 2051)])
    sea_levels_recent = res_recent.intercept + res_recent.slope * years_recent
    ax.plot(years_recent, sea_levels_recent, 'green', label='Second Line of Best Fit')

    # 5. Configurar etiquetas, título y rango de ejes
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Guardar la imagen y retornar la figura
    plt.savefig('sea_level_plot.png')
    return ax.get_figure()
