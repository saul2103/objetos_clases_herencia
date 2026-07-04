# Sistema de Gestión de Restaurante - POO

**Estudiante:** Bryan Saul Iza Llano

---

## Descripción del Sistema

Este proyecto implementa un sistema de gestión para un restaurante utilizando Python. El sistema permite administrar el catálogo de productos mediante una jerarquía de clases que demuestra los principios fundamentales de la POO: herencia, encapsulación y polimorfismo.

La estructura se basa en una clase padre **Producto** y dos clases hijas especializadas:
* **Platillo:** Representa comidas o platos del restaurante con atributos específicos como calorías y tiempo de preparación.
* **Bebida:** Representa bebidas disponibles con atributos como volumen en mililitros y tipo de bebida.

---

##  Funcionalidades Principales

* Registrar productos (platillos y bebidas) en el catálogo del restaurante.
* Modificar precios con validación para evitar valores negativos o cero.
* Gestionar la disponibilidad de cada producto.
* Mostrar información detallada de cada producto según su tipo.
* Demostrar polimorfismo al recorrer una lista de productos y ejecutar `mostrar_informacion()` según el tipo de objeto.

El programa se ejecuta desde `main.py`, donde se crean instancias de prueba, se agregan al servicio principal y se muestran los resultados en consola para verificar el correcto funcionamiento del sistema.

---

## Estructura del Proyecto

```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py       # Clase padre Producto
│   ├── platillo.py       # Clase hija Platillo
│   └── bebida.py         # Clase hija Bebida
├── servicios/
│   ├── __init__.py
│   └── restaurante.py    # Clase de servicio Restaurante
└── main.py               # Punto de entrada del programa
```

### Responsabilidad de cada módulo

| Archivo | Clase | Descripción |
| :--- | :--- | :--- |
| `modelos/producto.py` | `Producto` | Clase padre que representa un producto general del restaurante. Contiene atributos comunes como nombre, precio (encapsulado) y disponibilidad. Incluye métodos para obtener y modificar el precio con validaciones. |
| `modelos/platillo.py` | `Platillo` | Clase hija que hereda de `Producto`. Agrega atributos específicos: calorías y tiempo_preparacion. Sobrescribe el método `mostrar_informacion()` para incluir estos detalles. |
| `modelos/bebida.py` | `Bebida` | Clase hija que hereda de `Producto`. Agrega atributos específicos: volumen_ml y tipo_bebida. Sobrescribe el método `mostrar_informacion()` para incluir estos detalles. |
| `servicios/restaurante.py` | `Restaurante` | Clase de servicio que administra una lista de productos registrados. Proporciona métodos para agregar productos y mostrar toda la información de forma organizada. |
| `main.py` | — | Punto de entrada del programa. Crea objetos de tipo `Platillo` y `Bebida`, los agrega al servicio `Restaurante`, demuestra el polimorfismo y muestra los resultados en consola. |

---

## Principios de POO Aplicados

### Herencia
* `Platillo` y `Bebida` heredan de `Producto`, reutilizando sus atributos y métodos.
* Uso de `super()` en las clases hijas para invocar el constructor de la clase padre.

### Encapsulación
* El atributo `__precio` en `Producto` está encapsulado como privado.
* Métodos públicos `obtener_precio()` y `cambiar_precio()` permiten acceder y modificar el precio de forma controlada.
* Validación en `cambiar_precio()` para evitar precios negativos o iguales a cero.

### Polimorfismo
* El método `mostrar_informacion()` está sobrescrito en ambas clases hijas.
* El `Restaurante` itera sobre una lista de `Producto` y ejecuta `mostrar_informacion()` sin conocer el tipo específico de cada objeto, demostrando comportamiento polimórfico.

---

## Reflexión sobre Modularización y Separación de Responsabilidades

La organización del software en módulos independientes es una práctica fundamental en el desarrollo de aplicaciones mantenibles y escalables. Al separar las clases `Producto`, `Platillo`, `Bebida` y `Restaurante` en archivos distintos dentro de carpetas con responsabilidades bien definidas (modelos para las entidades del dominio y servicios para la lógica de gestión), se logran varios beneficios:

* **Reutilización:** Las clases pueden importarse y utilizarse en diferentes partes del proyecto sin duplicar código.
* **Mantenibilidad:** Cada módulo puede modificarse de forma aislada, reduciendo el riesgo de introducir errores en otras partes del sistema.
* **Legibilidad:** La estructura del proyecto comunica de forma inmediata la arquitectura del software a cualquier desarrollador que se una al proyecto.
* **Separación de responsabilidades:** `Producto` solo se preocupa por sus propios datos y comportamiento, mientras que `Restaurante` actúa como coordinador. Esto evita clases sobrecargadas con múltiples responsabilidades (principio SRP de SOLID).
* **Pruebas unitarias simplificadas:** Al estar las clases desacopladas, se pueden probar individualmente simulando dependencias.

En conclusión, modularizar el software y asignar responsabilidades claras a cada componente no es solo una buena práctica académica, sino una necesidad real para construir sistemas robustos que puedan crecer y adaptarse con el tiempo.
