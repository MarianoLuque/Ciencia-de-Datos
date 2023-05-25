import matplotlib.pyplot as plt
import seaborn as sns

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
    heatmap = sns.heatmap(df, cmap="YlGnBu")
    heatmap.set_title(title)
    plt.show()