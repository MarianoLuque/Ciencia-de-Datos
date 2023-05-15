import pandas as pd
def modificar_columnas(filename, valores_buscar):
    df = pd.read_csv(filename)
    for index, row in df.iterrows():
        nro_registro = row["nroRegistro"]
        if nro_registro in valores_buscar:
            codigo_crimen2 = row["codigoCrimen2"]
            codigo_crimen1 = row["codigoCrimen1"]
            df.loc[index, "codigoCrimen1"] = codigo_crimen2
            df.loc[index, "codigoCrimen2"] = codigo_crimen1
            #print("Numero de registro: ", nro_registro, " - codigoCrimen1: ", codigo_crimen1, " - codigoCrimen2: ", codigo_crimen2)
    df.to_csv(filename, index=False)
modificar_columnas('datos.csv', [200112035, 200116522, 211016055, 210118616, 221701255, 220509912, 220805565, 230106125])