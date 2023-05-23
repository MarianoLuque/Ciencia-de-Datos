import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def leerArchivo():
    """Definir el archivo y leerlo"""
    filename = 'datos.csv'
    df = pd.read_csv(filename, header=0)
    return df


def contar(df, columna, desde, hasta):
    """
    Cuenta la cantidad de elementos y nulos de una columna
    Args:
        :param df: Dataframe utilizado
        :param columna: Columna que se quiere contar los registros
        :param desde: Desde que nro de crimenes contar
        :param hasta: Hasta que nro de crimenes contar
    """
    cantidad = df[columna].value_counts()
    nulos = df[columna].isnull().sum()
    # Filtrar códigos de crimen con más de "desde" y menos de "hasta" crímenes asociados
    if(desde != 0):
        cantidad = cantidad[cantidad >= desde]
    if(hasta != 0):
        cantidad = cantidad[cantidad <= hasta]
    return (cantidad, nulos)


def ordenar(tipoOrdenamiento, descendente, objeto):
    """
    Ordena los datos de acuerdo a los valores de X o de Y
    :param tipoOrdenamiento: 1 para ordenar en X y 2 para ordenar en Y
    :param descendente: True para ordenar de manera ascendente y False para descendente
    :param objeto: columna a ordenar
    """
    ascendente = True
    if (descendente != True):
        ascendente = False
    if tipoOrdenamiento == 1:
        return objeto.sort_index(ascending=ascendente)
    if tipoOrdenamiento == 2:
        return objeto.sort_values(ascending=ascendente)


def rotular(grafico, titulo, labelX, labelY):
    """
    Agrega etiquetas al grafico
    :param grafico: Gráfico a rotular
    :param titulo: Título del gráfico
    :param labelX: Etiqueta X
    :param labelY: Etiqueta Y
    """
    grafico.set_title(titulo)
    grafico.set_xlabel(labelX)
    grafico.set_ylabel(labelY)


def print_datos():
    df = leerArchivo()
    cantidad, nulos = contar(df, "edadVictima", 2300, 0)
    ordenados = ordenar(2, False, cantidad)
    print(nulos)

    # Calculando el porcentaje de registros con cantidad de crímenes dentro del rango
    total_registros = len(df)
    cantidad_rango = cantidad.sum() + nulos
    print(cantidad_rango)  # Suma de la cantidad de crímenes dentro del rango
    porcentaje_rango = (cantidad_rango / total_registros) * 100
    
    # Contando la cantidad de códigos de crimen dentro del rango
    cantidad_codigos_rango = len(cantidad)

    # Contando la cantidad de códigos de crimen fuera del rango (< 5000)
    cantidad_codigos_fuera_rango = len(df["edadVictima"].unique()) - cantidad_codigos_rango

    print(f"Porcentaje de registros con cantidad de crímenes dentro del rango: {porcentaje_rango:.2f}%")
    print(f"Cantidad de códigos de crimen dentro del rango: {cantidad_codigos_rango}")
    print(f"Cantidad de códigos de crimen fuera del rango (< 5000): {cantidad_codigos_fuera_rango}")
    

    # ajustar para que se muestren todos los resultados por consola
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    # Generar el gráfico de barras
    grafico = ordenados.plot(kind='bar')

    # Modificando etiquetas de eje X (pone los nros verticales)
    grafico.set_xticklabels(ordenados.index, rotation=90)
    #Para no mostrar una etiqueta
    #grafico.set_xticklabels([])

    # Agregar etiquetas con los valores de cada barra
    for i, v in enumerate(ordenados):
        grafico.text(i, v + 1000, str(round(v, 2)), ha='center', fontweight='bold', fontsize=8, rotation='vertical')

    # Rotular los ejes y el título del gráfico
    rotular(grafico, 'Cantidad de incidentes por estado', 'Estado', 'Cantidad de incidentes')
    # Mostrar grafico
    plt.show()


def buscarVehiculos():
    # Definir el archivo y leerlo
    filename = 'datos.csv'
    df = pd.read_csv(filename, header=0)

    # Cuenta la cantidad de filas que contienen "vehicle" en la columna "CRM CD DESC"
    count = len(df[df['LAT'] > 0])

    # Imprime el resultado
    print(f"El archivo tiene {count} filas que contienen 'vehicle' en la columna 'CRM CD DESC'.")


def ejemploProfe():
    # dado dos conjuntos de datos:
    high_var_array = np.array([5001, 5000, 5000, 5000, 5000, 5000])
    low_var_array = np.array([2, 4, 6, 8, 10])

    # Obtener la varianza
    varianza1 = np.var(high_var_array)
    varianza2 = np.var(low_var_array)
    # y la desviación estándar
    devstd1 = np.std(high_var_array)
    devstd2 = np.std(low_var_array)
    # y la media
    media1 = np.mean(high_var_array)
    media2 = np.mean(low_var_array)

    plt.hist(high_var_array)
    plt.show()
    plt.hist(low_var_array)
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_datos()
