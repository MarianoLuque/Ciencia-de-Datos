
def printear(nulos, porcentajeNulos, cantidadRegistrosRango, porcentajeEnRango, cantidadRegistrosFueraRango, porcentajeFueraRango, cantidadValoresRango, cantidadValoresFueraRango, desde, hasta):
    print(f"**Nulos**\nCantidad de registros con nulos: {nulos}")
    print(f"Porcentaje de registros con nulos: {porcentajeNulos:.2f}%")
    print(f"**Cantidad en rango**\nCantidad de registros dentro del rango: {cantidadRegistrosRango}")
    print(f"Porcentaje de registros dentro del rango: {porcentajeEnRango:.2f}%")
    print(f"**Cantidad fuera rango**\nCantidad de registros fuera del rango: {cantidadRegistrosFueraRango}")
    print(f"Porcentaje de registros fuera del rango: {porcentajeFueraRango:.2f}%")
    print(f"**Valores unicos**\nCantidad de valores unicos dentro del rango (desde {desde} hasta {hasta}): {cantidadValoresRango}")
    print(f"Cantidad de valores unicos fuera del rango (desde {desde} hasta {hasta}): {cantidadValoresFueraRango}")
