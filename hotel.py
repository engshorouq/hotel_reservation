class hotel():
	Hotels=[]
	def __init__(self,hotel_name,hotel_city,total_rooms,empty_rooms):
		assert str is type(hotel_name) and hotel_name is not None , "requires a string"		
		assert str is type(hotel_city) and hotel_city is not None, "requires a string"
		assert int is type(total_rooms) and total_rooms>0 ,	"requires a Number"
		assert int is type(empty_rooms) and empty_rooms>0 and total_rooms>=empty_rooms ,"requires a Number"	
		self.hotel_name=hotel_name
		self.hotel_city=hotel_city
		self.total_rooms=total_rooms
		self.empty_rooms=empty_rooms

	def add_hotel(self):
		for ht in hotel.Hotels:
			if(ht.hotel_name == self.hotel_name):
				hotel.Hotels.remove(ht)
				print('removed')
		hotel.Hotels.append(self)
		print('The hotel name : '+self.hotel_name+' City : '+self.hotel_city +' Total rooms : '+str(self.total_rooms)+' Empty rooms : '+str(self.empty_rooms))
		print('Added')						
		
	def display_hotels_by_city_name(hotel_city):
		i=1
		for ht in hotel.Hotels:
			if ht.hotel_city == hotel_city:
				print(str(i)+' The hotel name : '+ht.hotel_name)			
			i=i+1	

	