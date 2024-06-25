# Task 1

def string_converter(tuple_list):
    number = 1
    for item in tuple_list:
        print(f"Itinerary {number}: {item[0]} - From {item[1]} to {item[2]}.")
        number += 1



flights = [("Tom", "New York", "London"), ("Fred", "Tokyo", "Los Angeles"), ("Allen", "Atlanta", "PBI")]



string_converter(flights)