import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.basemap import Basemap
import pandas as pd
from sklearn.decomposition import PCA
from scipy.stats import chi2_contingency
from scipy.stats import chi2

def graficarMapa(df):
    mapa = Basemap(projection='merc', llcrnrlat=-90, urcrnrlat=90, llcrnrlon=-180, urcrnrlon=180)

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(1, 1, 1)

    ax.scatter(df['longitud'], df['latitud'], s=20, c='red', alpha=0.5)

    mapa.drawcountries()
    mapa.drawcoastlines()

    plt.show()


def graficarEntreVariables(df, bin_size):
    sns.pairplot(data=df, vars=['edadVictima', 'codigoCrimen'], markers='+', diag_kws={'bins': bin_size})
    plt.show()

def graficoDeColores(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='codigoCrimen', hue='areaNro')
    plt.ylabel('Cantidad de Crimenes')
    plt.xlabel('Codigo del crimen')

    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., title='Numero de Area', ncol=2)
    plt.subplots_adjust(bottom=0.1, top=0.9, left=0.1, right=0.8)  # Ajustar los márgenes según necesites

    sns.despine(left=True)
    plt.show()


def dispersionCategoric(df, categoria, valor):
    # Gráfico de caja y bigotes
    sns.boxplot(x=categoria, y=valor, data=df)
    plt.show()
    # Gráfico de violín
    sns.violinplot(x=categoria, y=valor, data=df)
    plt.show()
    # Gráfico de punto
    sns.stripplot(x=categoria, y=valor, data=df)
    plt.show()

def dispersion(df):
    plt.scatter(df['latitud'], df['edadVictima'], c=df['edadVictima'])
    plt.show()

def mapaCalor(df):
    # Mapear los valores categóricos a valores numéricos
    df['sexo_numerico'] = df['sexoVictima'].map({'M': 1, 'F': 2, 'X': 3})

    columnas_seleccionadas = ['codigoCrimen', 'sexo_numerico']
    data_seleccionada = df[columnas_seleccionadas]
    correlacion = data_seleccionada.corr()
    sns.heatmap(correlacion, cmap='YlGnBu', annot=True)

def crear_diagrama_calor(df):
    """
    Crea un diagrama de calor (heatmap) para un conjunto de datos.

    Args:
        data (pandas.DataFrame): DataFrame con los datos.
        title (str): Título del diagrama de calor.

    Returns:
        None
    """
    plt.figure(figsize=(10, 8))

    # Realiza la codificación one-hot de las variables categóricas
    df_encoded = pd.get_dummies(df)
    # Crea la matriz de correlación a partir del dataframe codificado
    correlation_matrix = df_encoded.corr()
    # Crea el mapa de calor utilizando Seaborn
    sns.heatmap(correlation_matrix, cmap='coolwarm', annot=True)
    # Ajusta los márgenes de la figura para evitar que se recorten los bordes
    plt.tight_layout()
    # Muestra el mapa de calor
    plt.show()

def mapaDeCalor(df):
    
    df = df.copy()  # Hacer una copia del DataFrame
    # Convertir todas las columnas del DataFrame a tipo float
    # Eliminar la columna con datos de tipo Datetime
    df.loc[:, 'fecha_numerico'] = df['fecha'].map({'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12})
    df.loc[:, 'sexo_numerico'] = df['sexoVictima'].map({'M': 1, 'F': 2, 'X': 3})
    df.loc[:, 'descendencia_numerico'] = df['descendenciaVictima'].map({'H': 1, 'W': 2, 'B': 3, 'X':4, 'O':5, 'A':6})
    #df['estado_numerico'] = df['estado'].map({'IC': 1, 'AO': 2, 'AA': 3})
    
    columnas = ['fecha_numerico', 'hora', 'areaNro', 'codigoCrimen',  'edadVictima', 'sexo_numerico', 'descendencia_numerico']
    df = df[columnas] 
    df = df.astype(float)
    # Crear un mapa de calor a partir del DataFrame
    plt.imshow(df, cmap='hot', interpolation='nearest')

    # Agregar etiquetas a los ejes x e y
    plt.xticks(range(len(df.columns)), df.columns)
    plt.yticks(range(len(df.index)), df.index)

    # Agregar una barra de colores para indicar los valores
    plt.colorbar()

    # Mostrar el mapa de calor
    plt.show()

def chiCuadrado(df):
    # Calcular la tabla de contingencia
    tabla_contingencia = pd.crosstab(df['sexoVictima'], df['codigoCrimen'])
    # Realizar el test de chi-cuadrado
    chiDos, pval, _, _ = chi2_contingency(tabla_contingencia)

    # Imprimir los resultados
    print(f'Estadístico chi-cuadrado: {chiDos}')
    print(f'Valor p: {pval}')

    # Definir umbral de significancia
    nivel_significancia = 0.05

    # Comparar el valor p con el umbral de significancia
    if pval < nivel_significancia:
        print("Hay una asociación significativa entre las variables.")
    else:
        print("No se encontró una asociación significativa entre las variables.")
    
    # Calcular el número de grados de libertad
    grados_libertad = (tabla_contingencia.shape[0] - 1) * (tabla_contingencia.shape[1] - 1)

    # Obtener el valor crítico de chi-cuadrado
    valor_critico = chi2.ppf(1 - nivel_significancia, grados_libertad)

    # Comparar el valor chi2 con el valor crítico
    if chiDos > valor_critico:
        print("Hay una discrepancia significativa entre los valores observados y los valores esperados.")
    else:
        print("No se encontró una discrepancia significativa.")