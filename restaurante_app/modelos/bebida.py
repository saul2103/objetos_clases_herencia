from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, volumen_ml, tipo_bebida, disponibilidad=True):
        super().__init__(nombre, precio, disponibilidad)
        self.volumen_ml = volumen_ml
        self.tipo_bebida = tipo_bebida

    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base} - {self.volumen_ml} ml - {self.tipo_bebida}"