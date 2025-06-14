import datetime
 
def car_rental_system():
    cars = {
        "CAR001": {"type": "SUV", "available": True},
        "CAR002": {"type": "Sedan", "available": True},
        "CAR003": {"type": "Hatchback", "available": True}
    }
    users = ["user1", "user2"]
    rentals = {}
    log_file = "./week10/rental_log.txt"
 
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
            log_event(log_file, log_message)
 
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
                log_event(log_file, log_message)
            else:
                print("Car not available or invalid ID.")
                log_message = f"{datetime.datetime.now()} - {user_id} failed to rent {car_id}"
                log_event(log_file, log_message)
 
        elif choice == "3":
            user_id = input("Enter your user ID: ")
            if user_id in rentals:
                car_id = rentals[user_id]
                cars[car_id]["available"] = True
                del rentals[user_id]
                print(f"{user_id} returned {car_id}")
                log_message = f"{datetime.datetime.now()} - {user_id} returned {car_id}"
                log_event(log_file, log_message)
            else:
                print("No rental record found.")
                log_message = f"{datetime.datetime.now()} - {user_id} attempted return with no rental"
                log_event(log_file, log_message)
 
        elif choice == "4":
            print("Exiting system.")
            break
 
        else:
            print("Invalid choice.")
            log_message = f"{datetime.datetime.now()} - Invalid menu choice"
            log_event(log_file, log_message)

def get_current_timestamp():
    return datetime.datetime.now()

def log_event(file_name, event):
    with open(file_name, "a") as file:
        file.write(f"{event}\n")
        
if __name__ == "__main__":
    car_rental_system()