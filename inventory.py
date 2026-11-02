import filehandling
import product

class inventory:
    def __init__(self):
        self.products = []

        # Load products from JSON only once when inventory is created
        file_handling = filehandling.filehandling()
        file_handling.load_inventory()

        for product_data in file_handling.productdetail["products"]:

            if "weight" in product_data:
                product_obj = product.physicalProduct(
                    id=product_data["ID"],
                    type=product_data["type"],
                    name=product_data["name"],
                    price=product_data["price"],
                    stock=product_data["stock"],
                    weight=product_data["weight"]
                )
            elif "download_size" in product_data:
                product_obj = product.digitalProduct(
                    id=product_data["ID"],
                    type=product_data["type"],
                    name=product_data["name"],
                    price=product_data["price"],
                    stock=product_data["stock"],
                    download_size=product_data["download_size"]
                )
            self.products.append(product_obj)

    def storesproduct(self):
        # Save the current product objects to JSON
        file_handling = filehandling.filehandling()
        file_handling.save_inventory(self.products)

    def addproduct(self):
        # Validate product ID
        try:
            add_id = int(input("Enter the product ID: "))

            for item in self.products:
                if item.id == add_id:
                    print("Product ID already exists. Please enter a unique product ID.")
                    return

        except ValueError:
            print("Invalid input. Please enter a valid product ID.")
            return

        # Validate product name
        add_product = input("Enter the product name: ").strip()

        if not add_product:
            print("Invalid input. Product name cannot be empty.")
            return

        # Validate price
        try:
            add_price = float(input("Enter the product price: "))

            if add_price <= 0:
                print("Invalid input. Please enter a positive number for price.")
                return

        except ValueError:
            print("Invalid input. Please enter a valid product price.")
            return

        # Validate stock
        try:
            add_stock = int(input("Enter the product stock: "))

            if add_stock <= 0:
                print("Invalid input. Please enter a positive number for stock.")
                return

            if add_stock > 500:
                print("Inventory cannot exceed 500 items. Please enter a smaller amount.")
                return

        except ValueError:
            print("Invalid input. Please enter a valid product stock.")
            return

        type_choice = input("Is this a physical product or digital product? (Enter 'physical' or 'digital'): ").strip().lower()

        if type_choice == "physical":
            try:
                add_weight = float(input("Enter the product weight (in kg): "))

                if add_weight <= 0:
                    print("Invalid input. Please enter a positive number for weight.")
                    return

            except ValueError:
                print("Invalid input. Please enter a valid product weight.")
                return
            new_product = product.physicalProduct(add_id, type_choice, add_product, add_price, add_stock, add_weight)

        elif type_choice == "digital":
            try:
                add_download_size = float(input("Enter the product download size (in MB): "))

                if add_download_size <= 0:
                    print("Invalid input. Please enter a positive number for download size.")
                    return

            except ValueError:
                print("Invalid input. Please enter a valid product download size.")
                return
            new_product = product.digitalProduct(add_id, type_choice, add_product, add_price, add_stock, add_download_size)

        else:
            print("Invalid input. Please enter 'physical' or 'digital'.")
            return

        # Create a product object and add it to the existing list
        self.products.append(new_product)

        print("Product added successfully!")

    def updateproduct(self):

        try:
            update_id = int(input("Enter the product ID to update: "))
            for item in self.products:
                if item.id == update_id:
                    item.updatestock()
                    pass
                    
            print("Product ID not found.")

        except ValueError:
            print("Invalid input. Please enter a valid product ID.")
        pass

    def searchproduct(self):

        try:
            search_id = int(input("Enter the product ID to search: "))
            for item in self.products:
                if item.id == search_id:
                    print("===================================================================================================================")
                    print(f"Product found: ID: {item.id} | Type: {item.type} | Name: {item.name} | Price: {item.price} | Stock: {item.stock}")
                    print("===================================================================================================================")
                    return
            print("Product ID not found.")
        except ValueError:
            print("Invalid input. Please enter a valid product ID.")
        pass

