from modelos.platillo import Platillo
from modelos.bebida import Bebida

class Restaurante:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def mostrar_productos(self):
        if not self.__productos:
            print("No hay productos registrados")
            return
        
        print("\nRestaurante Recetas de mi Sierra")
        for idx, producto in enumerate(self.__productos, 1):
            print(f"{idx}. {producto.mostrar_informacion()}")