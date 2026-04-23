# Clase base que representa un ítem del menú
class MenuItem:
  def __init__(self, name: str, price: float):
    # Nombre del producto
    self.name = name
    # Precio del producto
    self.price = price


# Clase que representa los platos principales (hereda de MenuItem)
class Entrees(MenuItem):
  def __init__(self, name: str, price: float, Vegan: bool):
    # Inicializa los atributos heredados (name y price)
    super().__init__(name, price)
    # Indica si el plato es vegano o no
    self.Vegan = Vegan


# Clase que representa las entradas
class Appetizers(MenuItem):
  def __init__(self, name: str, price: float, shareable: bool):
    # Inicializa atributos heredados
    super().__init__(name, price)
    # Indica si el plato es para compartir
    self.shareable = shareable


# Clase que representa los postres
class Desserts(MenuItem):
  def __init__(self, name: str, price: float, Warm: bool):
    # Inicializa atributos heredados
    super().__init__(name, price)
    # Indica si el postre se sirve caliente
    self.Warm = Warm


# Clase que representa ensaladas
class Salad(MenuItem):
  def __init__(self, name: str, price: float, oil: bool):
    # Inicializa atributos heredados
    super().__init__(name, price)
    # Indica si contiene aceite
    self.oil = oil


# Clase que representa bebidas
class Beverages(MenuItem):
  def __init__(self, name: str, price: float, alcohol: bool):
    # Inicializa atributos heredados
    super().__init__(name, price)
    # Indica si la bebida contiene alcohol
    self.alcohol = alcohol


# Clase que representa una orden de compra
class Order:
  def __init__(self):
    # Lista donde se almacenan los ítems agregados al pedido
    self.Lista = []

  def add_item(self, item):
    # Método para agregar un ítem al pedido
    self.Lista.append(item)

  def Discounts(self):
    # Obtiene los tipos de cada ítem en la orden
    types = [type(order_item.item).__name__ for order_item in self.item]
    
    # Lista donde se guardarán los ítems con descuento
    discount_item = []
    
    # Si hay entradas y bebidas, se aplica descuento a esos ítems
    if "Appetizers" in types and "Beverages" in types:
      for order_item in self.Items:
        if isinstance(order_item.item, (Appetizers, Beverages)):
          discount_item.append((order_item.item, 0.2))

    # Si hay platos fuertes y ensaladas, se aplica descuento a esos ítems
    if "Entrees" in types and "Salad" in types:
      for order_item in self.Items:
        if isinstance(order_item.item, (Entrees, Salad)):
          discount_item.append((order_item.item, 0.2))


# Función para calcular el total de la cuenta considerando descuentos
def total_bill(self):
    # Obtiene los ítems con descuento
    discount_items = self.calculate_discount()
    
    # Variable acumuladora del total
    total = 0

    # Recorre cada ítem de la orden
    for order_item in self.items:
        # Calcula el subtotal de cada ítem
        subtotal = order_item.subtotal()
        
        # Inicializa el descuento en 0
        discount = 0

        # Verifica si el ítem tiene descuento
        for d_item, d_value in discount_items:
            if d_item == order_item:
                discount = d_value

        # Suma el subtotal aplicando el descuento correspondiente
        total += subtotal * (1 - discount)

    # Imprime el total de la cuenta
    print(f"El total de su cuenta es {total}")


# Punto de entrada del programa
if __name__ == "__main__":
    # Creación de platos principales
    BandejaPaisa = Entrees("Bandeja Paisa", 50000, False)
    Sancocho = Entrees("Sancocho", 45000, False)

    # Creación de entradas
    Empanada = Appetizers("Empanada", 2000, True)
    PanDeBono = Appetizers("Pan de Bono", 1000, True)

    # Creación de postres
    ArrozConLeche = Desserts("Arroz con Leche", 5000, True)
    Milhoja = Desserts("Milhoja", 30000, False)

    # Creación de ensaladas
    Defruta = Salad("Defruta", 2000, False)
    Lechuga = Salad("Lechuga", 1000, True)

    # Creación de bebidas
    CocaCola = Beverages("CocaCola", 2000, False)
    Refajo = Beverages("Refajo", 1500, True)


# Prueba:
pedido1 = Order()
pedido1.add_item(CocaCola)
pedido1.add_item(Milhoja)
pedido1.add_item(ArrozConLeche)
pedido1.add_item(Lechuga)
pedido1.Total_Bill_Amount()
pedido1.add_item(Empanada)
pedido1.Total_Bill_Amount()
pedido1.Lista