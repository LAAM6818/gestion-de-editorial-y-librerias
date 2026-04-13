def estructurar_vista_generos(indice_libros):
    agrupado = {}

    for libro in indice_libros.values():

        try:
            genero = libro.get("genero_literario", "Sin Género")
            if genero not in agrupado:
                agrupado[genero] = []

            # Copia para no modificar el índice original al eliminar la clave
            item = libro.copy()

            # Regla de insignia_web
            if item["unidades_vendidas"] > 1000:
                item["insignia_web"] = "Bestseller"
            else:
                item["insignia_web"] = "Regular"

            # Eliminar la clave del género dentro del objeto anidado
            item.pop("genero_literario")

            agrupado[genero].append(item)

        except Exception as e:
            # Si algo falla catastróficamente con un libro, lo reportamos
            print(f"Error procesando un libro: {e}")

    return agrupado
