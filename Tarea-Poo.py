

class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    def mostrar_info(self):
        print(f'Nombre: {self._nombre}, Precio: {self._precio}, Cantidad: {self._precio}')

    def restar_stock(self, cantidad_comprada):
        self._cantidad = cantidad_comprada

class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f'Talla: {self._talla}')

class RopaMujer (Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla
    
    def mostrar_info(self):
        super().mostrar_info()
        print(f'Talla: {self._talla}')

class Inventario:
    def __init__(self):
        self.prendas = []

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()

    def procesar_compra(self, nombre_prenda, cantidad):
        for prenda in self.prendas:
            if prenda._nombre ==  nombre_prenda:
                if prenda._cantidad >= cantidad:
                    prenda.restar_stock(cantidad)
                    return prenda._precio * cantidad
                else:
                    print(f'Stock insuficiente de {nombre_prenda}')
                    return 0
        print(f'{nombre_prenda} no está disponible')
        return 0
    
class Tienda:
    def __init__(self, inventario):
        self.inventario = inventario
        self.total_compra = 0

    def seleccionar_producto(self):
        self.inventario.mostrar_inventario()
        prenda = input('Qué prenda desea comprar?')
        cantidad = int(input(f'Cuántas unidades de {prenda} desea?'))
        costo = self.inventario.procesar_compra(prenda, cantidad)
        if costo > 0:
            self.total_compra += costo
            print(f'Compra exitosa. Costo: {costo:.2f}')
        else:
            print('No se pudo completar la compra')

    def mostrar_total(self):
        print(f'El total de su compra es: {self.total_compra:.2f}')

inventario = Inventario()
inventario.agregar_prenda(RopaHombre('Camisa de Hombre', 25.00, 50, 'M'))
inventario.agregar_prenda(RopaMujer('Falda de Mujer', 28.00, 15, 'M'))

tienda = Tienda(inventario)
tienda.seleccionar_producto()
tienda.mostrar_total()
