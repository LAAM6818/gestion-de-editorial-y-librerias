def calcular_regalias_pendientes(indice_libros):
    lista_filtrada = []

    for libro in indice_libros.values():
        # Cálculo de regalía proyectada
        regalia = (
            libro["unidades_vendidas"] * libro["precio"] * libro["porcentaje_autor"]
        )
        libro["regalia_proyectada"] = regalia

        # Filtro por categoría: Ficción o Académico
        if libro.get("categoria") in ["Ficción", "Académico"]:
            lista_filtrada.append(libro)

    # Ordenamiento: 1° Regalía (Desc), 2° Apellido (Asc)
    # Usamos -x para descendente en valores numéricos
    lista_ordenada = sorted(
        lista_filtrada, key=lambda x: (-x["regalia_proyectada"], x["apellido_autor"].lower())
    )
    return lista_ordenada
