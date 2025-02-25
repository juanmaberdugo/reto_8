class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_price(self, quantity=1):
        return self.price * quantity

    def get_details(self):
        return f"{self.name}: COP {self.price}"


class Beverage(MenuItem):
    def __init__(self, name, price, size, is_carbonated):
        super().__init__(name, price)
        self.size = size  # Size in milliliters
        self.is_carbonated = "Sí" if is_carbonated else "No"

    def get_details(self):
        return (
            f"{super().get_details()}, Tamaño: {self.size}ml, "
            f"Carbonatada: {self.is_carbonated}"
        )


class Appetizer(MenuItem):
    def __init__(self, name, price, portion_size, has_sauces):
        super().__init__(name, price)
        self.portion_size = portion_size
        self.has_sauces = "Sí" if has_sauces else "No"

    def get_details(self):
        return (
            f"{super().get_details()}, Porción: {self.portion_size}, "
            f"Con salsas: {self.has_sauces}"
        )


class MainCourse(MenuItem):
    def __init__(self, name, price, origin, cooking_time):
        super().__init__(name, price)
        self.origin = origin
        self.cooking_time = cooking_time  

    def get_details(self):
        return (
            f"{super().get_details()}, Origen: {self.origin}, "
            f"Tiempo de preparación: {self.cooking_time} min"
        )
    
class OrderIterator:
    def __init__(self, items):
        self._items = items
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._items):
            raise StopIteration
        item = self._items[self._index]
        self._index += 1
        return item
    

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item, quantity=1):
        self.items.append((menu_item, quantity))

    def calculate_total(self):
        return sum(item.calculate_price(quantity) for item, quantity in self.items)

    def generate_bill(self, filename):
        with open(filename, "w") as file:
            file.write("Factura\n")
            file.write("==========\n")
            for item, quantity in self:
                file.write(
                    f"{item.get_details()} x{quantity}: "
                    f"COP {item.calculate_price(quantity)}\n"
                )
            file.write("==========\n")
            file.write(f"Total: COP {self.calculate_total()}\n")
            file.write("==========\n")
            file.write("Gracias por su compra!\n")

    def get_order_details(self):
        receipt = "Detalles de la Orden:\n"
        for item, quantity in self:
            receipt += (
                f"{item.get_details()} x{quantity}: "
                f"COP {item.calculate_price(quantity)}\n"
            )
        receipt += f"Total: COP {self.calculate_total()}"
        return receipt

    def __iter__(self):
        return OrderIterator(self.items)


menu_items = [
    Beverage("Gaseosa", 2500.00, 500, True),
    Beverage("Café", 2000.00, 250, False),
    Beverage("Té Helado", 3000.00, 300, False),
    Appetizer("Papas Fritas", 4000.00, "Mediana", True),
    Appetizer("Nachos", 6000.00, "Grande", True),
    Appetizer("Alitas de Pollo", 8000.00, "Grande", True),
    MainCourse("Pasta Carbonara", 12000.00, "Italia", 15),
    MainCourse("Tacos al Pastor", 10000.00, "México", 10),
    MainCourse("Pollo Asado", 15000.00, "Colombia", 20),
    MainCourse("Sushi", 20000.00, "Japón", 25),
]

order = Order()
order.add_item(menu_items[0], 2)  
order.add_item(menu_items[3], 1)  
order.add_item(menu_items[6], 1)  
order.add_item(menu_items[7], 2)  

for item, quantity in order:
    print(f"{item.get_details()} x{quantity}: COP {item.calculate_price(quantity)}")

print("\nFactura generada en el archivo 'factura.txt'.")
order.generate_bill("factura.txt")
