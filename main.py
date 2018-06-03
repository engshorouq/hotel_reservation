import hotel
import customer
import reservation
import sys
import hotel
import customer
import reservation

def run_app():
	choose =None	
	while choose!=0:		
		print ("=" *25 +'Hotels Reservation Program Started'+ "=" * 25)
		print ("Please Select What To Do : ")
		print ("1- Add New Hotel")
		print ("2- Find All Hotels In City")
		print ("3- Add New Reservation ")
		print ("4- Reservation In an Hotel")
		print ("0- Exit")
		choose=int(input('Please Enter What You Need :) '))
		if choose==1:
			name=input('Please Enter The Hotel Name : ')
			city=input('Please Enter The Hotel City : ')
			total_room=int(input('Please Enter The Total Room of Hotel : '))
			empty_room=int(input('Please Enter The Empty Room of Hotel : '))
			new_hotel=hotel.hotel(name,city,total_room,empty_room)
			hotel.hotel.add_hotel(new_hotel)
		elif choose==2:
			city=input('Please Enter The City : ')
			print('The hotel in the '+city+' : ')
			hotel.hotel.display_hotels_by_city_name(city)
		elif choose==3:
			hotel_name=input('Please Enter The Hotel Name : ')
			customer_name=input('Please Enter The Customer Name : ')
			new_reservation=reservation.reservation(hotel_name,customer_name)
			reservation.reservation.add_new_reservation(new_reservation)
		elif choose==4:
			hotel_name=input('Please Enter The Hotel Name : ')
			print('The Reservation in '+hotel_name+' is :')
			reservation.reservation.list_resevrations_for_hotel(hotel_name)
		else:
			print('Please Enter Correct Number')								
	Exit(0)		
	

	


run_app()

