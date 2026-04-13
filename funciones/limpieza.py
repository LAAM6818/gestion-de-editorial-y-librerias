def generar_catalogo_activo(lista_libros):

    indice = {}
    descartados = 0

    for libro in lista_libros:

        try:
            # Verificar si tiene la clave 'isbn'
            if "isbn" not in libro:
                descartados += 1
                continue

            if libro.get("estado_impresion") == "descatalogado":
                descartados += 1
                continue

            # Si pasa ambos filtros, agregar al índice
            isbn = libro["isbn"]
            indice[isbn] = libro.copy()  # Usamos copy para evitar modificar el original

        except Exception as e:
            print(
                f"Error inesperado al procesar libro en limpieza:{libro.get('titulo', 'Título desconocido')} {e}"
            )
            descartados += 1

    return (indice, descartados)
