# ==========================
# Product Class
# ==========================
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.__stock = stock   # private

    def get_stock(self):
        return self.__stock

    def reduce_stock(self, qty):
        if qty <= 0:
            return "Quantity must be greater than zero."
        elif qty > self.__stock:
            return "Not enough stock."
        else:
            self.__stock -= qty
            return f"Stock reduced by {qty}. Remaining stock is {self.__stock}."

    def increase_stock(self, qty):
        if qty <= 0:
            return "Quantity must be greater than zero."
        self.__stock += qty
        return f"Quantity increased by {qty}. Updated stock is {self.__stock}."

    def info(self):
        return (
            f"Product ID: {self.product_id} | "
            f"Name: {self.name} | "
            f"Price: ₹{self.price} | "
            f"Remaining stock: {self.__stock}"
        )


# ==========================
# Inventory Class
# ==========================
class Inventory:
    def __init__(self):
        # product_id → Product object
        self.products = {}

    def add_product(self, product_obj):
        if product_obj.product_id in self.products:
            return "Product already exists in inventory."
        self.products[product_obj.product_id] = product_obj
        return f"Product {product_obj.product_id} added to inventory"

    def search(self, product_id):
        # returns Product object OR None
        return self.products.get(product_id, None)

    def list_all_products(self):
        if not self.products:
            print("No products found in Inventory")
            return

        print("Inventory of products:")
        for product in self.products.values():
            print(f"  {product.info()}")

    def is_available(self, product_id, qty):
        product = self.products.get(product_id)
        if product is None:
            return False
        return product.get_stock() >= qty


# ==========================
# Customer Class
# ==========================
class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def info(self):
        return f"Customer ID: {self.customer_id} | Name: {self.name} | Email: {self.email}"


# ==========================
# CartItem Class
# ==========================
class CartItem:
    def __init__(self, product, quantity):
        self.product = product     # Product object
        self.quantity = quantity

    def totalprice(self):
        return self.quantity * self.product.price

# ==========================
# ShoppingCart Class
# ==========================
class ShoppingCart:
    def __init__(self, customer):
        self.customer = customer
        self.items = []   # list of CartItem

    def add_item(self, product, qty):
        if qty <= 0:
            return "Quantity must be greater than zero."

        if product.get_stock() < qty:
            return f"Not enough stock. Only {product.get_stock()} left."

        self.items.append(CartItem(product, qty))
        return f"{qty} x {product.name} added to shopping cart"

    def remove_item(self, product_id):
        for item in self.items:
            if item.product.product_id == product_id:
                self.items.remove(item)
                return "Item removed from shopping cart"
        return "Item not found in shopping cart"

    def cart_total(self):
        return sum(item.totalprice() for item in self.items)

    def cart_summary(self):
        if not self.items:
            print("Cart is empty.")
            return

        print("\n=== CART SUMMARY ===")
        print(self.customer.info())
        print("\nItems:")
        for item in self.items:
            print(f"{item.product.name} | Qty: {item.quantity} | Line Total: ₹{item.totalprice()}")
        print(f"\nTotal Amount: ₹{self.cart_total()}")


# ==========================
# Order Class
# ==========================
class Order:
    def __init__(self, order_id, customer, items, inventory):
        self.order_id = order_id
        self.customer = customer
        self.items = items              # list of CartItem objects
        self.__total_amount = 0         # private
        self.inventory = inventory      # Inventory object reference

        # Reduce stock immediately when order is created
        self.__reduce_stock_from_inventory()

    def __reduce_stock_from_inventory(self):
        for item in self.items:
            # get the product from inventory and reduce its stock
            product = self.inventory.products[item.product.product_id]
            product.reduce_stock(item.quantity)

    def calculate_total(self):
        self.__total_amount = sum(item.totalprice() for item in self.items)
        return self.__total_amount

    def get_total(self):
        return self.__total_amount

    def order_summary(self):
        # Ensure total is calculated
        if self.__total_amount == 0:
            self.calculate_total()

        print("\n===== ORDER SUMMARY =====")
        print(f"Order ID: {self.order_id}")
        print(self.customer.info())
        print("\nItems:")
        for item in self.items:
            print(f"{item.product.name} | Qty: {item.quantity} | Line Total: ₹{item.totalprice()}")
        print(f"\nTotal Amount: ₹{self.__total_amount}")
        print("=========================")


# ==========================================================
# DEMO FLOW: PRODUCTS → INVENTORY → CARTS → ORDERS
# ==========================================================

# 1️⃣ Create products
p1 = Product(101, "Laptop", 50000, 10)
p2 = Product(102, "Mouse", 500, 50)
p3 = Product(103, "Keyboard", 1500, 30)
p4 = Product(104, "Monitor", 12000, 20)
p5 = Product(105, "Headphones", 3000, 25)

# 2️⃣ Inventory and add products
inventory = Inventory()
for p in [p1, p2, p3, p4, p5]:
    print(inventory.add_product(p))

# 3️⃣ Inventory BEFORE orders
print("\n>>> INVENTORY BEFORE ORDERS:")
inventory.list_all_products()

# 4️⃣ Customers
c1 = Customer(1, "Rishi", "rishi@example.com")
c2 = Customer(2, "Neha", "neha@example.com")

# 5️⃣ Shopping carts
cart1 = ShoppingCart(c1)
cart2 = ShoppingCart(c2)

# 6️⃣ Add items to carts
print("\n>>> ADDING ITEMS TO CARTS:")
print(cart1.add_item(p1, 2))  # 2 Laptops
print(cart1.add_item(p2, 3))  # 3 Mice

print(cart2.add_item(p3, 1))  # 1 Keyboard
print(cart2.add_item(p4, 2))  # 2 Monitors
print(cart2.add_item(p5, 4))  # 4 Headphones

# 7️⃣ Cart summaries
print("\n>>> CARTS BEFORE ORDERS:")
cart1.cart_summary()
cart2.cart_summary()

# 8️⃣ Create Orders from carts
order1 = Order(order_id=1001, customer=c1, items=cart1.items, inventory=inventory)
order1.calculate_total()

order2 = Order(order_id=1002, customer=c2, items=cart2.items, inventory=inventory)
order2.calculate_total()

# 9️⃣ Order summaries
print("\n>>> ORDER SUMMARIES:")
order1.order_summary()
order2.order_summary()

# 🔟 Inventory AFTER orders
print("\n>>> INVENTORY AFTER ORDERS:")
inventory.list_all_products()
