import pandas as pd
import numpy as np

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


def agrupar_por_hora(df):
    df['hora'] = df['horaAcontecimiento'].apply(lambda x: str(x).zfill(4)[:2])
    return df

def agrupar_por_fecha(df):
    # Convertir la columna fecha a tipo datetime
    df['fechaAcontecimiento'] = pd.to_datetime(df['fechaAcontecimiento'], errors='coerce')

    # Extraer el mes de la fecha
    df['fecha'] = df['fechaAcontecimiento'].dt.strftime('%b')

    return df


def filtrar_por_edad(df, columna, desde, hasta):
    """
    Filtra la columna 'edadVictima' de un DataFrame según los parámetros 'desde' y 'hasta',
    y distribuye los registros de forma aleatoria dentro del rango especificado.

    Args:
        df (pandas.DataFrame): DataFrame a filtrar.
        columna (str): Nombre de la columna que contiene las edades.
        desde (int): Valor mínimo para la edad.
        hasta (int): Valor máximo para la edad.

    Returns:
        pandas.DataFrame: DataFrame filtrado y distribuido aleatoriamente por edadVictima.
    """
    mask = (df[columna] < desde) | (df[columna] > hasta)
    cantidad_registros = mask.sum()
    valores_aleatorios = np.random.randint(desde, hasta + 1, size=cantidad_registros)
    df.loc[mask, columna] = valores_aleatorios
    return df

def filtrar_por_sexo(df):
    df['sexoVictima'] = df['sexoVictima'].fillna('X')  # Rellenar valores nulos con 'X'
    df['sexoVictima'] = df['sexoVictima'].replace(['H'], 'X')
    return df

def filtrar_por_codigo_crimen(df):
    codigo_crimen = [510, 624, 354, 330, 740, 310, 230, 440, 626, 420, 331, 210, 341, 745, 930, 442, 761, 888, 236, 901, 480, 956, 946, 900]
    df_filtrado = df[df['codigoCrimen'].isin(codigo_crimen)]
    return df_filtrado

def filtrar_por_descendencia(df):
    df.loc[:, 'descendenciaVictima'] = df['descendenciaVictima'].fillna('X')  # Rellenar valores nulos con 'X'
    df.loc[:, 'descendenciaVictima'] = df['descendenciaVictima'].replace(['K', 'F', 'C', 'J', 'V', 'I', 'Z', 'P', 'U', 'D', 'G', 'L', 'S', '-'], 'O')
    return df