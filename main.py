import string
import random
import json
import os

from tkinter import *
from datetime import datetime
from menu import menu_items
from bills import bills

class POSsystem:
	def __init__(self, window):
		self.window = window
		
		# Initialize file path
		self.file_path = 'sales_record.json'
		
		self.orders = []
		self.subtotal_amount = 0
		
		self.bills_added = []
		self.amount_received = 0
		
		self.change = 0
		
		# Set default mode of payment to cash
		self.mode_state = 0
		
		self.create_widgets()
		
	def create_widgets(self):
		self.window.geometry('500x500')
		self.window.resizable(False, False)
		
		self.window.title('POS System')
		
		# Create display screen
		self.order_label = Label(self.window,
								 text='Order:',
								 font=('Arial', 45, 'bold'),
								 fg='white',
								 bg='black')
								 
		self.order_label.place(x=300, y=0, width=200, height=100)
		
		self.screen = Label(self.window,
							text='',
							font=('Arial', 9),
							fg='white',
							bg='black',
							justify='left',
							anchor='nw')
							
		self.screen.place(x=300, y=100, width=200, height=300)
		
		self.amount_label = Label(self.window,
								  text=f'Total:' +
									   f'\nReceived:' +
									   f'\n--------------------------------------' +
									   f'\nChange:',
								  font=('Arial', 12),
								  fg='white',
								  bg='black',
								  justify='left',
								  anchor='nw')
								 
		self.amount_label.place(x=300, y=400, width=200, height=100)
		
		# Create frame to store menu buttons
		self.frame = Frame(self.window, bg='white')
		self.frame.place(x=0, y=0, width=300, height=400)
		
		self.menu_buttons = []
		for i, item in enumerate(menu_items):
			button = Button(self.frame,
							text=item['code'],
							fg='black',
							activeforeground='black',
							activebackground='light grey',
							width=11,
							height=7,
							borderwidth=0,
							# Takes in dict as argument
							command=lambda item=item: self.add_menu(item))
							
			button.grid(row=i//3, column=i%3, padx=8, pady=12)
			self.menu_buttons.append(button)

		# Create frame to store function buttons
		self.frame2 = Frame(self.window, bg='white')
		self.frame2.place(x=0, y=400, width=300, height=100)
		
		self.cancel_button = Button(self.frame2,
							 		text='cancel',
							 		bg='red',
							 		width=8,
							 		height=3,
							 		command=self.cancel)
							 
		self.cancel_button.grid(row=0, column=0, padx=7, pady=20)
		
		self.clear_button = Button(self.frame2,
								   text='clear',
								   bg='yellow',
								   width=8,
								   height=3,
								   command=self.clear)
							
		self.clear_button.grid(row=0, column=1)
		
		self.submit_button = Button(self.frame2,
							 		text='submit',
							 		bg='green',
							 		width=8,
							 		height=3,
							 		command=self.submit)
							 
		self.submit_button.grid(row=0, column=2, padx=7)
		
		self.mode_button = Button(self.frame2,
						   		  text='card/cash',
						   		  width=8,
						   		  height=3,
						   		  command=self.payment_mode)
						   
		self.mode_button.grid(row=0, column=3)
		
	def add_menu(self, item: dict):	
		self.orders.append(item['name'])
		self.display_orders(self.orders)
		# print(self.orders)
			
		self.subtotal_amount += item['price']
		self.display_total(self.subtotal_amount, self.amount_received, self.change)
		# print(self.subtotal_amount)
	
	def add_bills(self, bill: dict):
		if self.subtotal_amount > 0:
			self.bills_added.append(bill['amount'])
			self.amount_received += bill['amount']
			self.display_total(self.subtotal_amount, self.amount_received, self.change)
			# print(self.amount_received)
			
	def calculate_change(self, subtotal: int, received: int):
		total = (subtotal * 107/100)
		change = received - total	
		
		return change
	
	def cancel(self):
		# Reset initial state
		self.orders = []
		self.subtotal_amount = 0
		self.bills_added = []
		self.amount_received = 0
		self.change = 0
		self.mode_state = 0
		
		self.display_orders(self.orders)
		self.display_total(self.subtotal_amount, self.amount_received, self.change)
		
		for button, item in zip(self.menu_buttons, menu_items):
			button.config(text=item['code'],
						  state='normal',
						  command=lambda item=item: self.add_menu(item))
				
	def clear(self):
		if self.menu_buttons[0].cget('text') == '10¢':
			if len(self.bills_added) != 0:
				last_bill = self.bills_added.pop()
				self.amount_received -= last_bill
				
				self.display_orders(self.orders)	
				self.display_total(self.subtotal_amount, self.amount_received, self.change)
		
		else:
			if len(self.orders) != 0:
				last_item = self.orders.pop() # removes last item on list
				
				# Find the price of the last item in the menu_items list
				for item in menu_items:
					if item['name'] == last_item:
						self.subtotal_amount -= item['price']
						break 
				
				# Update screen
				self.display_orders(self.orders)	
				self.display_total(self.subtotal_amount, self.amount_received, self.change)
				
	def submit(self):
		if self.amount_received >= self.subtotal_amount:
			self.change += self.calculate_change(self.subtotal_amount, self.amount_received)
			# print(self.change)
			self.display_total(self.subtotal_amount, self.amount_received, self.change)
			
			transaction = self.generate_sales_invoice(self.orders, self.subtotal_amount)
			self.write_to_file(transaction)
			
			self.window.after(3000, self.cancel) # Delay the execution of self.cancel by 3 seconds
					
	def payment_mode(self):
		if self.mode_state == 0:
			print('Cash payment selected')
			# The zip function is used to iterate over two lists in parallel
			# Matches the index placement on both lists
			for button, bill in zip(self.menu_buttons, bills):
				button.config(text=bill['code'],
							  state='normal',
							  command=lambda bill=bill: self.add_bills(bill))
							  
			self.mode_state = 1
		else:
			print('Card payment selected')
			for button in self.menu_buttons:
				button.config(state='disabled')
			self.mode_state = 0 # Reset button state to 0
			
	def display_orders(self, order_list: list):
		if len(order_list) != 0:
			item_counts = {}
			for item in order_list:
				if item in item_counts:
					item_counts[item] += 1
				else:
					item_counts[item] = 1
			# print(item_counts)
			order_text = ''
			for key, value in item_counts.items():
				item_info = next((item for item in menu_items if item['name'] == key), None)
				
				price = item_info['price']	
				order_text += f'{key} x{value}\n${price:.2f}\n'
					
			self.screen.config(text=order_text,
							   font=('Arial', 9),
							   justify='left',
							   anchor='nw')
			
		else:
			self.screen.config(text='',
							   font=('Arial', 9),
							   justify='left',
							   anchor='nw')
			
	def display_total(self, total: int, received: int, change: int):
		if total == 0 and received == 0 and change == 0:
			self.amount_label.config(text=f'Total:' +
										  f'\nReceived:' +
										  f'\n--------------------------------------' +
										  f'\nChange:')
										  
		elif total > 0 and received == 0 and change == 0:
			self.amount_label.config(text=f'Total: ${(total * 107/100):.2f}' +
										  f'\nReceived:' +
										  f'\n--------------------------------------' +
										  f'\nChange:')								
										
		elif total > 0 and received > 0 and change == 0:
			self.amount_label.config(text=f'Total: ${(total * 107/100):.2f}' +
										  f'\nReceived: ${received:.2f}' +
										  f'\n--------------------------------------' +
										  f'\nChange:')
										  
		elif total > 0 and received > 0 and change > 0:
			self.amount_label.config(text=f'Total: ${(total * 107/100):.2f}' +
										  f'\nReceived: ${received:.2f}' +
										  f'\n--------------------------------------' +
										  f'\nChange: ${change:.2f}')
										  
	def display_error(self, message):
		self.screen.config(text=message,
						   font=('Arial', 16),
						   justify='center',
						   anchor='center')
										  
	def generate_id(self):
		keys = string.ascii_letters + string.digits
		id_key = ''
		
		for i in range(6):
			i = random.choice(keys)
			id_key += i
			
		return id_key
											  
	def generate_sales_invoice(self, finalOrderList: list, subtotal: int):
		id_key = self.generate_id()
		
		current_date = datetime.now().strftime('%d-%m-%Y')
		current_time = datetime.now().strftime('%I:%M %p')
		
		item_counts = {}
		for item in finalOrderList:
			if item in item_counts:
				item_counts[item] += 1
			else:
				item_counts[item] = 1

		orders = []
		for key, value in item_counts.items():
			item_info = next((item for item in menu_items if item['name'] == key), None)
			price = item_info['price']
			
			order = {'name': key, 'QTY': value, 'price': price}	
			orders.append(order)
			
		transaction = {'id': id_key, 
					   'receipt': {'date': current_date,
								   'time': current_time,
								   'total': round((subtotal * 107/100), 2),
								   'subtotal': subtotal,
								   'tax%': 7,
								   'order': orders
								   }
					   }
	
		return transaction
		
	def write_to_file(self, transaction):
		try:
			if not os.path.exists(self.file_path):		
				with open(self.file_path, 'w') as file:
					json.dump([transaction], file, indent=2)
						
			else:
				with open(self.file_path, 'r+') as file:	
					data = json.load(file)
				
					data.append(transaction)
					
					file.seek(0)
					json.dump(data, file, indent=2)	
					file.truncate() # truncate the file to the current position
				
		except json.JSONDecodeError:
			with open(self.file_path, 'a') as file:
				json.dump([transaction], file, indent=2)
						
		except Exception:
			self.display_error('--System Error--')
			self.window.after(3000, self.cancel)
					
if __name__ == '__main__':
	window = Tk()
	pos_system = POSsystem(window)
	window.mainloop()



