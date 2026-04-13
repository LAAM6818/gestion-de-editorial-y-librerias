import json
from funciones.limpieza import generar_catalogo_activo
from funciones.analisis_ordenamiento import calcular_regalias_pendientes
from funciones.interfaz import estructurar_vista_generos
from datos import lista_libros


def main():
    try:
        indice_libros, cantidad_descartados = generar_catalogo_activo(lista_libros)
        libros_ordenados = calcular_regalias_pendientes(indice_libros)
        vista_generos = estructurar_vista_generos(indice_libros)

        print("=" * 70)
        print(f"REPORTE DE PROCESAMIENTO EDITORIAL")
        print("=" * 70)
        print("libros procesados correctamente:", len(indice_libros))
        print(f"Libros descartados: {cantidad_descartados}")
        print("-" * 70)

        # Mostrar  el resultado del ordenamiento para comprobar (Regalía desc, Apellido asc)
        print("\n Regalías Calculadas (Ficción y Académico)]")
        for lib in libros_ordenados:
            print(
                f" - Autor: {lib.get('apellido_autor')}     | Regalía: ${lib.get('regalia_proyectada')}         | Ventas: {lib.get('unidades_vendidas')}"
            )

        print(json.dumps(vista_generos, indent=4, ensure_ascii=False))

        print("-" * 70)
    except Exception as e:
        print(f"Error inesperado en la ejecución principal: {e}")


if __name__ == "__main__":
    main()
