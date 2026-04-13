def calcular_regalias_pendientes(indice_libros):
    lista_filtrada = []

    for libro in indice_libros.values():
        try:  # Cálculo de regalía proyectada
            unidades = libro["unidades_vendidas"]
            precio = libro["precio"]
            porcentaje = libro["porcentaje_autor"]

            # Cálculo de regalía proyectada
            regalia = unidades * precio * porcentaje
            libro["regalia_proyectada"] = regalia

            # Filtro por categoría: Ficción o Académico
            if libro.get("categoria") in ["Ficción", "Académico"]:
                lista_filtrada.append(libro)

        except Exception as e:
            print(
                f"Error al procesar o calcular regalía para el libro {libro.get('titulo', 'Desconocido')}: {e}"
            )
            continue

    try:

        lista_ordenada = sorted(
            lista_filtrada,
            key=lambda x: (-x["regalia_proyectada"], x["apellido_autor"].lower()),
        )
    except Exception as e:
        print(f"Error al ordenar la lista: {e}")
        return []

    return lista_ordenada
