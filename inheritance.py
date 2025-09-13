# # 1. Flight and ScheduledFlight

# class Flight:
#     def __init__(self, flight_number, airline):
#         self.flight_number = flight_number
#         self.airline = airline

#     def display_info(self):
#         print(f"Flight Number: {self.flight_number}")
#         print(f"Airline: {self.airline}")


# class ScheduledFlight(Flight):
#     def __init__(self, flight_number, airline, departure_time, arrival_time):
#         super().__init__(flight_number, airline)
#         self.departure_time = departure_time
#         self.arrival_time = arrival_time

#     def display_info(self):
#         super().display_info()
#         print(f"Departure Time: {self.departure_time}")
#         print(f"Arrival Time: {self.arrival_time}")


# # 2. Person, CrewMember, Pilot

# class Person:
#     def __init__(self, name, id_number):
#         self.name = name
#         self.id_number = id_number

#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"ID: {self.id_number}")


# class CrewMember(Person):
#     def __init__(self, name, id_number, role):
#         super().__init__(name, id_number)
#         self.role = role

#     def display(self):
#         super().display()
#         print(f"Role: {self.role}")


# class Pilot(CrewMember):
#     def __init__(self, name, id_number, license_number, rank):
#         super().__init__(name, id_number, "Pilot")
#         self.license_number = license_number
#         self.rank = rank

#     def display(self):
#         super().display()
#         print(f"License Number: {self.license_number}")
#         print(f"Rank: {self.rank}")


# # 3. Service, SecurityService, BaggageService

# class Service:
#     def service_info(self):
#         print("General airport service.")


# class SecurityService(Service):
#     def service_info(self):
#         print("Security Service: Responsible for passenger and baggage screening.")


# class BaggageService(Service):
#     def service_info(self):
#         print("Baggage Service: Handles baggage check-in and retrieval.")


# # 4. PassengerDetails, TicketDetails, Booking (Multiple Inheritance)

# class PassengerDetails:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class TicketDetails:
#     def __init__(self, ticket_number, seat_number):
#         self.ticket_number = ticket_number
#         self.seat_number = seat_number


# class Booking(PassengerDetails, TicketDetails):
#     def __init__(self, name, age, ticket_number, seat_number):
#         PassengerDetails.__init__(self, name, age)
#         TicketDetails.__init__(self, ticket_number, seat_number)

#     def display(self):
#         print(f"Passenger Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Ticket Number: {self.ticket_number}")
#         print(f"Seat Number: {self.seat_number}")


# # Example usage
# if __name__ == "__main__":
#     sf = ScheduledFlight("AI202", "Air India", "10:00", "14:00")
#     sf.display_info()

#     print("\n--- Pilot Info ---")
#     pilot = Pilot("John Doe", "C123", "LN456", "Captain")
#     pilot.display()

#     print("\n--- Services ---")
#     sec = SecurityService()
#     sec.service_info()

#     bag = BaggageService()
#     bag.service_info()

#     print("\n--- Booking Info ---")
#     booking = Booking("Alice", 30, "T789", "12A")
#     booking.display()
