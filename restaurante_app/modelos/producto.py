class Producto:
    def __init__(self, nombre, precio, disponibilidad=True):
        self.nombre = nombre
        self.__precio = precio
        self.disponibilidad = disponibilidad

    def obtener_precio(self):
        return self.__precio

    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            return True
        return False

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponibilidad else "No disponible"
        return f"{self.nombre} - ${self.obtener_precio():.2f} - {estado}"