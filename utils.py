from typing import NoReturn
from prettytable import PrettyTable
from config import CURRENCY_SYMBOL

def get_currency_format(currency_symbol, price) -> str:
    """
      Método para formatear una variable numérica en string con formato de moneda
      """
    return "{}{:,.2f}".format(currency_symbol, price)


def show_products_list(products, prices, stock) -> NoReturn:
    # Definimos los nombres de los campos
    field_names = ['ID', 'Producto',
                   'Precio', 'Stock', ]

    # Establecemos los nombres de los campos en la tabla
    table = PrettyTable(field_names)

    # Agregamos la lista de productos y sus detalles
    for key, value in products.items():
        table.add_row([int(key), str(products[key]), get_currency_format(
            CURRENCY_SYMBOL, round(prices[key], 2)), int(stock[key])])

    # Alineamos todos los campos a la izquierda
    table.align = "l"

    print(table)

def exist_id(id, products) -> bool:
  """
  Función para revisar si existe el ID
  """
  # Si ya existe el id
  if id in products.keys():
    return True
  return False