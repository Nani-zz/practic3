class Product:
    def __init__(self, name, price, kolvo, category):
        self.name = name
        self.price = price
        self.kolvo = kolvo
        self.category = category

    def is_available(self, quantity=1):
        return self.kolvo >= quantity

    def reduce_kolvo(self, quantity):
        if not self.is_available(quantity):
            raise ValueError(f"Недостаточно товара «{self.name}» на складе")
        self.kolvo -= quantity

    def __str__(self):
        return f"{self.name} ({self.category}) — {self.price} руб., на складе: {self.kolvo}"


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add(self, product, quantity=1):
        new_quantity = self.items.get(product, 0) + quantity
        self.items[product] = new_quantity

    def remove(self, product):
        self.items.pop(product, None)

    def update_quantity(self, product, quantity):
        if quantity <= 0:
            self.remove(product)
            return
        if not product.is_available(quantity):
            raise ValueError(f"На складе только {product.stock} шт. «{product.name}»")
        self.items[product] = quantity

    def subtotal(self):
        return sum(product.price * qty for product, qty in self.items.items())

    def is_empty(self):
        return not self.items

    def clear(self):
        self.items = {}

    def __str__(self):
        if self.is_empty():
            return "Корзина пуста"
        lines = [f"  {p.name} × {q} = {p.price * q} руб." for p, q in self.items.items()]
        return "Корзина:\n" + "\n".join(lines) + f"\n  Итого: {self.subtotal()} руб."


class Order:
    nalog = 0.20
    next_id = 1

    def __init__(self, customer, items, discount_percent=0):
        self.id = Order.next_id
        Order.next_id += 1
        self.customer = customer
        self.items = dict(items)
        self.discount_percent = discount_percent
        self.status = "создан"

    def subtotal(self):
        return sum(p.price * q for p, q in self.items.items())

    def discount_amount(self):
        return round(self.subtotal() * self.discount_percent / 100, 2)

    def tax_amount(self):
        return round((self.subtotal() - self.discount_amount()) * self.nalog, 2)

    def total(self):
        return round(self.subtotal() - self.discount_amount() + self.tax_amount(), 2)

    def process(self):
        for product, qty in self.items.items():
            if not product.is_available(qty):
                self.status = "отменён"
                raise ValueError(f"Товар «{product.name}» закончился")
        for product, qty in self.items.items():
            product.reduce_kolvo(qty)
        self.status = "оплачен"

    def __str__(self):
        lines = [f"Заказ №{self.id} ({self.status}) — {self.customer.name}"]
        for p, q in self.items.items():
            lines.append(f"  {p.name} × {q} = {p.price * q} руб.")
        lines.append(f"  Сумма:   {self.subtotal()} руб.")
        lines.append(f"  Скидка:  -{self.discount_amount()} руб. ({self.discount_percent}%)")
        lines.append(f"  Налог:   +{self.tax_amount()} руб. ({int(self.nalog * 100)}%)")
        lines.append(f"  К оплате: {self.total()} руб.")
        return "\n".join(lines)


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = ShoppingCart()
        self.orders = []            # история заказов

    def checkout(self, discount_percent=0):
        order = Order(self, self.cart.items, discount_percent)
        order.process()
        self.orders.append(order)
        self.cart.clear()
        return order

    def order_history(self):
        if not self.orders:
            return f"У {self.name} пока нет заказов"
        lines = [f"История заказов {self.name}:"]
        for order in self.orders:
            lines.append(f"  №{order.id}: {order.total()} руб. — {order.status}")
        spent = sum(order.total() for order in self.orders)
        lines.append(f"  Всего потрачено: {spent} руб.")
        return "\n".join(lines)


laptop = Product("Ноутбук", 75_000, kolvo=3, category="Электроника")
mouse = Product("Мышь", 1_500, kolvo=10, category="Электроника")
book = Product("Книга «Женщины»", 1_200, kolvo=5, category="Книги")

lexa = Customer("Алексей", "alex@777.com")

lexa.cart.add(laptop)
lexa.cart.add(mouse, 2)
lexa.cart.add(book)
print(lexa.cart, "\n")

lexa.cart.update_quantity(mouse, 1)
lexa.cart.remove(book)
print(lexa.cart, "\n")

order1 = lexa.checkout(discount_percent=10)
print(order1, "\n")

lexa.cart.add(book, 2)
order2 = lexa.checkout()
print(order2, "\n")

print(lexa.order_history(), "\n")
print("Остатки на складе:")
for product in (laptop, mouse, book):
    print(" ", product)