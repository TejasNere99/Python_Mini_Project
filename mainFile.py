from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from datetime import datetime

# Function to validate date input
def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format! Please enter the date in YYYY-MM-DD format.")
        return None

# Function to calculate the difference between two dates
def date_difference(start_date, end_date):
    diff = abs(end_date - start_date)
    return diff.days

# Function to suggest activities based on trip duration
def suggest_activities(days):
    if days < 3:
        return "🏖️ Short trip! Focus on must-visit places and local cuisine."
    elif days <= 7:
        return "🌍 One-week adventure! Explore attractions and plan leisure days."
    else:
        return "🧳 Long vacation! Consider road trips, local experiences, and relaxation."

def get_coordinates(place):
    """Fetch latitude and longitude of a place using Geopy."""
    geolocator = Nominatim(user_agent="my_geopy_app", timeout=10)
    location = geolocator.geocode(place)
    
    if location:
        return (location.latitude, location.longitude)
    else:
        print(f"Error: Could not find coordinates for {place}.")
        return None

def calculate_distance(place1, place2):
    """Calculate geodesic distance between two places."""
    coords1 = get_coordinates(place1)
    coords2 = get_coordinates(place2)

    if coords1 and coords2:
        return round(geodesic(coords1, coords2).kilometers, 2)
    else:
         return None
def trip_details(place):
    famous_places = {
        "Pune": {
            "visiting_places": {
                1: "Shaniwar Wada",
                2: "Dagadusheth Halwai Ganapati Temple",
                3: "Aga Khan Palace",
                4: "Sinhagad Fort"
            },
            "food": {
                1: "Vada Pav",
                2: "Misal Pav",
                3: "Puran Poli",
                4: "Bhel Puri"
            },
            "theater": {
                1: "Bal Gandharva Rang Mandir",
                2: "Prabhat Talkies",
                3: "E-Square",
                4: "Inox"
            },
            "movies": {
                1: "Raid 2",
                2: "Marvels",
                3: "12th Fail",
                4: "Kalki"
            },
            "shopping": {
                1: "Laxmi Road",
                2: "Fergusson College Road",
                3: "MG Road",
                4: "Phoenix Market City"
            }
        },
        "Mumbai": {
            "visiting_places": {
                1: "Gateway of India",
                2: "Marine Drive",
                3: "Elephanta Caves",
                4: "Chhatrapati Shivaji Maharaj Terminus"
            },
            "food": {
                1: "Pav Bhaji",
                2: "Bhel Puri",
                3: "Vada Pav",
                4: "Dhokla"
            },
            "theater": {
                1: "Prithvi Theatre",
                2: "NCPA",
                3: "Regal Cinema",
                4: "PVR Cinemas"
            },
            "movies": {
                1: "Raid 2",
                2: "Marvels",
                3: "12th Fail",
                4: "Kalki"
            },
            "shopping": {
                1: "Colaba Causeway",
                2: "Crawford Market",
                3: "Phoenix Market City",
                4: "High Street Phoenix"
            }
        },
        "Delhi": {
            "visiting_places": { 
                1: "India Gate",
                2: "Red Fort",
                3: "Qutub Minar",
                4: "Lotus Temple"
            },
            "food": {
                1: "Chaat",
                2: "Butter Chicken",
                3: "Paranthas",
                4: "Biryani"
            },
            "theater": {
                1: "Kingdom of Dreams",
                2: "National School of Drama",
                3: "PVR Cinemas",
                4: "Satyajit Ray Film and Television Institute"
            },
            "movies": {
                1: "Raid 2",
                2: "Marvels",
                3: "12th Fail",
                4: "Kalki"
            },
            "shopping": {
                1: "Connaught Place",
                2: "Chandni Chowk",
                3: "DLF Mall of India",
                4: "Select Citywalk"
            }
        },
        "Bangalore": {
            
            "visiting_places": {
                1: "Bangalore Palace",
                2: "Cubbon Park",
                3: "Vidhana Soudha",
                4: "Lalbagh Botanical Garden"
            },
            "food": {
                1: "Bisi Bele Bath",
                2: "Mysore Pak",
                3: "Rava Idli",
                4: "Dosa"
            },
            "theater": {
                1: "Ranga Shankara",
                2: "Jagriti Theatre",
                3: "PVR Cinemas",
                4: "Inox"
            },
            "movies": {
                1: "Raid 2",
                2: "Marvels",
                3: "12th Fail",
                4: "Kalki"
            },
            "shopping": {
                1: "Brigade Road",
                2: "Commercial Street",
                3: "UB City",
                4: "Phoenix Market City"
            }
        },
        "Chennai": {
            "visiting_places": {
                1: "Marina Beach",
                2: "Kapaleeshwarar Temple",
                3: "Fort St. George",
                4: "Mahabalipuram"
            },
            "food": {
                1: "Idli",
                2: "Dosa",
                3: "Sambar",
                4: "Chettinad Chicken"
            },
            "theater": {
                1: "Sathyam Cinemas",
                2: "Escape Cinemas",
                3: "PVR Cinemas",
                4: "Inox"
            },
            "movies": {
                1: "Raid 2",
                2: "Marvels",
                3: "12th Fail",
                4: "Kalki"
            },
            "shopping": {
                1: "T Nagar",
                2: "Phoenix Market City",
                3: "Express Avenue",
                4: "Chennai Citi Centre"
            }
        }
        
    }

    place = place.title()
    if place not in famous_places:
        print("Sorry, we don't have data for that city.")
        return None

    activities = famous_places[place]
    user_choices = {}

    # Function to handle multiple choices
    def get_multiple_choices(options, category):
        print(f"\n{category} options in {place}:")
        for i, item in options.items():
            print(f"{i}. {item}")
        selected = input(f"Enter the numbers of {category.lower()} you want to choose (comma-separated): ")
        selected_indices = [int(x.strip()) for x in selected.split(",") if x.strip().isdigit()]
        return [options[i] for i in selected_indices if i in options]

    # Get choices for each category
    user_choices["visiting_places"] = get_multiple_choices(activities["visiting_places"], "Visiting Places")
    user_choices["food"] = get_multiple_choices(activities["food"], "Food")
    user_choices["theater"] = get_multiple_choices(activities["theater"], "Theater")
    user_choices["shopping"] = get_multiple_choices(activities["shopping"], "Shopping")
    user_choices["movies"] = get_multiple_choices(activities["movies"], "Movies")
    return {place: user_choices}




def food_selection(trip_days):
    # Food options with their prices
    food_menu = {
        "Breakfast": {
            "Continental Breakfast": 200,
            "Indian Breakfast": 150,
            "South Indian Breakfast": 180
        },
        "Lunch": {
            "Veg Thali": 250,
            "Non-Veg Thali": 350,
            "Fast Food Combo": 200
        },
        "Dinner": {
            "North Indian Meal": 300,
            "South Indian Meal": 280,
            "Chinese Meal": 350
        }
    }
    total_price = 0

    # Loop through each day and ask for food choices
    for day in range(1, trip_days + 1):
        print(f"\nDay {day} Food Selection:")

        for meal_type, options in food_menu.items():
            while True:  # Keep asking until a valid choice is made
                print(f"\nChoose your {meal_type}:")
                # enumerate(options.items(), 1) to start index from 1
                print("0. Skip this meal")
                for i, (food, price) in enumerate(options.items(),1):   
                    print(f"{i}. {food} - ₹{price}")

                try:
                    print("Enter the number corresponding to your choice ".ljust(70,' ')+": ",end = ' ')
                    choice = int(input())
                    if choice==0:
                        break
                    if 1 <= choice <= len(options):
                        selected_food = list(options.keys())[choice - 1]
                        total_price += options[selected_food]
                        break  # Exit loop if valid choice is made
                    else:
                        print("Invalid choice! Please enter a valid option.")
                except ValueError:
                    print("Invalid input! Please enter a valid number.")
    return total_price

def get_hotel_cost(hotel_type):
    hotel_prices = {
        1: 1000,
        2: 3000,
        3: 10000
    }
    return hotel_prices.get(hotel_type)
    

print("\t\t✈️ ✈️ ✈️  Welcome to the Travel Itinerary Planner! ✈️ ✈️ ✈️\n")
print("Plan Your Perfect Trip! \nTell us about your dream trip, and we’ll craft the perfect itinerary for you!")
# User Input
while True:
    place1 = input("Enter the first place ".ljust(70,' ')+": ")
    place2 = input("Enter the second place ".ljust(70,' ')+": ")
    distance = calculate_distance(place1, place2)
    if distance:
        print(f"Distance between {place1} and {place2}: {distance} km")
        break;
    print("Could not calculate distance. Please try again.")

# Taking user input for dates
while True:
    start_date_str = input("📅 Enter the start date of your trip (YYYY-MM-DD) ".ljust(70,' ')+": ")
    start_date = validate_date(start_date_str)
    if start_date:
        break

while True:
    end_date_str = input("📅 Enter the end date of your trip (YYYY-MM-DD) ".ljust(70,' ')+": ")
    end_date = validate_date(end_date_str)
    if end_date and end_date >= start_date:
        break
    print("❌ End date must be after or the same as the start date!")

# Calculating difference
trip_days = date_difference(start_date, end_date)


print("Preferred mode of transport?\nEnter Numbers Options Shown Below\n(Ex : For Airline Enter 1)\n1: Airline ✈️\n2: Train 🚆\n3: Bus 🚌\n4: Car 🚗")
print("Enter your choice ".ljust(70,' ')+": ", end='')
# Taking user input for mode of transport   
mode = input()
transport = {200: "Airline✈️", 1: "Train🚆", 6: "Bus🚌", 13: "Rental Car🚗"}

while True:
    if mode == "1":
        print(f"Your preferred mode of transport is {transport[200]}.")
        Tr_cost = distance * 200
        break;
    elif mode == "2":
        print(f"Your preferred mode of transport is {transport[1]}.")
        Tr_cost = distance * 1
        break;
    elif mode == "3":
        print(f"Your preferred mode of transport is {transport[6]}.")
        Tr_cost = distance * 6
        break;
    elif mode == "4":
        print(f"Your preferred mode of transport is {transport[13]}.")
        Tr_cost = distance * 13
        break;
    else:
        print("❌Invalid input. Please enter a valid option.")
print("Are you traveling solo, with family, friends, or a partner?")
print("Enter Number of Members ".ljust(70,' ')+":",end = ' ')
MemNum = int(input())
Tr_cost = Tr_cost * MemNum


#Hotel Cost
while True:
    hotel_type = int(input("Enter the type of hotel\nEnter numbers for\n1 : Budget🏠\n2 : Standard🏨\n3 : Luxury🏰\n"+"Enter your choice ".ljust(70,' ')+": "))
    if hotel_type in [1, 2, 3]:
        break
    print("Invalid option")
cost = get_hotel_cost(hotel_type)

if isinstance(cost, int):
    print(f"The estimated cost for a {hotel_type} hotel is {cost} per night.")
else:
    print("Invalid hotel type. Please enter Numeric value only.")
while True:
    print("How many nights are you planning to stay?")
    print("Enter Number of Nights ex : For two nights Enter 2".ljust(70,' ')+":",end = ' ')
    nights = int(input())
    if nights > trip_days:
        print("❌ Invalid number of nights! Please enter a positive number.")
    else:
        print(f"You are planning to stay for {nights} nights.") 
        break
hotel_cost = cost * nights
#Food Cost
food_price = food_selection(trip_days)
# Get the trip plan
trip_plan = trip_details(place2)
# Displaying results
print("\n🎉 Your trip details 🎉".ljust(30,' '))
print("📅 Start Date".ljust(30,' ')+": "+start_date_str)
print("📅 End Date".ljust(30,' ')+": "+end_date_str)
print(f"⏳ Duration".ljust(30,' ')+": "+str(trip_days)+" days")
# Show results outside the function
if trip_plan:
    for city, details in trip_plan.items():
        # print(f"\n--- Your Trip Plan for {city} ---")
        print("Visiting Places ".ljust(30, ' ') + ": " + ", ".join(details["visiting_places"]))
        print("Food Choices ".ljust(30, ' ') + ": " + ", ".join(details["food"]))
        print("Theaters ".ljust(30, ' ') + ": " + ", ".join(details["theater"]))
        print("Shopping Spots ".ljust(30, ' ') + ": " + ", ".join(details["shopping"]))
        print("Movies ".ljust(30, ' ') + ": " + ", ".join(details["movies"]))
print(f"Total Travelling Cost".ljust(30,' ')+" : ₹"+str(int(Tr_cost))) 
print(f"Total Hotel Cost".ljust(30,' ')+" : ₹"+str(int(hotel_cost)))
print(f"Total cost for food".ljust(30,' ')+" : ₹"+str(int(food_price)))
print(f"Total Cost".ljust(30,' ')+" : ₹"+str(int(Tr_cost + hotel_cost+food_price)))
print("💡 Travel Tip".ljust(30, ' ') + ": "+suggest_activities(trip_days))


print("✈️ ✈️ ✈️  Thank you for using the Travel Itinerary Planner! ✈️ ✈️ ✈️")