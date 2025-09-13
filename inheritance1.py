import json
import os

# -------- Flight Classes --------
class Flight:
    def __init__(self, flight_number, airline):
        self.flight_number = flight_number
        self.airline = airline


class ScheduledFlight(Flight):
    def __init__(self, flight_number, airline, departure_time, arrival_time):
        super().__init__(flight_number, airline)
        self.departure_time = departure_time
        self.arrival_time = arrival_time


# -------- Person Classes --------
class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number


class CrewMember(Person):
    def __init__(self, name, id_number, role):
        super().__init__(name, id_number)
        self.role = role


class Pilot(CrewMember):
    def __init__(self, name, id_number, license_number, rank):
        super().__init__(name, id_number, "Pilot")
        self.license_number = license_number
        self.rank = rank


# -------- Service Classes --------
class Service:
    def service_info(self):
        print("General service.")


class SecurityService(Service):
    def __init__(self, info):
        self.info = info

    def service_info(self):
        print(f"Security Service: {self.info}")


class BaggageService(Service):
    def __init__(self, info):
        self.info = info

    def service_info(self):
        print(f"Baggage Service: {self.info}")


# -------- Booking Classes (Multiple Inheritance) --------
class PassengerDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class TicketDetails:
    def __init__(self, ticket_number, seat_number):
        self.ticket_number = ticket_number
        self.seat_number = seat_number


class Booking(PassengerDetails, TicketDetails):
    def __init__(self, passenger, ticket):
        PassengerDetails.__init__(self, passenger["name"], passenger["age"])
        TicketDetails.__init__(self, ticket["ticket_number"], ticket["seat_number"])


# -------- Load JSON --------
def load_data(filename):
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, filename)
    with open(file_path, "r") as f:
        return json.load(f)


# -------- Main Menu --------
def main():
    data = load_data("data.json")

    # Flights
    flights = [ScheduledFlight(**f) for f in data["flights"]]

    # Pilots
    pilots = [Pilot(**p) for p in data["pilots"]]

    # Passengers & Tickets
    passengers = data["passengers"]
    tickets = data["tickets"]

    # Bookings: combine passenger + ticket based on booking indexes
    bookings = [Booking(passengers[b["passenger_index"]], tickets[b["ticket_index"]])
                for b in data["bookings"]]

    total_records = min(len(flights), len(pilots), len(bookings))

    while True:
        print("\n--- Airport System Menu ---")
        print(f"Enter a number between 1 and {total_records} to see one record")
        print("0 to Exit")

        choice = input("Enter choice: ")

        if choice == "0":
            print("Exiting...")
            break

        if not choice.isdigit():
            print("Invalid input. Enter a number.")
            continue

        index = int(choice) - 1
        if 0 <= index < total_records:
            f = flights[index]
            p = pilots[index]
            b = bookings[index]

            print("\n--- Flight Info ---")
            print(f"Flight: {f.flight_number}, Airline: {f.airline}, "
                  f"Departure: {f.departure_time}, Arrival: {f.arrival_time}")

            print("\n--- Pilot Info ---")
            print(f"Name: {p.name}, ID: {p.id_number}, "
                  f"License: {p.license_number}, Rank: {p.rank}")

            print("\n--- Booking Info ---")
            print(f"Passenger: {b.name}, Age: {b.age}, "
                  f"Ticket: {b.ticket_number}, Seat: {b.seat_number}")
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
