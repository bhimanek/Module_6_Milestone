# ItemToPurchase class definition
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

# ShoppingCart class definition
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                return
        print("Item not found in cart. Nothing removed.")

    def modify_item(self, modified_item):
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                if modified_item.item_price != 0:
                    item.item_price = modified_item.item_price
                if modified_item.item_quantity != 0:
                    item.item_quantity = modified_item.item_quantity
                return
        print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.item_quantity * item.item_price for item in self.cart_items)

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

# Function to display menu and execute user commands
def print_menu(cart):
    menu = """
    MENU
    a - Add item to cart
    r - Remove item from cart
    c - Change item quantity
    i - Output items' descriptions
    o - Output shopping cart
    q - Quit
    Choose an option: """
    while True:
        option = input(menu).strip()
        if option == 'a':
            name = input("Enter the item name: ")
            price = float(input("Enter the item price: "))
            quantity = int(input("Enter the item quantity: "))
            cart.add_item(ItemToPurchase(name, price, quantity))
        elif option == 'r':
            name = input("Enter the item name to remove: ")
            cart.remove_item(name)
        elif option == 'c':
            name = input("Enter the item name: ")
            price = float(input("Enter the new price (0 to leave unchanged): "))
            quantity = int(input("Enter the new quantity (0 to leave unchanged): "))
            cart.modify_item(ItemToPurchase(name, price, quantity))
        elif option == 'i':
            cart.print_descriptions()
        elif option == 'o':
            cart.print_total()
        elif option == 'q':
            break
        else:
            print("Invalid option. Please try again.")

# Main function
if __name__ == "__main__":
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    my_cart = ShoppingCart(customer_name, current_date)
    print_menu(my_cart)
