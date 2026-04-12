from funciones.limpieza import generar_catalogo_activo
from datos import lista_libros

def main():
    listas,libros_ignorados = generar_catalogo_activo(lista_libros)
    print(f"La listas de los diccionarios son: {listas}")
    print(f"los libros ignorados fueron: {libros_ignorados}")
if __name__ == "__main__":
    main()
    