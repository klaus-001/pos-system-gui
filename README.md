<h1 style="text-align: center;">Point of Sale (POS) System </h1>

A **Point of Sale (POS) system** consists of both hardware and software that enables businesses to handle sales transactions. It usually features a register, a card reader, and software that manages sales, inventory, and customer information. POS systems are applicable in a range of environments, such as retail shops, restaurants, and service-oriented businesses. They are crucial for businesses to manage sales transactions, monitor inventory, and enhance operational efficiency.

## Table of Contents

## Overview

This Python project simulates the software used in handling sales transactions of a product, specifically for the use in restaurants. The code utilizes a `POSsystem` class to easily and efficiently handle the adding and removing of items, calculation of cost, and the generating of sales invoice. This project is implemented using Python and the Tkinter GUI library for a simple and intuitive user experience.

## Features

- **User-friendly Design:** The app features a simple and intuitive interface design that enhances the user's experience by allowing for effortless navigation and quick access to essential features.
- **After-Tax Calculation:** Realistically replicates real-world situations by incorporating a 7% Goods and Services Tax (GST) into the overall cost.
- **Unique ID Reference:** Generates a 6-character unique identifier for every transaction, which enables the owner to monitor and record every transaction made with precision and accuracy.
- **Sales Invoice:** Generates a comprehensive sales invoice that includes the date and time of the transaction, the subtotal and total cost of items, the applicable tax percentage, and a detailed list of all items ordered.
- **Multiple Payment Options:** Easily toggle between cash or card payment.
- **Backup JSON File:** A backup copy of all sales invoices is maintained in JSON format, enabling easy access and retrieval of the data whenever needed.

## Full Code

```python
class POSsystem:
	def __init__(self, window):
        pass
		
	def create_widgets(self):
        pass
		
	def add_menu(self, item: dict):	
        pass
	
	def add_bills(self, bill: dict):
        pass

	def calculate_change(self, subtotal: int, received: int):
        pass
	
	def cancel(self):
        pass
				
	def clear(self):
        pass
				
	def submit(self):
        pass
					
	def payment_mode(self):
        pass
			
	def display_orders(self, order_list: list):
        pass
			
	def display_total(self, total: int, received: int, change: int):
        pass
										  
	def display_error(self, message):
        pass
										  
	def generate_id(self):
        pass
											  
	def generate_sales_invoice(self, finalOrderList: list, subtotal: int):
        pass
		
	def write_to_file(self, transaction):
        pass

if __name__ == '__main__':
	window = Tk()
	pos_system = POSsystem(window)
	window.mainloop()

```

## Code Overview

-  `__init__()`: This method initializes the required attributes for the POS system.
- `create_widgets()`: This method sets up the interface the users will interact with.
- `add_menu()`: This method adds the menu item selected by the user and updates the corresponding displays accordingly.
- `add_bills()`: This method adds the bill selected by the user and updates the corresponding displays accordingly.
- `calculate_changes()`: This method calculates the change that the customer should receive.
- `cancel()`: This method sends a signal to cancel the entire transaction process, resetting the interface to its original state.
- `clear()`: This method sends a signal to remove the last selected item or bill chosen by the user.
- `submit()`: This method sends a signal to process the transaction order. Ensure orders are finalized and customer has given a mode of payment.
- `payment_mode()`: This method selects the mode of payment, which can be either cash or card, as specified by the customer.
- `display_orders()`: This method is called when necessary to update the display that shows the items ordered by the customer.
- `display_total()`: This method is called when necessary to update the display that shows the total cost of all items ordered by the customer.
- `display_error()`: This method is called when there is a need to update the display to show any errors encountered while using the POS system.
- `generate_id()`: This method generates a unique 6-character ID.
- `generate_sales_invoice()`: This method generates the sales invoice for each transaction.
- `write_to_file()`: This method writes the generated sales invoice to a json file.

## Possible Improvements

1. Add a database to store all transaction details.

2. Chage the labels **F1-F9** to the name of the food items or add a way for the user to identify which food item is behind which label (e.g. creating a pop-up message).

3. The POS system is currently only capable of storing 9 food items, we can add a menu bar to the project to allow changes from foods only to also drinks, desserts, and etc.

This project is far from perfect and there are numerous ways to improve it. Contributions are encouraged, please feel free to make useful changes to the project.

## Project Structure

### main.py

This file contains the `POSsystem` class 

## Installation

## Usage

## Contributing

## License
