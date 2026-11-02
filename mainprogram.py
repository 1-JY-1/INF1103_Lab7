import inventory

class mainprogram:
    def __init__(self):
        # Create one inventory object
        self.inventory = inventory.inventory()

    def getuserinput(self, user_input):
        try:
            user_input = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            return
        
        if user_input == 1:
            print("\nCurrent Inventory")
            print("===========================================================================")
            if not self.inventory.products:
                print("No products found.")
            else:
                for product_obj in self.inventory.products:
                    print("===========================================================================")
                    product_obj.display_information()
                    product_obj.get_fulfilment_info()
                    print("===========================================================================")
            print("===========================================================================")

        elif user_input == 2:
            print("===========================================================================")
            print("Add a new product to the inventory")
            self.inventory.addproduct()
            print("===========================================================================")

        elif user_input == 3:
            print("===========================================================================")
            print("Update the stock of the product")
            self.inventory.updateproduct()
            print("===========================================================================")

        elif user_input == 4:
            print("===========================================================================")
            print("Search for the product")
            self.inventory.searchproduct()
            print("===========================================================================")

        elif user_input == 5:
            print("===========================================================================")
            print("Save Inventory")
            self.inventory.storesproduct()
            print("===========================================================================")

        elif user_input == 6:
            print("===========================================================================")
            print("Quit the app")

        else:
            print("Invalid input. Please enter a number between 1 and 6.")


