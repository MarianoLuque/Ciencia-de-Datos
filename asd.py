import pandas as pd

def modificar_registro(filename, fila_modificar, columna_modificar, fila_origen, columna_origen):
    df = pd.read_csv(filename)
    df.iloc[fila_modificar, columna_modificar] = df.iloc[fila_origen, columna_origen]
    df.to_csv(filename, index=False)

# Ejemplo de uso: Modificar el registro en la fila 2, columna 3 con el valor de la fila 1, columna 2
modificar_registro('datos.csv', 1, 2, 0, 1)