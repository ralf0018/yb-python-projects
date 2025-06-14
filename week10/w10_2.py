import datetime

def car_rental_system():
    """Main function that runs the car rental system."""
    cars = initialize_cars()
    users = initialize_users()
    rentals = {}
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            view_available_cars(cars)
            log_event("View", "system", "Viewed available cars")
            
        elif choice == "2":
            rent_car(cars, users, rentals)
            
        elif choice == "3":
            return_car(cars, rentals)
            
        elif choice == "4":
            print("Exiting system.")
            break
            
        else:
            print("Invalid choice.")
            log_event("Error", "system", "Invalid menu choice")

# Supporting functions below
def initialize_cars():
    """Initialize the car inventory."""
    return {
        "CAR001": {"type": "SUV", "available": True},
        "CAR002": {"type": "Sedan", "available": True},
        "CAR003": {"type": "Hatchback", "available": True}
    }

def initialize_users():
    """Initialize the user list."""
    return ["user1", "user2"]

def display_menu():
    """Display the menu and return user's choice."""
    print("\n--- Car Rental System ---")
    print("1. View Available Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Exit")
    return input("Enter your choice: ")

def view_available_cars(cars):
    """Display all available cars."""
    print("\nAvailable Cars:")
    for car_id, details in cars.items():
        if details["available"]:
            print(f"{car_id} - {details['type']}")

def rent_car(cars, users, rentals):
    """Handle the car rental process."""
    user_id = input("Enter your user ID: ")
    
    if user_id not in users:
        print("Invalid user.")
        return
    
    view_available_cars(cars)
    car_id = input("Enter Car ID to rent: ")
    
    if car_id in cars and cars[car_id]["available"]:
        cars[car_id]["available"] = False
        rentals[user_id] = car_id
        print(f"{user_id} rented {car_id}")
        log_event("Rental", user_id, f"rented {car_id}")
    else:
        print("Car not available or invalid ID.")
        log_event("Error", user_id, f"failed to rent {car_id}")

def return_car(cars, rentals):
    """Handle the car return process."""
    user_id = input("Enter your user ID: ")
    
    if user_id in rentals:
        car_id = rentals[user_id]
        cars[car_id]["available"] = True
        del rentals[user_id]
        print(f"{user_id} returned {car_id}")
        log_event("Return", user_id, f"returned {car_id}")
    else:
        print("No rental record found.")
        log_event("Error", user_id, "attempted return with no rental")

def log_event(event_type, user_id, message):
    """Log an event to the rental log file."""
    timestamp = datetime.datetime.now()
    log_message = f"{timestamp} - {user_id} {message}"
    with open("./week10/rental_log.txt", "a") as log_file:
        log_file.write(log_message + "\n")
        
if __name__ == "__main__":
    car_rental_system()

''' 
Original Code

def car_rental_system():
    cars = {
        "CAR001": {"type": "SUV", "available": True},
        "CAR002": {"type": "Sedan", "available": True},
        "CAR003": {"type": "Hatchback", "available": True}
    }
    users = ["user1", "user2"]
    rentals = {}
 
    while True:
        print("\n--- Car Rental System ---")
        print("1. View Available Cars")
        print("2. Rent a Car")
        print("3. Return a Car")
        print("4. Exit")
        choice = input("Enter your choice: ")
 
        if choice == "1":
            print("\nAvailable Cars:")
            for car_id, details in cars.items():
                if details["available"]:
                    print(f"{car_id} - {details['type']}")
            log_message = f"{datetime.datetime.now()} - Viewed available cars"
            with open("rental_log.txt", "a") as log_file:
                log_file.write(log_message + "\n")
 
        elif choice == "2":
            user_id = input("Enter your user ID: ")
            if user_id not in users:
                print("Invalid user.")
                continue
 
            print("\nAvailable Cars:")
            for car_id, details in cars.items():
                if details["available"]:
                    print(f"{car_id} - {details['type']}")
            car_id = input("Enter Car ID to rent: ")
 
            if car_id in cars and cars[car_id]["available"]:
                cars[car_id]["available"] = False
                rentals[user_id] = car_id
                print(f"{user_id} rented {car_id}")
                log_message = f"{datetime.datetime.now()} - {user_id} rented {car_id}"
                with open("rental_log.txt", "a") as log_file:
                    log_file.write(log_message + "\n")
            else:
                print("Car not available or invalid ID.")
                log_message = f"{datetime.datetime.now()} - {user_id} failed to rent {car_id}"
                with open("rental_log.txt", "a") as log_file:
                    log_file.write(log_message + "\n")
 
        elif choice == "3":
            user_id = input("Enter your user ID: ")
            if user_id in rentals:
                car_id = rentals[user_id]
                cars[car_id]["available"] = True
                del rentals[user_id]
                print(f"{user_id} returned {car_id}")
                log_message = f"{datetime.datetime.now()} - {user_id} returned {car_id}"
                with open("rental_log.txt", "a") as log_file:
                    log_file.write(log_message + "\n")
            else:
                print("No rental record found.")
                log_message = f"{datetime.datetime.now()} - {user_id} attempted return with no rental"
                with open("rental_log.txt", "a") as log_file:
                    log_file.write(log_message + "\n")
 
        elif choice == "4":
            print("Exiting system.")
            break
 
        else:
            print("Invalid choice.")
            log_message = f"{datetime.datetime.now()} - Invalid menu choice"
            with open("rental_log.txt", "a") as log_file:
                log_file.write(log_message + "\n")
'''
