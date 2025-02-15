import os
import barcode
from barcode.writer import ImageWriter
import json

PRODUCTS_SN_DATAFILE = "products_serial-data.json"

def load_products():
    if os.path.exists(PRODUCTS_SN_DATAFILE):
        with open(PRODUCTS_SN_DATAFILE, "r") as file:
            return json.load(file)
    else:
        return {"last_serial": 100000, "products": []}

def save_products(data):
    """Save product data to JSON file."""
    try:
        with open(PRODUCTS_SN_DATAFILE, "w") as file:
            json.dump(data, file, indent=4)
        #print(f"JSON successfully updated: {data}")  # Debugging print
    except Exception as e:
        print(f"Error saving JSON: {e}")

def generate_serial_number(data):
    #print(f"Before update - last_serial: {data['last_serial']}")  # Debugging print

    new_serial = data["last_serial"] + 1
    data["last_serial"] = new_serial  # Update the last serial number

    #print(f"After update - last_serial: {data['last_serial']}")  # Debugging print

    return f"SN-{new_serial}"

def generate_barcode(serial_number):
    """Generate a barcode image for a given serial number."""
    barcode_type = barcode.get_barcode_class('code128')
    barcode_obj = barcode_type(serial_number, writer=ImageWriter())

    folder = "barcodes/"
    os.makedirs(folder, exist_ok=True)
    filename = f"{folder}{serial_number}.png"

    barcode_obj.save(filename)
    print(f"Barcode saved as {filename}")

def add_product():
    """Add a new product with a unique serial number and save it."""
    data = load_products() 

    product_name = input("Enter Product Name: ").strip()
    try:
        product_price = float(input("Enter Product Price: ").strip())
    except ValueError:
        print("Invalid price! Please enter a numeric value.")
        return

    serial_number = generate_serial_number(data) 

    new_product = {
        "name": product_name,
        "price": product_price,
        "serial": serial_number
    }

    data["products"].append(new_product)

    save_products(data) 

    generate_barcode(serial_number) 

    print(f"\nProduct '{product_name}' added successfully! Serial Number: {serial_number}")

def list_products():
    """List all registered products."""
    data = load_products()

    if not data["products"]:
        print("\nNo products found!")
        return
    
    print("\nList of Products:")
    print("-" * 40)
    for product in data["products"]:
        print(f"{product['name']} - $ {product['price']} - Serial Number: {product['serial']}")
    print("-" * 40)

def menu():
    """Display the main menu and handle user input."""
    while True:
        print("\n--- Market System Menu ---")
        print("1 - Add New Product")
        print("2 - List Products")
        print("0 - Exit")

        choice = input("Enter the desired option: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            list_products()
        elif choice == "0":
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Please try again.")

menu()
