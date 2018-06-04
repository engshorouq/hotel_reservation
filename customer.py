class customer():
	Customers=[]
	def __init__(self,customer_full_name,customer_phone_number):
		assert str is type(customer_full_name) and customer_full_name is not None , "requires a string"
		assert str is type(customer_phone_number) and customer_phone_number is not None , "requires a string"
		self.customer_full_name=customer_full_name
		self.customer_phone_number=customer_phone_number

	def add_customer(self):		
		for cu in customer.Customers:
			if(cu.customer_full_name==self.customer_full_name and cu.customer_id == self.customer_id):
				print('The customer exist')
		if result :
			customer.Customers.append(self)	
			print('The customer added')				
