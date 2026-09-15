import random

class Train:

    def __init__(self, train_number, train_name, source, destination, seats):
        self.train_number = train_number
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.seats = seats

    def display_train(self):
        print("Train Number:", self.train_number)
        print("Train Name:", self.train_name)
        print("From:", self.source)
        print("To:", self.destination)
        print("Available Seats:", self.seats)

    def book_seat(self, number_of_tickets):

        if number_of_tickets <= 0:
            print("Invalid number of tickets.")
            return False

        elif number_of_tickets <= self.seats:
            self.seats -= number_of_tickets

            print("\nTickets booked successfully!")
            print("Remaining Seats:", self.seats)

            return True

        else:
            print("\nSorry! Not enough seats available.")
            return False

class Passenger:

    def __init__(self, passenger_number, name, age, gender, phone):
        self.passenger_number = passenger_number
        self.passenger_name = name
        self.passenger_age = age
        self.passenger_gender = gender
        self.passenger_number_phone = phone

    def display_passenger(self):

        print("Passenger Number:", self.passenger_number)
        print("Passenger Name:", self.passenger_name)
        print("Age:", self.passenger_age)
        print("Gender:", self.passenger_gender)
        print("Phone:", self.passenger_number_phone)

class Ticket:

    def __init__(self, passengers, train, pnr):
        self.passengers = passengers
        self.train = train
        self.pnr = pnr

    def display_ticket(self):

        print("\n")
        print("======================================")
        print("             RAILWAY TICKET")
        print("======================================")

        print("PNR:", self.pnr)
        print("Train Number:", self.train.train_number)
        print("Train Name:", self.train.train_name)
        print("From:", self.train.source)
        print("To:", self.train.destination)

        print("\n--------- PASSENGER DETAILS ----------")

        for passenger in self.passengers:

            print("\nPassenger Number:", passenger.passenger_number)
            print("Name:", passenger.passenger_name)
            print("Age:", passenger.passenger_age)
            print("Gender:", passenger.passenger_gender)
            print("Phone:", passenger.passenger_number_phone)

        print("\n======================================")
        print("          BOOKING CONFIRMED")
        print("======================================")

class Account:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):

        if self.username == username and self.password == password:
            print("\nLogin successful!")
            return True

        else:
            print("\nInvalid username or password.")
            return False

train1 = Train(
    12345,
    "East Coast Express",
    "Howrah",
    "Rajahmundry",
    100
)

train2 = Train(
    12864,
    "Howrah Express",
    "Howrah",
    "Visakhapatnam",
    80
)

account = Account(
    "neebha",
    "12345"
)


print("======================================")
print("     RAILWAY TICKET BOOKING SYSTEM")
print("======================================")

print("\n========== LOGIN ==========")

username = input("Enter username: ")
password = input("Enter password: ")

login_success = account.login(username, password)

if login_success:

    print("\n========== AVAILABLE TRAINS ==========")

    print("\n1. Train 1")
    train1.display_train()

    print("\n2. Train 2")
    train2.display_train()

    choice = int(input("\nSelect train (1 or 2): "))

    if choice == 1:

        selected_train = train1

    elif choice == 2:

        selected_train = train2

    else:

        print("Invalid train selection.")
        selected_train = None

    if selected_train:

        print("\n========== SELECTED TRAIN ==========")

        selected_train.display_train()

        number_of_tickets = int(
            input("\nEnter number of tickets: ")
        )

        if number_of_tickets <= 0:

            print("Invalid number of tickets.")

        elif number_of_tickets > selected_train.seats:

            print(
                "Sorry! Only",
                selected_train.seats,
                "seats are available."
            )

        else:

            passengers = []

            for i in range(number_of_tickets):

                print(
                    "\n===== PASSENGER",
                    i + 1,
                    "DETAILS ====="
                )

                name = input("Enter passenger name: ")

                while True:

                    try:

                        age = int(
                            input("Enter passenger age: ")
                        )

                        if age <= 0:

                            print("Age must be greater than 0.")
                        else:

                            break

                    except ValueError:

                        print("Please enter a valid age.")
                        
                gender=input("Enter passenger gender: ")

                phone = input("Enter passenger phone: ")

                passenger = Passenger(
                    i + 1,
                    name,
                    age,
                    gender,
                    phone
                )

                passengers.append(passenger)

            booking_success = selected_train.book_seat(
                number_of_tickets
            )


            if booking_success:

                pnr = random.randint(
                    100000,
                    999999
                )

                ticket = Ticket(
                    passengers,
                    selected_train,
                    pnr
                )

                print()

                ticket.display_ticket()

print("\n")
print("****************************Thank You*****************************************")                 
print("****************************Safe Journey****************************************")







