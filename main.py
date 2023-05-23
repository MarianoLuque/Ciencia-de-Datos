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

def valoresAModificar():
    columna = "codigoCrimen"
    desde = 2500
    hasta = 50000
    titulo = 'Cantidad de incidentes por codigo de crimen'
    ejeX = 'Codigo crimen'
    ejeY = 'Cantidad de incidentes'
    return columna, desde, hasta, titulo, ejeX, ejeY

def main():
    df = leerArchivo()
    columna, desde, hasta, titulo, ejeX, ejeY = valoresAModificar()
    cantidad, nulos = contar(df, columna, desde, hasta)
    ordenados = ordenar(2, False, cantidad)

    # Datos para calcular porcentajes
    totalRegistros = len(df) # cantidad de datos que tiene el registro
    cantidadRegistrosRango = cantidad.sum() # cantidad de datos dentro de desde-hasta
    cantidadRegistrosFueraRango = totalRegistros - cantidadRegistrosRango - nulos
    cantidadValoresRango = len(cantidad) # cantidad de valores unicos dentro de desde-hasta
    cantidadValoresFueraRango = len(df[columna].unique()) - cantidadValoresRango # cantidad de valores unicos fuera de desde-hasta
    porcentajeNulos, porcentajeEnRango, porcentajeFueraRango = calcularPorcentajes(totalRegistros, nulos, cantidadRegistrosRango, cantidadRegistrosFueraRango)

    print(f"**Nulos**\nCantidad de registros con nulos: {nulos}")
    print(f"Porcentaje de registros con nulos: {porcentajeNulos:.2f}%")
    print(f"**Cantidad en rango**\nCantidad de registros dentro del rango: {cantidadRegistrosRango}")
    print(f"Porcentaje de registros dentro del rango: {porcentajeEnRango:.2f}%")
    print(f"**Cantidad fuera rango**\nCantidad de registros fuera del rango: {cantidadRegistrosFueraRango}")
    print(f"Porcentaje de registros fuera del rango: {porcentajeFueraRango:.2f}%")
    print(f"**Valores unicos**\nCantidad de valores unicos dentro del rango (desde {desde} hasta {hasta}): {cantidadValoresRango}")
    print(f"Cantidad de valores unicos fuera del rango (desde {desde} hasta {hasta}): {cantidadValoresFueraRango}")

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
    rotular(grafico, titulo, ejeX, ejeY)
    # Mostrar grafico
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
