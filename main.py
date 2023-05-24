from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


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


def filtrar_por_percentiles(df, columna, percentile_desde, percentile_hasta):
    """
    Filtra los registros de un DataFrame por percentiles en una columna dada.

    Args:
        df (pandas.DataFrame): DataFrame a filtrar.
        columna (str): Nombre de la columna en la que se aplicará el filtro.
        percentile_desde (float): Percentil desde el cual se incluirán los registros.
        percentile_hasta (float): Percentil hasta el cual se incluirán los registros.

    Returns:
        pandas.DataFrame: DataFrame filtrado por percentiles.
    """
    valor_desde = np.percentile(df[columna], percentile_desde)
    valor_hasta = np.percentile(df[columna], percentile_hasta)
    df_filtrado = df.loc[(df[columna] >= valor_desde) & (df[columna] <= valor_hasta)]
    return df_filtrado

def valoresAModificar():
    columna = "fecha"
    desde = 0
    hasta = 0
    percentile_desde = 0
    percentile_hasta = 100
    titulo = 'Cantidad de incidentes por mes'
    ejeX = 'Mes'
    ejeY = 'Cantidad de incidentes'
    return columna, desde, hasta, titulo, ejeX, ejeY, percentile_desde, percentile_hasta

def recortarHoras(df):
    df['hora'] = df['horaAcontecimiento'].apply(lambda x: str(x).zfill(4)[:2])
    return df

def agrupar_por_fecha(df):
    # Convertir la columna fecha a tipo datetime
    df['fechaAcontecimiento'] = pd.to_datetime(df['fechaAcontecimiento'], errors='coerce')

    # Extraer el mes de la fecha
    df['fecha'] = df['fechaAcontecimiento'].dt.strftime('%b')

    return df


def filtrar_edad_victima(df, desde, hasta):
    """
    Filtra la columna 'edadVictima' de un DataFrame según los parámetros 'desde' y 'hasta'.

    Args:
        df (pandas.DataFrame): DataFrame a filtrar.
        desde (int): Valor mínimo para la edad.
        hasta (int): Valor máximo para la edad.

    Returns:
        pandas.DataFrame: DataFrame filtrado por edadVictima.
    """
    df_filtrado = df.loc[(df['edadVictima'] >= desde) & (df['edadVictima'] <= hasta)]
    return df_filtrado

def graficarEntreVariables(df, bin_size):
    sns.pairplot(data=df, vars=['edadVictima', 'codigoCrimen', 'areaNro'], markers='+', diag_kws={'bins': bin_size})
    plt.show()

def main():
    df = leerArchivo()
    df_filtrado = df
    columna, desde, hasta, titulo, ejeX, ejeY, percentile_desde, percentile_hasta = valoresAModificar()
    df = agrupar_por_fecha(df)
    df_filtrado = recortarHoras(df)
    df_filtrado = filtrar_edad_victima(df, 18, 75)
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
    grafico.set_xticklabels(ordenados.index, rotation=0)
    # Para no mostrar una etiqueta
    # grafico.set_xticklabels([])

    # Agregar etiquetas con los valores de cada barra
    for i, v in enumerate(ordenados):
        grafico.text(i, v + 1000, str(round(v, 2)), ha='center', fontweight='bold', fontsize=8, rotation='vertical')

    # Rotular los ejes y el título del gráfico
    rotular(grafico, titulo, ejeX, ejeY)
    # Mostrar grafico
    plt.show()

    graficarEntreVariables(df_filtrado, 20)
    print(df['edadVictima'].describe())
    print(df_filtrado['edadVictima'].describe())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
