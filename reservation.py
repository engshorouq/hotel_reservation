from hotel import hotel
import customer
from twilio import rest
class reservation():
	Reservations=[]

	def __init__(self,hotel_name,customer_name):
		assert hotel_name is not None and str is type(hotel_name),"require hotel"
		assert self.hotel_exist(hotel_name) , "the hotel name not exist"
		assert customer_name is not None and str is type(customer_name),"require customer"		  
		self.hotel_name=hotel_name
		self.customer_name=customer_name
		
		

	def reserve_room(self,hotel_name,customer_name):
		#hotel_obj=None
		for x in hotel.Hotels :
			if(x.hotel_name == hotel_name):
				if(x.empty_rooms==0):
					return False
				else:
					reservation.Reservations.append(reservation(hotel_name,customer_name))
					x.empty_rooms=x.empty_rooms-1					
					return True
		

	def hotel_exist(self,hotel_name):
		for x in hotel.Hotels :
			if(x.hotel_name == hotel_name):								
				return True			
		return False	


	def add_new_reservation(self):
		a=self.hotel_name
		b=self.customer_name		
		if(self.reserve_room(a,b)):
			#print('confirmation')
			number=input('Please Enter Your Phone Number To Complete Confirmation  :')
			new_customer=customer.customer(b,number)
			#customer.customer.add_customer()
			self.send_text_message(number)
			print('Check Your Phone Please ')
		else:
			print('sorry no room available ')


	def send_text_message(self,number):
		account_sid = "AC6ea547f6193e305f11ad917dcb4d1bb6"
		# Your Auth Token from twilio.com/console
		auth_token  = "185116e72070699a2fc180fda82573de"

		client = rest.Client(account_sid, auth_token)

		message = client.messages.create(
		    to=number, 
		    from_="+15012264574",
		    body="the reservation complete :)")							


	def list_resevrations_for_hotel(hotel_name):
		i=1
		for x in reservation.Reservations:
			if(x.hotel_name == hotel_name):
				print(str(i)+' the hotel name : '+x.hotel_name +' the customer name : '+x.customer_name)	
			i=i+1							