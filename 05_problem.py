#Write a class Train which has methods to book a ticket, get status (no of seats) and get fare information of train running under indian Railways.
import random

class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def get_status(self):
        print(f"Train name: {self.name}")
        print(f"Available seats: {self.seats}")

    def get_fare_info(self):
        print(f"Fare per ticket: ₹{self.fare}")

    def book_ticket(self):
        if self.seats > 0:
            seat_no = random.randint(1, 100)
            print("Ticket booked successfully!")
            print(f"Your seat number is: {seat_no}")
            self.seats -= 1
            print(f"Seats left: {self.seats}")
        else:
            print("Sorry, no seats available.")
