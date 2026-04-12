def generar_catalogo_activo(lista_libros):

    indice = {}
    descartados = 0

    for libro in lista_libros:
        # Verificar si tiene la clave 'isbn'
        if "isbn" not in libro:
            descartados += 1
            continue

        if libro.get("estado_impresion") == "descatalogado":
            descartados += 1
            continue

        # Si pasa ambos filtros, agregar al índice
        isbn = libro["isbn"]
        indice[isbn] = libro

    return (indice, descartados)
