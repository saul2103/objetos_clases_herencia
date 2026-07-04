from modelos.producto import Producto

class Platillo(Producto):
    def __init__(self, nombre, precio, calorias, tiempo_preparacion, disponibilidad=True):
        super().__init__(nombre, precio, disponibilidad)
        self.calorias = calorias
        self.tiempo_preparacion = tiempo_preparacion

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base} - {self.calorias} kcal - {self.tiempo_preparacion} min"