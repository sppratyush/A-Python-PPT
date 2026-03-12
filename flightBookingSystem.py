"""6.Flight Booking System 
A system to search, book, and cancel flight tickets. 
Handle exceptions such as seat not available, invalid passenger details, payment 
failure."""
class FlightBookingSystem:
    def __init__(self):
        self.flights = {"FL001": {"seats": 100, "price": 200}}
        self.bookings = {}

    def search_flight(self, flight_id):
        if flight_id not in self.flights:
            raise KeyError("Flight ID does not exist.")
        return self.flights[flight_id]

    def book_ticket(self, booking_id, flight_id, passenger_name):
        if flight_id not in self.flights:
            raise KeyError("Flight ID does not exist.")
        if self.flights[flight_id]["seats"] <= 0:
            raise ValueError("No seats available.")
        if not passenger_name:
            raise ValueError("Passenger name cannot be empty.")
        self.bookings[booking_id] = {"flight_id": flight_id, "passenger_name": passenger_name}
        self.flights[flight_id]["seats"] -= 1

    def cancel_booking(self, booking_id):
        if booking_id not in self.bookings:
            raise KeyError("Booking ID does not exist.")
        flight_id = self.bookings[booking_id]["flight_id"]
        del self.bookings[booking_id]
        self.flights[flight_id]["seats"] += 1
# Example usage
if __name__ == "__main__":
    flight_system = FlightBookingSystem()
    try:
        flight_system.book_ticket("B001", "FL001", "John Doe")
        print(flight_system.bookings)  # Output: {'B001': {'flight_id': 'FL001', 'passenger_name': 'John Doe'}}
        flight_system.cancel_booking("B001")
        print(flight_system.bookings)  # Output: {}
        flight_system.cancel_booking("B002")  # This will raise an exception
    except (ValueError, KeyError) as e:
        print("Error:", e)
        