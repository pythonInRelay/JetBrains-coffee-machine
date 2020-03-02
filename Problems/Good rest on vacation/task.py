trip_duration = int(input())
food_cost = int(input())
return_ticket = int(input())
hotel_cost = int(input())

print((return_ticket * 2) + (food_cost * trip_duration) + (hotel_cost * (trip_duration - 1)))
