import pandas as pd

def modificar_csv(filename):
    df = pd.read_csv(filename)  # Leer el archivo CSV existente

    # Realizar modificaciones en el dataframe según tus necesidades
    df['codigoCrimen1'][] = df['columna'].fillna(-1)  # Ejemplo: Rellenar valores nulos con -1 en una columna

    # Guardar los cambios en el archivo CSV existente
    df.to_csv(filename, index=False)

# Ejemplo de uso
modificar_csv('datos.csv')