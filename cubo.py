def verificar_validez_configuracion(cubo):
    # Paridad de las aristas
    paridad_aristas = sum([cubo.aristas.index(i) % 2 for i in range(12)]) % 2
    
    # Paridad de las esquinas
    paridad_esquinas = sum([cubo.esquinas.index(i) % 3 for i in range(8)]) % 3
    
    # Suma total de los giros de las aristas
    giros_totales_aristas = sum([cubo.orientaciones_aristas[i] for i in range(12)]) % 2
    
    # Suma total de los giros de las esquinas
    giros_totales_esquinas = sum([cubo.orientaciones_esquinas[i] for i in range(8)]) % 3

    # Verificar si todas las condiciones de congruencia se cumplen
    if paridad_aristas == 0 and paridad_esquinas == 0 and giros_totales_aristas == 0 and giros_totales_esquinas == 0:
        return True
    else:
        return False
