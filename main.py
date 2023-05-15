import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def leerArchivo():
    """Definir el archivo y leerlo"""
    filename = 'datos.csv'
    df = pd.read_csv(filename, header=0)
    return df
def contar(df, columna):
    """
    Cuenta la cantidad de elementos y nulos de una columna
    Args:
        :param df: Dataframe utilizado
        :param columna: Columna que se quiere contar los registros
    """
    cantidad = df[columna].value_counts()
    nulos = df[columna].isnull().sum()
    return (cantidad, nulos)
def ordenar(tipoOrdenamiento, descendente, objeto):
    """
    Ordena los datos de acuerdo a los valores de X o de Y
    :param tipoOrdenamiento: 1 para ordenar en X y 2 para ordenar en Y
    :param descendente: True para ordenar de manera ascendente y False para descendente
    :param objeto: columna a ordenar
    """
    ascendente = True
    if(descendente != True):
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
    cantidad, nulos = contar(df, "codigoCrimen1")
    ordenados = ordenar(2, False, cantidad)

    # ajustar para que se muestren todos los resultados por consola
    pd.set_option('display.max_rows', None)

    # Generar el gráfico de barras
    grafico = ordenados.plot(kind='bar')

    # Modificando etiquetas de eje X (pone los nros verticales)
    grafico.set_xticklabels(ordenados.index, rotation=0)

    # Agregar etiquetas con los valores de cada barra
    for i, v in enumerate(ordenados):
        grafico.text(i, v, str(round(v, 2)), ha='center', fontweight='bold', fontsize=8)

    # Configurar el eje X y el título del gráfico
    rotular(grafico, 'Cantidad de incidentes por área', 'Area', 'Cantidad de incidentes')
    # Mostrar grafico
    print(df.describe())
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

