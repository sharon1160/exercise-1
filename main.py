from typing import Dict

from utils import *


def create_dic_products() -> Dict[int, str]:
    """
    Función que crea y devuelve un diccionario de productos
    """
    products: Dict[int, str] = {
        1: 'Pantalones',
        2: 'Camisas',
        3: 'Corbatas',
        4: 'Casacas'
    }
    return products


def create_dic_prices() -> Dict[int, float]:
    """
    Función que crea y devuelve un diccionario de precios
    """
    prices: Dict[int, float] = {
        1: 200.00,
        2: 120.00,
        3: 50.00,
        4: 350.00
    }
    return prices


def create_dic_stock() -> Dict[int, int]:
    """
    Función que crea y devuelve un diccionario de stocks
    """
    stock: Dict[int, int] = {
        1: 50,
        2: 45,
        3: 30,
        4: 15
    }
    return stock

def add_product(products, prices, stock) -> None:
    """
    Función para agregar productos
    """
    print()
    print('=' * 40)
    print(' ' * 8, "INGRESAR NUEVO PRODUCTO")
    print('=' * 40)

    # Mostramos lista de productos
    show_products_list(products, prices, stock)

    print("\nNuevo Producto")
    print("-" * 14)

    # Definimos ID por default
    id = 1
    # Ingresamos ID del producto
    while True:
        # Manejando errores en el caso de que se ingrese un tipo de dato
        # diferente a un entero
        try:
            # Ingresamos el ID del nuevo producto
            id = int(input("ID: "))

            # Validamos si el ID existe
            if exist_id(id, products) == False:
                break
            else:
                print("El ID ya existe, intente nuevamente...")
        except:
            print("Ingrese sólo números, intente nuevamente...")

    # Ingresamos el producto
    product = str(input("Producto: "))
    products[id] = product.title()

    # Ingresamos el precio del producto
    price = float(input("Precio: "))
    prices[id] = price

    # Ingresamos el stock del producto
    product_stock = int(input("Stock: "))
    stock[id] = product_stock

def delete_product(products, prices, stock) -> None:
    """
    Función para agregar productos
    """
    print()
    print('=' * 40)
    print(' ' * 10, "ELIMINAR PRODUCTO")
    print('=' * 40)

    # Mostramos lista de productos
    show_products_list(products, prices, stock)

    print("\nProducto a Eliminar")
    print("-" * 19)

    while True:
        # Manejando errores en el caso de que se ingrese un tipo de dato
        # diferente a un entero
        try:
            # Ingresamos id del producto a eliminar
            id = int(input("Ingrese ID del producto a eliminar: "))

            # Verificamos si existe el id
            if exist_id(id, products) == True:
                break
            else:
                print("El ID NO existe!!, intente nuevamente...")
        except:
            print("Ingrese sólo números, intente nuevamente...")

    # Eliminamos el producto
    del products[id]

    # Eliminamos el precio
    del prices[id]

    # Eliminamos el stock
    del stock[id]


def update_product(products, prices, stock) -> None:
    """
    Función para actualizar producto
    """
    id = 1
    print()
    print('=' * 40)
    print(' ' * 10, "ACTUALIZAR PRODUCTO")
    print('=' * 40)
    print()

    # Mostramos lista de productos
    show_products_list(products, prices, stock)

    print("\nProducto a Actualizar")
    print("-" * 21)

    while True:
        # Manejando errores en el caso de que se ingrese un tipo de dato
        # diferente a un entero
        try:
            # Ingresamos id del producto a actualizar
            id = int(input("Ingrese ID del producto a actualizar: "))

            # Verificamos si existe el id
            if exist_id(id, products) == True:
                break
            else:
                print("El ID NO existe!!, intente nuevamente...")
        except:
            print("Ingrese sólo números, intente nuevamente...")

    while True:
        print()
        print(f"Ingrese campo a actualizar del producto {id}:")
        print("[1] Nombre")
        print("[2] Precio")
        print("[3] Stock")
        print("[4] Salir")

        # Manejando errores en el caso de que se ingrese caracteres
        # u otro tipo de dato diferente a un entero
        try:
            opc = int(input("Elija una opción (1-4): "))
            if opc == 1:
                # Actualizamos el nombre del producto
                new_name = str(input("Nuevo nombre: "))
                products[id] = new_name.title()
                print(f"\nNombre del producto {id} actualizado exitosamente!!")
            elif opc == 2:
                # Validando que el precio sea un entero o un flotante
                try:
                    # Actualizamos el precio del producto
                    new_price = float(input("Nuevo precio: "))
                    prices[id] = new_price
                    print(f"\nPrecio del producto {id} actualizado exitosamente!!")
                except:
                    print("\nIngrese números enteros o decimales, intente nuevamente...")
            elif opc == 3:
                # Validando que el stock sea un entero
                try:
                    # Actualizamos el stock del producto
                    new_stock = int(input("Nuevo stock: "))
                    stock[id] = new_stock
                    print(f"\nStock del producto {id} actualizado exitosamente!!")
                except:
                    print("\nIngrese números enteros, intente nuevamente...")
            elif opc == 4:
                print("Saliendo del menú...")
                break
            else:
                print("Opción inválida, intente nuevamente...")
                continue
        except:
            print("Ingrese un número del 1 al 4, intente nuevamente...")

def show_menu(products, prices, stock) -> None:
    while True:
        print()
        print('=' * 40)
        print(' ' * 12,"MENU PRINCIPAL")
        print('=' * 40)
        show_products_list(products, prices, stock)
        print()
        print("[1] Agregar")
        print("[2] Eliminar")
        print("[3] Actualizar")
        print("[4] Salir")

        # Manejando errores en el caso de que el usuario ingrese caracteres
        # u otro tipo de dato diferente a un entero
        try:
            opc = int(input("Elija una opción: "))
            if opc == 1:
                add_product(products, prices, stock)
                print("\nProducto agregado exitosamente!!")
            elif opc == 2:
                delete_product(products, prices, stock)
                print("\nProducto eliminado exitosamente!!")
            elif opc == 3:
                update_product(products, prices, stock)
            elif opc == 4:
                print("\nSaliendo del menú...")
                break
            else:
                print("Opción inválida, intente nuevamente...")
        except:
            print("Ingrese un número del 1 al 4, intente nuevamente...")

def main():
    """
    Función principal
    """

    # Creamos el diccionario de productos
    products = create_dic_products()

    # Creamos el diccionario de precios
    prices = create_dic_prices()

    # Creamos el diccionario de stocks
    stock = create_dic_stock()

    # mostrar menú de opciones
    show_menu(products, prices, stock)


if __name__ == "__main__":
    main()
