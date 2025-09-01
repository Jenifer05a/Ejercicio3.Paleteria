class Paleta:
    def __init__(self, sabor: str, precio: float):
        self.sabor = sabor
        self.precio = precio

    def mostrar_informacion(self):
        print(f"Sabor: {self.sabor}")
        print(f"Precio base: ${self.precio}")

    def precio_final(self):
        return self.precio


class PaletaAgua(Paleta):
    def __init__(self, sabor, precio, base_agua=True):
        super().__init__(sabor, precio)
        self.base_agua = base_agua

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Tipo: Paleta de Agua")
        print("Base: Agua")

    def precio_final(self):
        return self.precio + 2


class PaletaCrema(Paleta):
    def __init__(self, sabor, precio, cremosa=True):
        super().__init__(sabor, precio)
        self.cremosa = cremosa

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Tipo: Paleta de Crema")
        print("Base: Cremosa")

    def precio_final(self):
        return self.precio + 6

    def cambiar_sabor(self, nuevo_sabor: str):
        self.sabor = nuevo_sabor


def main():

    paletas = [
        PaletaAgua("Limón", 12),
        PaletaCrema("Nuez", 28),
        PaletaAgua("Fresa", 14),
        PaletaCrema("Chocolate", 30)
    ]

    print(" Lista de Paletas ")

    for paleta in paletas:
        paleta.mostrar_informacion()
        print(f"Precio final: ${paleta.precio_final()}\n")


    nueva = input("Ingrese el nuevo sabor para la paleta de crema: ")
    if isinstance(paletas[1], PaletaCrema):
        paletas[1].cambiar_sabor(nueva)
        print("\nPaleta actualizada:")
        paletas[1].mostrar_informacion()
        print(f"Precio final: ${paletas[1].precio_final()}")


if __name__ == "__main__":
    main()
