import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from funciones import *
from agruparYfiltrar import *
from graficar import *
from imprimir import *
import missingno as msno

def valoresAModificar():
    columna = "fecha"
    desde = 0
    hasta = 0
    percentile_desde = 0
    percentile_hasta = 100
    titulo = 'Cantidad de incidentes por sexo de la victima'
    ejeX = 'Sexo de la victima'
    ejeY = 'Cantidad de incidentes'
    return columna, desde, hasta, titulo, ejeX, ejeY, percentile_desde, percentile_hasta


def main():
    df = leerArchivo()
    df_filtrado = df
    msno.matrix(df)
    plt.show()
    columna, desde, hasta, titulo, ejeX, ejeY, percentile_desde, percentile_hasta = valoresAModificar()
    df_filtrado = agrupar_por_fecha(df_filtrado)
    df_filtrado = agrupar_por_hora(df_filtrado)
    df_filtrado = filtrar_por_sexo(df_filtrado)
    df_filtrado = filtrar_por_codigo_crimen(df_filtrado)
    df_filtrado = filtrar_por_descendencia(df_filtrado)
    df_filtrado = filtrar_por_edad(df_filtrado, 'edadVictima', 12, 76)
    cantidad, nulos = contar(df_filtrado, columna, desde, hasta)
    ordenados = ordenar(1, True, cantidad)


    #graficoDeColores(df_filtrado)
    #crear_diagrama_calor(df_filtrado, "Diagrama de Calor")
    #graficarMapa(df_filtrado)
    #dispersionCategoric(df_filtrado, 'sexoVictima', 'codigoCrimen')
    #dispersion(df_filtrado)
    #mapaDeCalor(df_filtrado)

    # Datos para calcular porcentajes
    totalRegistros = len(df_filtrado) # cantidad de datos que tiene el registro
    cantidadRegistrosRango = cantidad.sum() # cantidad de datos dentro de desde-hasta
    cantidadRegistrosFueraRango = totalRegistros - cantidadRegistrosRango - nulos
    cantidadValoresRango = len(cantidad) # cantidad de valores unicos dentro de desde-hasta
    cantidadValoresFueraRango = len(df_filtrado[columna].unique()) - cantidadValoresRango # cantidad de valores unicos fuera de desde-hasta
    porcentajeNulos, porcentajeEnRango, porcentajeFueraRango = calcularPorcentajes(totalRegistros, nulos, cantidadRegistrosRango, cantidadRegistrosFueraRango)

    printear(nulos, porcentajeNulos, cantidadRegistrosRango, porcentajeEnRango, cantidadRegistrosFueraRango, porcentajeFueraRango, cantidadValoresRango, cantidadValoresFueraRango, desde, hasta)
    
    # ajustar para que se muestren todos los resultados por consola
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    # Generar el gráfico de barras
    grafico = ordenados.plot(kind='bar')

    # Modificando etiquetas de eje X (pone los nros verticales)
    grafico.set_xticklabels(ordenados.index, rotation=0)
    # Para no mostrar una etiqueta
    # grafico.set_xticklabels([])

    # Agregar etiquetas con los valores de cada barra
    for i, v in enumerate(ordenados):
        grafico.text(i, v + 3000, str(round(v, 2)), ha='center', fontweight='bold', fontsize=8, rotation='vertical')

    # Rotular los ejes y el título del gráfico
    rotular(grafico, titulo, ejeX, ejeY)
    # Mostrar grafico
    plt.show()

    # graficarEntreVariables(df_filtrado, 20)

    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
