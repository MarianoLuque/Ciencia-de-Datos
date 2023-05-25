import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.basemap import Basemap
import pandas as pd
from sklearn.decomposition import PCA

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

def crear_diagrama_calor(df, title):
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