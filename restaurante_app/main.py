from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def main():
    restaurante = Restaurante()

    platillo1 = Platillo("Caldo de Pata", 4.99, 850, 20)
    platillo2 = Platillo("Seco de Pollo", 3.00, 450, 10, False)
    
    bebida1 = Bebida("Coca-Cola", 3.00, 330, "Gaseosa")
    bebida2 = Bebida("Jugo Natural", 4.50, 400, "Jugo", False)

    restaurante.agregar_producto(platillo1)
    restaurante.agregar_producto(platillo2)
    restaurante.agregar_producto(bebida1)
    restaurante.agregar_producto(bebida2)

    print("Precios modificados...")
    platillo1.cambiar_precio(5.99)
    bebida1.cambiar_precio(3.25)
    
    if not bebida2.cambiar_precio(-5.00):
        print("No se permiten precios negativos o cero")

    restaurante.mostrar_productos()

if __name__ == "__main__":
    main()