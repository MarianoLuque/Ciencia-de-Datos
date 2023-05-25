import pandas as pd

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
    if desde != 0:
        cantidad = cantidad[cantidad >= desde]
    if hasta != 0:
        cantidad = cantidad[cantidad <= hasta]
    return cantidad, nulos


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


def calcularPorcentajes(total, nulos, enRango, fueraRango):
    porcentajeNulos = (nulos / total) * 100
    porcentajeEnRango = (enRango / total) * 100
    porcentajeFueraRango = (fueraRango / total) * 100
    return porcentajeNulos, porcentajeEnRango, porcentajeFueraRango
