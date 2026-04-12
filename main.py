from funciones.limpieza import generar_catalogo_activo
from funciones.analisis_ordenamiento import calcular_regalias_pendientes
from funciones.interfaz import estructurar_vista_generos
from datos import lista_libros


def main():
    try:
        indice_libros, cantidad_descartados = generar_catalogo_activo(lista_libros)
        calcular_regalias_pendientes(indice_libros)
        vista_generos = estructurar_vista_generos(indice_libros)

        print("="*70)
        print(f"REPORTE DE PROCESAMIENTO EDITORIAL")
        print("="*70)
        print("libros procesados correctamente:", len(indice_libros))
        print(f"Libros descartados: {cantidad_descartados}")
        print("-" * 70)

       
       ##### aqui se mostrata la parte de oriana 
        

        

    except Exception as e:
        print(f"Error durante el procesamiento: {e}")

if __name__ == "__main__":
    main()
